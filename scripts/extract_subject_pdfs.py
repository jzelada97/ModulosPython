from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
print(f"Workspace root: {ROOT}")

count = 0
for pdf in ROOT.rglob("en.subject*.pdf"):
    out = pdf.with_suffix('.txt')
    try:
        reader = PdfReader(str(pdf))
        text_parts = []
        for p in reader.pages:
            t = p.extract_text()
            if t:
                text_parts.append(t)
        text = "\n\n".join(text_parts)
        out.write_text(text, encoding='utf-8')
        print(f"Wrote: {out}")
        count += 1
    except Exception as e:
        print(f"Failed to extract {pdf}: {e}")

print(f"Done. Extracted {count} PDFs.")
