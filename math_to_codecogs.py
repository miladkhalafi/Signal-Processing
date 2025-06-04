import re
import urllib.parse
import requests

def formula_to_image_url(formula, display_mode=False):
    """
    Converts a LaTeX formula to an image URL using Codecogs.
    """
    formula_encoded = urllib.parse.quote(formula)
    mode = "block" if display_mode else "inline"
    url = f"https://latex.codecogs.com/svg.latex?{formula_encoded}"
    return url


def process_markdown_file(input_path, output_path):
    """
    Processes the markdown file and replaces all math formulas with image URLs.
    """
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Match $...$ (inline math) 
    inline_math_pattern = re.compile(r'\$(.*?)\$')
    
    # Match $$...$$ (display math)
    display_math_pattern = re.compile(r'\$\$(.*?)\$\$', re.DOTALL)

    def replace_inline(match):
        formula = match.group(1).strip()
        if not formula:
            return match.group(0)
        url = formula_to_image_url(formula, display_mode=False)
        return f"![Math](<{url}>)"

    def replace_display(match):
        formula = match.group(1).strip()
        if not formula:
            return match.group(0)
        url = formula_to_image_url(formula, display_mode=True)
        return f"\n\n![Math Formula](<{url}>)\n"

    # Replace inline formulas
    content = inline_math_pattern.sub(replace_inline, content)
    
    # Replace display formulas
    content = display_math_pattern.sub(replace_display, content)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"✅ Processed file saved to: {output_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python math_to_codecogs.py input.md output.md")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_markdown_file(input_file, output_file)