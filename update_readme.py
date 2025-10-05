import os

# Look for PDFs in the main directory (same folder as this script)
pdf_dir = os.getcwd()
readme_path = os.path.join(pdf_dir, "README.md")

# Get all PDF files in the current directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]
pdf_files.sort()

if not pdf_files:
    print("⚠️ No PDF files found in the main directory.")
    exit()

# Build markdown table rows
rows = []
for pdf in pdf_files:
    title = os.path.splitext(pdf)[0].replace("_", " ").title()
    link = f"[Download PDF]({pdf})"
    rows.append(f"| **{title}** | | {link} |")

table_header = "| Title | Description | Download Link |\n|-------|--------------|----------------|\n"
table = table_header + "\n".join(rows) + "\n"

# Read the README content
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Identify section markers
start_marker = "## 📂 Available Review Materials"
end_marker = "## 🧭 How to Use"

start = content.find(start_marker)
end = content.find(end_marker)

if start != -1 and end != -1:
    before = content[:start + len(start_marker)] + "\n\n"
    after = content[end:]
    new_content = before + table + "\n" + after

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ README updated successfully with all PDFs from main directory.")
else:
    print("⚠️ Could not locate section markers. Please check README format.")
