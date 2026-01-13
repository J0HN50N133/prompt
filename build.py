from sys import argv
import textwrap


def embed_text_to_var(name, text):
    return f"""\
read -r -d '' {name} << 'EOF'
{text}
EOF\
"""


def generate_script(translate_prompt_file_path: str) -> str:
    with open(translate_prompt_file_path, "r") as f:
        translate_prompt = f.read().rstrip()
    return textwrap.dedent(f"""
        {embed_text_to_var(name="TRANSLATE_PROMPT", text=translate_prompt)}

        trans() {{
            ai --prompt $TRANSLATE_PROMPT "input=$*"
        }}
    """).strip()


def main() -> None:
    output_file = argv[1]
    s = generate_script(translate_prompt_file_path="翻译.md")
    with open(output_file, "w") as f:
        f.write(s)


if __name__ == "__main__":
    main()
