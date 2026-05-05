import re
import os
from bs4 import BeautifulSoup

def load_and_clean_docs(folder_path: str) -> list:
    documents = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'r', encoding='utf-8') as f:
            html_source = f.read()

        soup = BeautifulSoup(html_source, "html.parser")

        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator="\n")

        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'[ \t]+', ' ', text)

        start_match = re.search(r"\*\*\* START OF (THE|THIS) PROJECT GUTENBERG EBOOK.*\*\*\*", text, re.IGNORECASE)

        if start_match:
            text = text[start_match.end():]

        end_match = re.search(r"\*\*\* END OF (THE|THIS) PROJECT GUTENBERG EBOOK.*\*\*\*", text, re.IGNORECASE)

        if end_match:
            text = text[:end_match.start()]

        text = text.strip()
        document_name = os.path.splitext(file_name)[0]

        documents.append({
            'document': document_name,
            'text': text
        })

    return documents
