
---

````markdown
# 📄 Adobe India Hackathon 2025 – Round 1A: Document Outline Extractor

## 🚀 Challenge Goal

Reimagine how PDFs are understood by extracting a structured outline with:

- 📌 **Title**
- 📂 **Headings** (H1, H2, H3) with page numbers

---

## 📁 Folder Structure

```text
ROUND1a/
├── app/
│   ├── __init__.py
│   ├── clustering.py
│   ├── extractor.py
│   ├── json_writer.py
│   ├── main.py
│   ├── utils.py
│   ├── input/
│   │   └── notes-50-100.pdf
│   └── output/
│       └── notes-50-100.json  ← (Generated after running)
├── Dockerfile
├── requirements.txt
└── README.md
````

---

## ⚙ How It Works

The script:

1. Loads all PDFs from `/app/app/input`
2. Extracts:

   * **Title** using font heuristics
   * **Headings (H1, H2, H3)** using position and font size clustering
3. Writes results to `/app/app/output` as a structured JSON

---

## 🐳 How to Run (Docker)

### 🔨 Build Docker Image

```bash
docker build --platform linux/amd64 -t pdf-outline:shreya .
```

### ▶ Run the Container

```bash
docker run --rm \
  -v "$(pwd)/app/input:/app/app/input" \
  -v "$(pwd)/app/output:/app/app/output" \
  --network none pdf-outline:shreya
```

> 📝 This will generate `.json` output in the `/app/output` directory.

---

## 🧠 Libraries Used

* `PyMuPDF` (`fitz`) – PDF parsing
* `os` – Directory handling
* `json` – Output generation
* `scikit-learn` – Clustering (if used in `clustering.py`)

---

## 📤 Output Format

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

## ❗ Constraints

* ⏱ ≤ 10 seconds for a 50-page PDF
* 📦 No internet access during execution
* 🖥 CPU-only; model size ≤ 200MB (if used)

---

```
```
