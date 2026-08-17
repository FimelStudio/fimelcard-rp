param(
    [string]$TextureDir = (Join-Path $PSScriptRoot '..\assets\card\textures\item\poker'),
    [string]$OutputDir = $TextureDir,
    [string]$BackupDir = (Join-Path $PSScriptRoot '..\.backup\poker_jqk_static'),
    [switch]$SkipBackup
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$frameSize = 48
$frameCount = 12
$glyphX = 15
$glyphY = 21

# 5×7字模只覆盖牌面中央；角标区域不参与任何处理。
$glyphs = @{
    j = @(
        '11111',
        '00010',
        '00010',
        '00010',
        '00010',
        '10010',
        '01100'
    );
    q = @(
        '01110',
        '10001',
        '10001',
        '10001',
        '10101',
        '10010',
        '01101'
    );
    k = @(
        '10001',
        '10010',
        '10100',
        '11000',
        '10100',
        '10010',
        '10001'
    );
}

function Get-ColorKey {
    param([System.Drawing.Color]$Color)
    return '{0:X2}{1:X2}{2:X2}{3:X2}' -f $Color.A, $Color.R, $Color.G, $Color.B
}

function Blend-Color {
    param(
        [System.Drawing.Color]$Source,
        [System.Drawing.Color]$Target,
        [double]$Amount
    )
    $r = [int][Math]::Round($Source.R + (($Target.R - $Source.R) * $Amount))
    $g = [int][Math]::Round($Source.G + (($Target.G - $Source.G) * $Amount))
    $b = [int][Math]::Round($Source.B + (($Target.B - $Source.B) * $Amount))
    return [System.Drawing.Color]::FromArgb($Source.A, $r, $g, $b)
}

function Test-GlyphPixel {
    param(
        [string[]]$Glyph,
        [int]$X,
        [int]$Y
    )
    if ($Y -lt 0 -or $Y -ge $Glyph.Count -or $X -lt 0 -or $X -ge $Glyph[0].Length) {
        return $false
    }
    return $Glyph[$Y][$X] -eq '1'
}

function Add-CentralLetter {
    param(
        [System.Drawing.Bitmap]$Bitmap,
        [string[]]$Glyph,
        [System.Drawing.Color]$Outline
    )

    $letterPixels = [System.Collections.Generic.HashSet[string]]::new()
    for ($gy = 0; $gy -lt $Glyph.Count; $gy++) {
        for ($gx = 0; $gx -lt $Glyph[$gy].Length; $gx++) {
            if (Test-GlyphPixel -Glyph $Glyph -X $gx -Y $gy) {
                [void]$letterPixels.Add("$($glyphX + $gx),$($glyphY + $gy)")
            }
        }
    }

    # 先绘制一像素深色描边，再绘制稳定不闪烁的暖金字母。
    foreach ($point in $letterPixels) {
        $parts = $point.Split(',')
        $x = [int]$parts[0]
        $y = [int]$parts[1]
        for ($oy = -1; $oy -le 1; $oy++) {
            for ($ox = -1; $ox -le 1; $ox++) {
                if ($ox -eq 0 -and $oy -eq 0) {
                    continue
                }
                $nx = $x + $ox
                $ny = $y + $oy
                if ($nx -ge 6 -and $nx -le 29 -and $ny -ge 15 -and $ny -le 32 -and
                    -not $letterPixels.Contains("$nx,$ny")) {
                    $Bitmap.SetPixel($nx, $ny, $Outline)
                }
            }
        }
    }

    $gold = [System.Drawing.Color]::FromArgb(255, 241, 199, 91)
    $goldHighlight = [System.Drawing.Color]::FromArgb(255, 255, 235, 167)
    $goldShadow = [System.Drawing.Color]::FromArgb(255, 202, 139, 43)

    for ($gy = 0; $gy -lt $Glyph.Count; $gy++) {
        for ($gx = 0; $gx -lt $Glyph[$gy].Length; $gx++) {
            if (-not (Test-GlyphPixel -Glyph $Glyph -X $gx -Y $gy)) {
                continue
            }

            $color = $gold
            if (-not (Test-GlyphPixel -Glyph $Glyph -X $gx -Y ($gy - 1))) {
                $color = $goldHighlight
            }
            elseif (-not (Test-GlyphPixel -Glyph $Glyph -X $gx -Y ($gy + 1))) {
                $color = $goldShadow
            }

            $Bitmap.SetPixel($glyphX + $gx, $glyphY + $gy, $color)
        }
    }
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
if (-not $SkipBackup) {
    New-Item -ItemType Directory -Force -Path $BackupDir | Out-Null
}

$blackPalette = [System.Collections.Generic.HashSet[string]]::new(
    [string[]]@('FF2B2D33', 'FF37383C', 'FF323438', 'FF34363A')
)
$redPalette = [System.Collections.Generic.HashSet[string]]::new(
    [string[]]@('FF812E2C', 'FFAF302E', 'FF9E2E2C', 'FFC93332')
)

foreach ($suit in @('c', 'd', 'h', 's')) {
    foreach ($rank in @('j', 'q', 'k')) {
        $name = "${suit}_${rank}"
        $sourcePath = Join-Path $TextureDir "$name.png"
        $outputPath = Join-Path $OutputDir "$name.png"
        $metaPath = "$outputPath.mcmeta"

        if (-not (Test-Path -LiteralPath $sourcePath)) {
            throw "缺少源纹理：$sourcePath"
        }

        $sourceImage = [System.Drawing.Bitmap]::new($sourcePath)
        if ($sourceImage.Width -ne $frameSize -or $sourceImage.Height -lt $frameSize) {
            $sourceImage.Dispose()
            throw "纹理尺寸无效：$sourcePath"
        }

        # 已经是动画帧条时取第一帧作为基准，使脚本可重复执行。
        $baseFrame = [System.Drawing.Bitmap]::new($frameSize, $frameSize, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
        for ($y = 0; $y -lt $frameSize; $y++) {
            for ($x = 0; $x -lt $frameSize; $x++) {
                $baseFrame.SetPixel($x, $y, $sourceImage.GetPixel($x, $y))
            }
        }

        if (-not $SkipBackup -and $sourceImage.Height -eq $frameSize) {
            Copy-Item -LiteralPath $sourcePath -Destination (Join-Path $BackupDir "$name.png") -Force
            if (Test-Path -LiteralPath "$sourcePath.mcmeta") {
                Copy-Item -LiteralPath "$sourcePath.mcmeta" -Destination (Join-Path $BackupDir "$name.png.mcmeta") -Force
            }
        }
        $sourceImage.Dispose()

        $strip = [System.Drawing.Bitmap]::new(
            $frameSize,
            $frameSize * $frameCount,
            [System.Drawing.Imaging.PixelFormat]::Format32bppArgb
        )

        $isRed = $suit -in @('d', 'h')
        $palette = if ($isRed) { $redPalette } else { $blackPalette }
        $shineTarget = if ($isRed) {
            [System.Drawing.Color]::FromArgb(255, 235, 82, 75)
        }
        else {
            [System.Drawing.Color]::FromArgb(255, 104, 108, 119)
        }
        $outline = if ($isRed) {
            [System.Drawing.Color]::FromArgb(255, 91, 27, 25)
        }
        else {
            [System.Drawing.Color]::FromArgb(255, 31, 32, 38)
        }

        for ($frameIndex = 0; $frameIndex -lt $frameCount; $frameIndex++) {
            $frame = [System.Drawing.Bitmap]::new($baseFrame)
            $shineX = -1.0 + (3.0 * $frameIndex)

            # 高光只识别中央图案原有的黑/红调色板，并限制在中央矩形。
            for ($y = 15; $y -le 32; $y++) {
                for ($x = 6; $x -le 29; $x++) {
                    $color = $frame.GetPixel($x, $y)
                    if (-not $palette.Contains((Get-ColorKey -Color $color))) {
                        continue
                    }

                    $distance = [Math]::Abs($x - $shineX)
                    if ($distance -le 0.55) {
                        $frame.SetPixel($x, $y, (Blend-Color -Source $color -Target $shineTarget -Amount 0.42))
                    }
                    elseif ($distance -le 1.55) {
                        $frame.SetPixel($x, $y, (Blend-Color -Source $color -Target $shineTarget -Amount 0.18))
                    }
                }
            }

            Add-CentralLetter -Bitmap $frame -Glyph $glyphs[$rank] -Outline $outline

            for ($y = 0; $y -lt $frameSize; $y++) {
                for ($x = 0; $x -lt $frameSize; $x++) {
                    $strip.SetPixel($x, ($frameIndex * $frameSize) + $y, $frame.GetPixel($x, $y))
                }
            }
            $frame.Dispose()
        }

        $baseFrame.Dispose()
        $temporaryPath = "$outputPath.building.png"
        $strip.Save($temporaryPath, [System.Drawing.Imaging.ImageFormat]::Png)
        $strip.Dispose()
        Move-Item -LiteralPath $temporaryPath -Destination $outputPath -Force

        $meta = "{`n  `"animation`": {`n    `"frametime`": 3,`n    `"interpolate`": true`n  }`n}`n"
        [System.IO.File]::WriteAllText($metaPath, $meta, [System.Text.UTF8Encoding]::new($false))
        Write-Host "已生成 $name"
    }
}
