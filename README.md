# 📄 Adobe India Hackathon 2025 – Round 1A: Document Outline Extractor

---

## 🧠 Challenge Theme: *Connecting the Dots Through Docs*

Welcome to the “Connecting the Dots” Challenge!

> **Rethink Reading. Rediscover Knowledge.**  
> Your mission is to turn static PDFs into intelligent, interactive experiences.  
> In **Round 1A**, we focus on understanding structure — the foundation of all semantic tasks.

---

## 🚀 Round 1A Goal

You're handed a PDF — but instead of simply reading it, you're tasked with making sense of it like a machine would. Your job is to extract a structured outline of the document including:

- 📌 **Title**
- 📂 **Headings** – H1, H2, H3 with page numbers

This forms the **semantic foundation** for future rounds like recommendation and insight generation.

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
```

---

## ⚙ How It Works

The pipeline performs the following:

1. **Loads PDFs** from `/app/input`
2. **Extracts:**
   - 📌 Title using font heuristics
   - 📂 Headings (H1/H2/H3) using font size, layout, and position clustering
3. **Writes structured output** to `/app/output` in valid JSON format

---

## 🐳 How to Run with Docker

### 🔨 Build the Docker Image

```bash
docker build --platform linux/amd64 -t dualcore:extractor1a .
```

### ▶ Run the Container

#### If using **PowerShell** (Windows):
```powershell
docker run --rm `
  -v "${PWD}\input:/app/input" `
  -v "${PWD}\output:/app/output" `
  --network none `
  dualcore:extractor1a
```

#### If using **bash** (Linux/macOS/Git Bash):
```bash
docker run --rm \
  -v "$(pwd)/input:/app/input" \
  -v "$(pwd)/output:/app/output" \
  --network none \
  dualcore:extractor1a
```

> 📝 All PDFs in `/app/input` will be processed and corresponding `.json` files generated in `/app/output`.

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

## 📦 Libraries & Tools Used

- `PyMuPDF (fitz)` – PDF parsing
- `os` & `json` – Filesystem and serialization
- `scikit-learn` – Clustering logic for heading detection

---

## ✅ What You Need to Build

Your container must:

- Accept a **PDF file up to 50 pages**
- Extract:
  - `title`
  - Headings `H1`, `H2`, `H3` (with level and page number)
- Output a **valid JSON file** per input file

---

## ❗ Constraints

| Constraint            | Requirement                             |
|-----------------------|------------------------------------------|
| Execution time        | ⏱ ≤ 10 seconds for a 50-page PDF         |
| Model size            | 📦 ≤ 200MB (if used)                      |
| Network               | 🚫 No internet access allowed             |
| Platform              | 🖥 Must run on CPU (amd64 architecture)   |

---

## 🧪 Evaluation Criteria

| Metric                             | Max Points |
|------------------------------------|------------|
| Heading Detection Accuracy         | 25         |
| Performance (Time & Size)          | 10         |
| Bonus: Multilingual Handling       | 10         |
| **Total**                          | **45**     |

---

## 📌 Submission Checklist

✔ Working **Dockerfile** in root directory  
✔ All dependencies installed inside container  
✔ **README.md** that includes:
- 📘 Approach overview
- 🧠 Models/Libraries used
- 🐳 How to build and run the solution

> ✅ **Pro Tip**: Avoid hardcoding or API calls. Generalize the logic. Keep the repo private until told otherwise.

---

## 💡 Pro Tips

- Don’t rely **only** on font size for heading levels — use position and spacing too!
- Test on **both simple and complex** PDFs
- Make your code **modular** — reuse it in Round 1B
- Avoid hardcoding text or file-specific rules

---
---
