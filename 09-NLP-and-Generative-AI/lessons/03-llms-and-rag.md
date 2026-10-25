# NLP, LLMs, Embeddings, and RAG

## NLP and tokenization
Natural Language Processing handles text tasks such as classification, extraction, summarization, translation, and question answering. A tokenizer converts text into tokens; tokens are not always whole words.

## Transformers and LLMs
Transformers use attention to combine contextual information. Large language models generate token sequences based on learned patterns and the provided context. They can produce incorrect or fabricated claims, so important outputs need verification.

## Embeddings and vector search
An embedding maps text to a numeric vector so semantically related text may be close in vector space. Retrieval systems search for relevant chunks using similarity and sometimes metadata filters. Similarity is a ranking signal, not proof of truth.

## Retrieval-Augmented Generation (RAG)
1. Load permitted documents.
2. Extract and normalize text.
3. Split text into chunks while preserving useful context.
4. Embed chunks and store vectors with source metadata.
5. Retrieve relevant chunks for a question.
6. Generate an answer grounded in retrieved context.
7. Cite sources and evaluate retrieval and answer quality.

## RAG risks and safeguards
Watch for bad chunking, stale documents, poor retrieval, prompt injection inside retrieved documents, privacy leaks, unsupported answers, and missing citations. Treat document content as untrusted data, separate instructions from evidence, restrict tools, and test adversarial cases.

## Evaluation
Evaluate retrieval recall/precision, groundedness, citation correctness, answer usefulness, latency, and cost. Use a fixed evaluation set and human review for high-impact tasks.
