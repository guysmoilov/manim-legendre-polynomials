#!/bin/bash
# Render all scenes at 720p/30fps and concatenate into one video
set -e

export PATH="/Library/TeX/texbin:/opt/homebrew/Cellar/ffmpeg/8.0.1_1/bin:$PATH"

OUTPUT="legendre_polynomials.mp4"
QUALITY="--resolution 1280,720 --fps 30"
SCENE_DIR="media/videos/legendre/720p30"

SCENES=(
    S01_PowerOfPerpendicular
    S02_FunctionsAsVectors
    S03_GramSchmidt
    S04_OrthogonalityGrid
    S05_FunctionApproximation
    S06_ClosingCard
)

echo "=== Rendering ${#SCENES[@]} scenes at 720p/30fps ==="

for scene in "${SCENES[@]}"; do
    echo "--- Rendering $scene ---"
    uv run manim render $QUALITY legendre.py "$scene"
done

echo "=== Concatenating with ffmpeg ==="

# Build concat file list with absolute paths
CONCAT_FILE=$(mktemp /tmp/manim_concat_XXXX.txt)
for scene in "${SCENES[@]}"; do
    echo "file '$(pwd)/${SCENE_DIR}/${scene}.mp4'" >> "$CONCAT_FILE"
done

cat "$CONCAT_FILE"
ffmpeg -y -f concat -safe 0 -i "$CONCAT_FILE" -c copy "$OUTPUT"
rm "$CONCAT_FILE"

echo "=== Done: $OUTPUT ==="
