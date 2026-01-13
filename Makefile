.PHONY: all clean

PROMPT_FILE := 翻译.md
BUILD_SCRIPT := build.py
TARGET_FILE := ai_script.bash

all: $(TARGET_FILE)

$(TARGET_FILE): $(PROMPT_FILE) $(BUILD_SCRIPT)
	@uv run build.py $(TARGET_FILE)

clean:
	rm -f $(TARGET_FILE)
