import os

pdf_dir = "pdfs"
readme_path = "README.md"

pdf_files = sorted(os.listdir(pdf_dir))
table_rows = []

for pdf in pdf_files:
    if pdf.lower().endswith(".pdf"):
        title = os.path.splitext(pdf)[0].replace("_", " ").title()
        link = f"[Download PDF]({pdf_dir}/{pdf})"
        table_rows.append(f"| **{title}** | | {link} |")

table = "| Title | Description | Download Link |\n|-------|--------------|----------------|\n" + "\n".join(table_rows)

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace only the section between markers
start = content.find("## 📂 Available Review Materials")
end = content.find("## 🧭 How to Use")

if start != -1 and end != -1:
    new_content = (
        content[:start]
        + "## 📂 Available Review Materials\n\n"
        + table
        + "\n\n"
        + content[end:]
    )
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ README updated with new PDF list.")
else:
    print("⚠️ Could not find section markers. Please check README format.")
