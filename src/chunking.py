from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

def chunking(documents: list, chunk_size=800, chunk_overlap=100) -> list:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    chunks = []

    for doc in documents:
        split_texts = text_splitter.split_text(doc['text'])

        for i, chunk in enumerate(split_texts):
            chunks.append({
                'id': f"{doc['document']}_chunk_{i}",
                'text': chunk,
                'document': doc['document']
            })

    return chunks