
```
# 📄 Adobe India Hackathon 2025 – Round 1A: Document Outline Extractor

---

## ✅ Approach

The solution extracts a structured outline from PDFs by analyzing each page’s layout and text organization. It identifies the document’s title and classifies headings into hierarchical levels (H1, H2, H3) using content patterns and structural cues. Repetitive or non-informative elements are filtered out to ensure the output remains clean and relevant.

This process is designed to generalize across different document types and styles without relying on hardcoded rules, producing a consistent and readable outline in JSON format.

---

## 🧠 Libraries Used

- PyMuPDF (fitz) – for PDF parsing and layout extraction
- scikit-learn – used internally for grouping logic
- re – for pattern-based filtering and cleanup
- os, json – for file I/O and output formatting

All dependencies are listed in requirements.txt and are installed inside the Docker container.

---

## 🐳 How to Build and Run (Documentation Purpose)

These commands are for documentation purposes only. The solution will be evaluated using the official execution commands provided in the challenge.

### Build the Docker Image

```bash
docker build --platform linux/amd64 -t dualcore:extractor1a .
````

### Run the Docker Container

Using PowerShell (Windows):

```powershell
docker run --rm `
  -v "${PWD}\input:/app/input" `
  -v "${PWD}\output:/app/output" `
  --network none `
  dualcore:extractor1a
```

Using Bash (Linux/macOS):

```bash
docker run --rm \
  -v "$(pwd)/input:/app/input" \
  -v "$(pwd)/output:/app/output" \
  --network none \
  dualcore:extractor1a
```

Each PDF in /app/input will be processed, and a corresponding JSON file will be generated in /app/output.

---

```

Let me know if you'd like this saved to a file or bundled in a ZIP with your code. You're now fully ready for submission ✅.
```
