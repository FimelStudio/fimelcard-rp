"""Export the generated UNO atlas to the existing 48 px card/box UV layouts.

Pillow is the sole dependency. Run from any directory:
    python .source/uno/export_assets.py --art /path/to/generated.png
The atlas is AI-drawn artwork. This exporter only crops/recolours its panels and
adds deterministic pixel glyphs, so numbers and action icons remain exact.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw


SOURCE = Path(__file__).resolve().parent
PACK = SOURCE.parents[1]
ASSETS = PACK / "assets" / "card"
IVORY = (255, 246, 217, 255)
INK = (28, 28, 31, 255)
COLOURS = [(224, 20, 31), (244, 193, 18), (30, 162, 68), (29, 118, 218)]
COLOUR_NAMES = ["red", "yellow", "green", "blue"]
PIXELS = {
    "0": ["01110", "11011", "11011", "11011", "11011", "11011", "01110"],
    "1": ["00110", "01110", "00110", "00110", "00110", "00110", "01111"],
    "2": ["01110", "11011", "00011", "00110", "01100", "11000", "11111"],
    "3": ["11110", "00011", "00011", "01110", "00011", "00011", "11110"],
    "4": ["00011", "00111", "01111", "11011", "11111", "00011", "00011"],
    "5": ["11111", "11000", "11000", "11110", "00011", "00011", "11110"],
    "6": ["01110", "11000", "11000", "11110", "11011", "11011", "01110"],
    "7": ["11111", "00011", "00110", "00110", "01100", "01100", "01100"],
    "8": ["01110", "11011", "11011", "01110", "11011", "11011", "01110"],
    "9": ["01110", "11011", "11011", "01111", "00011", "00011", "01110"],
    "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
}


def asset_name(index: int) -> str:
    if index == 52:
        return "wild"
    if index == 53:
        return "wild_plus4"
    value = index % 13
    rank = str(value) if value < 10 else ["skip", "reverse", "plus2"][value - 10]
    return "rygb"[index // 13] + rank


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def glyph(text: str) -> Image.Image:
    result = Image.new("RGBA", (len(text) * 6 - 1, 7))
    for pos, char in enumerate(text):
        for y, row in enumerate(PIXELS[char]):
            for x, bit in enumerate(row):
                if bit == "1":
                    result.putpixel((pos * 6 + x, y), IVORY)
    return result


def icon(value: int, small: bool = False) -> Image.Image:
    if value <= 9:
        return glyph(str(value))
    if value == 12:
        return glyph("+2")
    if value == 53:
        return glyph("+4")
    # Draw action glyphs at their final pixel size. Shrinking thick 11 px
    # artwork to a corner used to close the gaps and blur the two arrows.
    if value in (10, 11):
        return action_icon(value, small)
    result = Image.new("RGBA", (11, 11))
    draw = ImageDraw.Draw(result)
    if value == 52:
        for bounds, colour in zip([(1, 1, 5, 5), (6, 1, 10, 5), (1, 6, 5, 10), (6, 6, 10, 10)], COLOURS):
            draw.rectangle(bounds, fill=colour + (255,))
    else:
        raise ValueError(value)
    if small:
        result = result.resize((7, 7), Image.Resampling.NEAREST)
    return result


def action_icon(value: int, small: bool) -> Image.Image:
    """Native-size, thin symbols with open counters and distinct arrows."""
    size = 9 if small else (15 if value == 10 else 17)
    result = Image.new("RGBA", (size, size))
    draw = ImageDraw.Draw(result)
    if value == 10:
        # A one-pixel ring plus slash leaves both triangular counters open.
        # The 9 px corner is drawn separately rather than downsampled.
        if small:
            draw.ellipse((0, 0, 8, 8), outline=IVORY, width=1)
            draw.line((1, 7, 7, 1), fill=IVORY, width=1)
        else:
            draw.ellipse((1, 1, 13, 13), outline=IVORY, width=1)
            draw.line((3, 11, 11, 3), fill=IVORY, width=1)
        return result

    upper = Image.new("RGBA", (size, size))
    arrow = ImageDraw.Draw(upper)
    if small:
        # The hooked tail identifies the bend; the opposite arrow is a
        # half-turn of this one, retaining a clean gap between the heads.
        arrow.line([(0, 3), (0, 2), (1, 1), (6, 1)], fill=IVORY, width=1)
        arrow.polygon([(5, 0), (8, 2), (5, 3)], fill=IVORY)
    else:
        # Two 2 px shafts bend around each other. Three empty rows between
        # arrows keep a visible coloured gap after the one-pixel outline.
        arrow.polygon([(1, 6), (1, 4), (3, 2), (10, 2), (10, 0),
                       (16, 3), (10, 6), (10, 4), (4, 4),
                       (3, 5), (3, 6)], fill=IVORY)
    result.alpha_composite(upper)
    result.alpha_composite(upper.transpose(Image.Transpose.ROTATE_180))
    return result


def underline_digit(source: Image.Image, gap: int, thickness: int) -> Image.Image:
    """Keep six/nine orientation readable in both rotated corner labels."""
    result = Image.new("RGBA", (source.width, source.height + gap + thickness))
    result.alpha_composite(source)
    ImageDraw.Draw(result).rectangle((0, source.height + gap,
                                     source.width - 1, result.height - 1), fill=IVORY)
    return result


def outlined_paste(target: Image.Image, source: Image.Image, at: tuple[int, int], outline: bool = True, uniform_outline: bool = False) -> None:
    if outline:
        ink = Image.new("RGBA", source.size, INK)
        ink.putalpha(source.getchannel("A"))
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if not uniform_outline:
            offsets.append((1, 1))
        for dx, dy in offsets:
            target.alpha_composite(ink, (at[0] + dx, at[1] + dy))
    target.alpha_composite(source, at)


def recolour(image: Image.Image, colour: tuple[int, int, int] | None) -> Image.Image:
    result = image.copy()
    for y in range(result.height):
        for x in range(result.width):
            r, g, b, a = result.getpixel((x, y))
            if r > 80 and g < r * 0.58 and b < r * 0.58:
                if colour is None:
                    value = 25 + round((r - 160) * 0.05)
                    result.putpixel((x, y), (value, value, value + 3, a))
                else:
                    shade = min(1.08, max(0.88, r / 224))
                    result.putpixel((x, y), tuple(min(255, round(c * shade)) for c in colour) + (a,))
    return result


def make_face(blank: Image.Image, index: int) -> Image.Image:
    value = index % 13 if index < 52 else index
    face = recolour(blank, COLOURS[index // 13] if index < 52 else None)
    # Keep the generated ellipse and render exact, readable symbols at its centre.
    center = icon(value)
    if value <= 9:
        center = center.resize((10, 14), Image.Resampling.NEAREST)
        if value in (6, 9):
            center = underline_digit(center, gap=2, thickness=2)
    elif value in (12, 53):
        center = center.resize((17, 11), Image.Resampling.NEAREST)
    elif value not in (10, 11):
        center = center.resize((14, 14), Image.Resampling.NEAREST)
    outlined_paste(face, center, ((26 - center.width) // 2, (44 - center.height) // 2), uniform_outline=value in (10, 11))
    corner = icon(value, small=True)
    if value in (6, 9):
        corner = underline_digit(corner, gap=1, thickness=1)
    # +2/+4 fit within the 26 px face at the original 11 px width.
    outlined_paste(face, corner, (2, 3), outline=False)
    opposite = corner.transpose(Image.Transpose.ROTATE_180)
    outlined_paste(face, opposite, (24 - opposite.width, 41 - opposite.height), outline=False)
    return face


def card_uv(face: Image.Image) -> Image.Image:
    uv = Image.new("RGBA", (48, 48), IVORY)
    uv.paste(face, (4, 2))
    # Model border strips at x=2..4/30..32 and top/bottom stay ivory.
    return uv


def selected_face(face: Image.Image) -> Image.Image:
    """A luminous two-pixel frame; keep glyph size and advance unchanged."""
    result = face.copy()
    draw = ImageDraw.Draw(result)
    draw.rounded_rectangle((0, 0, 25, 43), radius=2,
                           outline=(255, 194, 28, 255), width=2)
    draw.rounded_rectangle((1, 1, 24, 42), radius=1,
                           outline=(255, 248, 168, 255), width=1)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--art", type=Path, default=SOURCE / "art-atlas.png")
    args = parser.parse_args()
    SOURCE.mkdir(parents=True, exist_ok=True)
    atlas_path = SOURCE / "art-atlas.png"
    if args.art.resolve() != atlas_path.resolve():
        shutil.copy2(args.art, atlas_path)
    atlas = Image.open(atlas_path).convert("RGBA")
    width, height = atlas.size
    # Exclude the black outer frame and the grid's divider. Ratios support re-export.
    def panel(bounds: tuple[float, float, float, float], size: tuple[int, int]) -> Image.Image:
        return atlas.crop(tuple(round(v * (width if i % 2 == 0 else height)) for i, v in enumerate(bounds))).resize(size, Image.Resampling.NEAREST)

    blank = panel((0.004, 0.004, 0.497, 0.493), (26, 44))
    back = panel((0.504, 0.004, 0.997, 0.493), (26, 44))
    box_front = panel((0.004, 0.497, 0.497, 0.996), (30, 48))
    box_side = panel((0.504, 0.501, 0.997, 0.996), (6, 48))
    item_dir = ASSETS / "textures" / "item" / "uno"
    font_dir = ASSETS / "textures" / "font" / "uno"
    item_dir.mkdir(parents=True, exist_ok=True)
    font_dir.mkdir(parents=True, exist_ok=True)
    (font_dir / "selected").mkdir(parents=True, exist_ok=True)
    faces = []
    providers = []
    selected_providers = []
    for index in range(54):
        name = asset_name(index)
        face = make_face(blank, index)
        faces.append(face)
        card_uv(face).save(item_dir / f"{name}.png")
        face.save(font_dir / f"{name}.png")
        selected_face(face).save(font_dir / "selected" / f"{name}.png")
        model = f"card:item/uno/{name}"
        dump(ASSETS / "models" / "item" / "uno" / f"{name}.json", {
            "parent": "card:item/fake_card",
            "textures": {"0": f"card:item/uno/{name}", "1": "card:item/uno/back_flipped", "particle": f"card:item/uno/{name}"},
        })
        dump(ASSETS / "items" / "uno" / f"{name}.json", {
            "model": {"type": "minecraft:select", "property": "minecraft:display_context", "cases": [
                {"when": ["thirdperson_righthand", "thirdperson_lefthand"], "model": {"type": "minecraft:model", "model": "card:item/uno/back"}},
            ], "fallback": {"type": "minecraft:model", "model": model}},
        })
        # DDZ assembles six 9px slices into a 54px card. Match that height,
        # retaining UNO's narrower card aspect ratio and independent HUD fonts.
        providers.append({"type": "bitmap", "file": f"card:font/uno/{name}.png", "height": 54, "ascent": 50, "chars": [chr(0xE600 + index)]})
        selected_providers.append({"type": "bitmap", "file": f"card:font/uno/selected/{name}.png", "height": 54, "ascent": 50, "chars": [chr(0xE600 + index)]})
    card_uv(back).save(item_dir / "back.png")
    # fake_card's south face runs U from 10 to 1.33333. Pre-flip only its #1 UV
    # texture, leaving #0/back and the held-item front artwork naturally readable.
    back_flipped = back.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    card_uv(back_flipped).save(item_dir / "back_flipped.png")
    dump(ASSETS / "models" / "item" / "uno" / "back.json", {"parent": "card:item/fake_card", "textures": {"0": "card:item/uno/back", "1": "card:item/uno/back_flipped", "particle": "card:item/uno/back"}})
    box = Image.new("RGBA", (48, 48), INK)
    box.paste(box_front, (2, 0))
    box.paste(box_side, (42, 0))
    box.save(item_dir / "box.png")
    dump(ASSETS / "models" / "item" / "uno" / "box.json", {"parent": "card:item/cardbox", "textures": {"0": "card:item/uno/box", "particle": "card:item/uno/box"}})
    for name in ["back", "box"]:
        dump(ASSETS / "items" / "uno" / f"{name}.json", {"model": {"type": "minecraft:model", "model": f"card:item/uno/{name}"}})
    dump(ASSETS / "font" / "uno" / "dialog.json", {"providers": providers})
    dump(ASSETS / "font" / "uno" / "dialog_selected.json", {"providers": selected_providers})
    # Review sheet deliberately lives outside runtime assets.
    sheet = Image.new("RGB", (9 * 96, 7 * 156), (45, 48, 54))
    draw = ImageDraw.Draw(sheet)
    for index, face in enumerate(faces):
        x, y = (index % 9) * 96 + 9, (index // 9) * 156 + 6
        sheet.paste(face.resize((78, 132), Image.Resampling.NEAREST), (x, y))
        draw.text((x, y + 136), asset_name(index), fill="white")
    sheet.paste(back.resize((78, 132), Image.Resampling.NEAREST), (9, 6 * 156 + 6))
    draw.text((9, 6 * 156 + 142), "back", fill="white")
    sheet.paste(box_front.resize((90, 144), Image.Resampling.NEAREST), (105, 6 * 156 + 6))
    draw.text((201, 6 * 156 + 12), "box", fill="white")
    sheet.paste(back_flipped.resize((78, 132), Image.Resampling.NEAREST), (297, 6 * 156 + 6))
    draw.text((297, 6 * 156 + 142), "back_flipped (UV)", fill="white")
    sheet.save(SOURCE / "contact-sheet.png")
    # Side-by-side review of the regular/selected dialog and HUD faces.
    preview = Image.new("RGB", (6 * 190, 174), (45, 48, 54))
    preview_draw = ImageDraw.Draw(preview)
    for column, index in enumerate([7, 24, 36, 48, 52, 53]):
        x = column * 190 + 8
        for offset, face in [(0, faces[index]), (88, selected_face(faces[index]))]:
            preview.paste(face.resize((78, 132), Image.Resampling.NEAREST), (x + offset, 8))
        preview_draw.text((x, 150), asset_name(index), fill="white")
    preview.save(SOURCE / "selection-preview.png")
    print(f"Exported 54 card faces, back, box, 56 item models, 54 regular/selected dialog glyphs to {PACK}")


if __name__ == "__main__":
    main()
