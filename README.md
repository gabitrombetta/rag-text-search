# Pipeline de Busca Semântica (inspirado em RAG)
Projeto desenvolvido como entrega final do Bootcamp do Fellowship da [AI/R Compass UOL](https://aircompany.ai/en/about-us/). Este projeto implementa um sistema de busca semântica capaz de recuperar trechos relevantes de textos com base no significado da consulta, e não apenas em correspondência de palavras-chave.

O pipeline inclui:

- Limpeza de dados HTML
- Segmentação de texto (*chunking*)
- Geração de embeddings
- Busca por similaridade vetorial

## 🚀 Funcionalidades

- Extração e limpeza de texto com BeautifulSoup
- Divisão de documentos em chunks
- Geração de embeddings com modelos pré-treinados
- Normalização vetorial
- Busca semântica com cosine similarity
- Retorno dos trechos mais relevantes

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/gabitrombetta/rag-text-search.git
cd rag-text-search
```

### 2. Crie um ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o projeto
```bash
python scripts/run_search.py
```
#### ⚠️ Sobre a execução

Este projeto depende de dados que não estão incluídos no repositório.

## 📊 Exemplo de uso
```
Query: In The Great Gatsby, who hosts the parties at the Gatsby mansion?

Top 1
Documento: the_great_gatsby
Score: 0.87
Texto:
In his blue gardens men and girls came and went like moths among the whisperings...
```
## 🧠 Tecnologias utilizadas
- Python
- NumPy
- Scikit-learn
- BeautifulSoup
- LangChain
- Sentence Transformers

## 👩🏻‍💻 Gabriela Trombetta
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabitrombetta/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gabitrombetta)