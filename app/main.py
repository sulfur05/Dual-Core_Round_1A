import os
import fitz  # PyMuPDF
from extractor import extract_headings
from json_writer import save_json


INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf(file_path, output_path):
    doc = fitz.open(file_path)
    title, outline = extract_headings(doc)
    output_data = {
        "title": title,
        "outline": outline
    }
    save_json(output_data, output_path)

def main():
    if not os.path.exists(INPUT_DIR):
        raise FileNotFoundError(f"Input directory not found: {INPUT_DIR}")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            print(f"Processing: {filename}")
            process_pdf(input_path, output_path)
            print(f"Saved: {output_filename}")

if __name__ == "__main__":
    main()