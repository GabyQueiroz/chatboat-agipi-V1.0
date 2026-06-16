import re
from pathlib import Path
import pymupdf4llm as mu

def normalize_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"==>\s*picture.*?<==", " ", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"-{3,}\s*Start of picture text\s*-{3,}", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"-{3,}\s*End of picture text\s*-{3,}", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\b[pP]icture\b", " ", text)

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = text.strip()

    return text

def pdf_to_md(pdf_path: str, md_path: str) -> None:
    text = mu.to_markdown(pdf_path)
    with open(md_path, "w", encoding="utf-8") as f:
        text = normalize_text(text)
        f.write(text)

raw_dir = Path('data/raw')
MD_PATH = Path('data/md')
MD_PATH.mkdir(parents=True, exist_ok=True)

# for path in sorted(raw_dir.glob("*.pdf")):
for path in sorted(raw_dir.rglob("*.pdf")):
    if not path.is_file():
        continue
    md_path = MD_PATH / path.relative_to(raw_dir).with_suffix(".md")
    md_path.parent.mkdir(parents=True, exist_ok=True)

    print(str(md_path))

    if md_path.exists():
        continue

    pdf_to_md(str(path), str(md_path))