# Makefile for Legendre Polynomials video
# Usage:
#   make           - Build the full video (only re-renders changed scenes)
#   make -j4       - Build with 4 parallel jobs
#   make clean     - Remove generated video files
#   make scene3    - Render just Scene 3 (S03_GramSchmidt)

# Configuration
SHELL := /bin/bash
export PATH := /Library/TeX/texbin:/opt/homebrew/Cellar/ffmpeg/8.0.1_1/bin:$(PATH)

OUTPUT := legendre_polynomials.mp4
QUALITY := --resolution 1280,720 --fps 30
SCENE_DIR := media/videos/legendre/720p30
SOURCE := legendre.py

# Scene list
SCENES := S01_PowerOfPerpendicular \
          S02_FunctionsAsVectors \
          S03_GramSchmidt \
          S04_OrthogonalityGrid \
          S05_FunctionApproximation \
          S06_ClosingCard

# Generate scene file paths
SCENE_FILES := $(patsubst %,$(SCENE_DIR)/%.mp4,$(SCENES))

# Default target
.PHONY: all
all: $(OUTPUT)

# Final concatenated video depends on all scene files
$(OUTPUT): $(SCENE_FILES)
	@echo "=== Concatenating $(words $(SCENE_FILES)) scenes with ffmpeg ==="
	@CONCAT_FILE=$$(mktemp /tmp/manim_concat_XXXX.txt); \
	for scene in $(SCENES); do \
		echo "file '$$(pwd)/$(SCENE_DIR)/$${scene}.mp4'" >> "$$CONCAT_FILE"; \
	done; \
	cat "$$CONCAT_FILE"; \
	ffmpeg -y -f concat -safe 0 -i "$$CONCAT_FILE" -c copy "$(OUTPUT)"; \
	rm "$$CONCAT_FILE"
	@echo "=== Done: $(OUTPUT) ==="

# Pattern rule for rendering individual scenes
$(SCENE_DIR)/%.mp4: $(SOURCE)
	@echo "--- Rendering $* ---"
	@mkdir -p $(SCENE_DIR)
	uv run manim render $(QUALITY) $(SOURCE) "$*"

# Convenience targets for individual scenes
.PHONY: scene1 scene2 scene3 scene4 scene5 scene6
scene1: $(SCENE_DIR)/S01_PowerOfPerpendicular.mp4
scene2: $(SCENE_DIR)/S02_FunctionsAsVectors.mp4
scene3: $(SCENE_DIR)/S03_GramSchmidt.mp4
scene4: $(SCENE_DIR)/S04_OrthogonalityGrid.mp4
scene5: $(SCENE_DIR)/S05_FunctionApproximation.mp4
scene6: $(SCENE_DIR)/S06_ClosingCard.mp4

# Clean up generated files
.PHONY: clean
clean:
	rm -f $(OUTPUT)
	rm -rf media/

# Show what would be built
.PHONY: status
status:
	@echo "Source: $(SOURCE)"
	@echo "Output: $(OUTPUT)"
	@echo "Scenes:"
	@for scene in $(SCENE_FILES); do \
		if [ -f "$$scene" ]; then \
			echo "  ✓ $$scene (exists)"; \
		else \
			echo "  ✗ $$scene (needs rendering)"; \
		fi \
	done

.PHONY: help
help:
	@echo "Legendre Polynomials Video Build System"
	@echo ""
	@echo "Targets:"
	@echo "  make           - Build full video (only re-renders if legendre.py changed)"
	@echo "  make -j4       - Build with 4 parallel jobs"
	@echo "  make scene3    - Render just Scene 3 (S03_GramSchmidt)"
	@echo "  make status    - Show which scenes need rendering"
	@echo "  make clean     - Remove all generated videos"
	@echo "  make help      - Show this message"
