#version 330

#moj_import <minecraft:fog.glsl>
#moj_import <minecraft:dynamictransforms.glsl>
#moj_import <minecraft:projection.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV2;

uniform sampler2D Sampler2;

out float sphericalVertexDistance;
out float cylindricalVertexDistance;
out vec4 vertexColor;
out vec2 texCoord0;

void main() {
    // Detect the orthographic GUI projection before decoding panel coordinates.
    if (ProjMat[3][3] == 1.0) {
        // BetterTitle 26.1 把 X、Y 和锚点全部编码进文字顶点的 X 坐标。
        // 本版本保留 rendertype_text 入口，与相应版本的原版顶点接口一致。
        vec2 guiPixel = vec2(ProjMat[0][0], -ProjMat[1][1]);
        vec2 titlePos = vec2(1.0, 63.2 * guiPixel.y);
        vec2 origins[10] = vec2[10](
            titlePos,
            vec2(1.0, 2.0),
            vec2(1.0, 0.0),
            vec2(0.0, 1.0),
            vec2(2.0, 1.0),
            vec2(0.0, 2.0),
            vec2(2.0, 2.0),
            vec2(0.0, 0.0),
            vec2(2.0, 0.0),
            vec2(1.0, 1.0)
        );
    
        vec2 decodedPosition = Position.xy + vec2(750.0);
        int originIndex = int(mod(floor(decodedPosition.x / 1500.0), 10.0));
        decodedPosition.y -= 0.5 * floor(decodedPosition.x / 15000.0);
        decodedPosition.x = mod(decodedPosition.x, 1500.0);
        decodedPosition -= vec2(750.0);
    
        gl_Position = ProjMat * ModelViewMat * vec4(decodedPosition, Position.z, 1.0);
        gl_Position.xy += origins[originIndex] - titlePos;
    
        // 独立加载探针使用专用颜色 #12FEDC，不参与 BetterTitle 或花火正式面板。
        // 它只用于确认 core/text 的自定义 GUI 分支正在执行。
        bool isShaderProbe =
            Color.r > 0.06 && Color.r < 0.08 &&
            Color.g > 0.98 &&
            Color.b > 0.85 && Color.b < 0.88;
        if (isShaderProbe) {
            vec2 probePosition = vec2(mod(Position.x, 128.0), mod(Position.y, 16.0));
            gl_Position = vec4(
                -0.95 + probePosition.x * guiPixel.x,
                0.82 + probePosition.y * guiPixel.y,
                0.0,
                1.0
            );
        }
    } else {
        gl_Position = ProjMat * ModelViewMat * vec4(Position, 1.0);
    }

    sphericalVertexDistance = fog_spherical_distance(Position);
    cylindricalVertexDistance = fog_cylindrical_distance(Position);
    vertexColor = Color * texelFetch(Sampler2, UV2 / 16, 0);
    texCoord0 = UV0;
}
