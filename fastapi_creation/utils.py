from pathlib import Path

def create_structure(base_path: Path, structure: dict):
    """
    ساختار دیکشنری را به فولدر و فایل در base_path تبدیل می‌کند.
    """
    for name, content in structure.items():
        path = base_path / name
        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)  # بازگشتی
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
