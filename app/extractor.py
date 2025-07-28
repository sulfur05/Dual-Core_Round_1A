# extractor.py
import fitz
import re
from collections import Counter
from clustering import cluster_font_sizes
from utils import clean_text

def is_heading_prefix(text):
    return bool(re.match(r"^\d+(\.\d+)*$", text.strip()))

def is_label(text):
    return bool(re.match(r"^[A-Z][A-Za-z\s\-]{2,40}$", text.strip()))

def is_junk_header(text):
    normalized = re.sub(r'[^A-Z0-9 ]', '', text.upper())
    normalized = re.sub(r'\s+', ' ', normalized).strip()
    return bool(re.match(r'^\d{1,3}\s+[A-Z]{4,}$', normalized))

def fix_spacing(text):
    return re.sub(r'(?<=\b)([A-Z])(?:\s)(?=[A-Z])', r'\1', text)

def extract_headings(doc):
    line_items = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                if not spans:
                    continue

                text = " ".join(clean_text(s["text"]) for s in spans if s["text"].strip())
                text = fix_spacing(text.strip())
                if not text or len(text) < 2:
                    continue

                font_sizes = [s["size"] for s in spans]
                avg_font = sum(font_sizes) / len(font_sizes)

                line_items.append({
                    "text": text,
                    "font_size": round(avg_font, 2),
                    "page": page_num  # ← changed to 0-based index
                })

    text_counts = Counter(item["text"] for item in line_items)
    repeat_threshold = max(2, int(0.3 * len(doc)))

    if not line_items:
        return "Untitled", []

    font_size_to_level = cluster_font_sizes(line_items)

    title_candidates = [item for item in line_items if item["page"] <= 1]  # 0,1 pages
    title_line = max(title_candidates, key=lambda x: x["font_size"], default=None)
    title = title_line["text"] if title_line else "Untitled"

    pre_outline = []
    for item in line_items:
        if is_junk_header(item["text"]) or text_counts[item["text"]] >= repeat_threshold:
            continue
        level = font_size_to_level.get(item["font_size"])
        pre_outline.append({
            "level": level if level else "UNKNOWN",
            "text": item["text"],
            "page": item["page"]
        })

    final_outline = []
    i = 0
    while i < len(pre_outline):
        current = pre_outline[i]
        next_item = pre_outline[i + 1] if i + 1 < len(pre_outline) else None

        if (
            next_item
            and current["page"] == next_item["page"]
            and is_heading_prefix(current["text"])
            and is_label(next_item["text"])
        ):
            final_outline.append({
                "level": current["level"] if current["level"] != "UNKNOWN" else "H2",
                "text": f"{current['text']} {next_item['text']}",
                "page": current["page"]
            })
            i += 2
        elif current["level"] in {"H1", "H2", "H3"}:
            final_outline.append(current)
            i += 1
        else:
            i += 1

    return title, final_outline
