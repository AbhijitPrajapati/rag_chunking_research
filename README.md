# RAG Chunking
A multitude of components come together to form an effective retrieval-augmented generation system, including embedding models, vector stores, and large language models. Although the process of generation commonly receives the utmost attention, its results depend entirely on correct preprocessing and storage techniques, making each module of a RAG system not supplemental, but critical for performance. This repository contins the experimental evaluation of various methods of chunking, a process that is foundational to RAG success. Additionally, it presents a thorough examination of the effects of chunking with respect to retrieval accuracy and generative efficacy.

## Results
Each of the following chunking strategies were tested:
- Fixed-length chunking
- Sentence-based chunking
- Semantic chunking

A combination of metrics screening for robust retrieval and high-quality responses were employed in order to analyze the reliability of proxy metrics. As discussed in the report, it was shown that precise retrieval does not necessarily correlate with a greater accuracy or clarity in the generated result. 

## Tools
ChromaDB was utilized as a lightweight vector store for all generated chunks. The LLM for generation was run locally alongside embedding models on an NVIDIA RTX 4070. The evaluation model was provided by the Groq API, as a larger model was desired to facilitate accurate evaluation.

## Repo Structure
- `report.pdf` — full report of findings
- `chunks/` — created when papers are chunked
- `data/` — raw papers, processed papers, and evaluation prompts
- `figures/` — plots used in the report to illustrate findings
- `results/` — raw results from each step of the evaluation process
- `src/chunking` — implementations for each chunking method
- `src/groq` — LLM for evaluation using Groq
- `src/metrics` — implementations of key metrics
- `src/nlp` — embedding model and LLM for generation, run locally
- `src/scripts` — scripts to carry out the experiments
- `src/vector_store` — vector store functionality
