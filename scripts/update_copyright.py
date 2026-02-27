import re
from pathlib import Path
from datetime import datetime

def update_copyright_notice_in_notebooks(notebooks_path: Path) -> None:
    """
    Update the copyright notice in all Jupyter notebooks within the given path.

    Args:
    notebooks_path (Path): The path to the directory containing notebook files.
    """
    current_year = datetime.now().year
    copyright_pattern = re.compile(
        r'\[Creative Commons Attribution-NonCommercial-ShareAlike 4\.0 International \(CC BY-NC-SA 4\.0\)\]\(https://creativecommons\.org/licenses/by-nc-sa/4\.0/\)\. Copyright © 2018-\d{4} \[Point 8 GmbH\]\(https://point-8\.de\)'
    )

    for notebook_file in notebooks_path.rglob('*.ipynb'):
        with notebook_file.open('r', encoding='utf-8') as file:
            content = file.read()

        updated_content = copyright_pattern.sub(
            f"[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Copyright © 2018-{current_year} [Point 8 GmbH](https://point-8.de)",
            content
        )

        with notebook_file.open('w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Updated copyright notice in: {notebook_file}")

if __name__ == "__main__":
    notebooks_dir = Path('notebooks')
    update_copyright_notice_in_notebooks(notebooks_dir)