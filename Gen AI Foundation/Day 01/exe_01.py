"""Exercise 1: Text Embeddings & Similarity Comparison
Objective:
Understand how to generate embeddings using Sentence Transformers and compute similarity between sentences.

Problem Statement:
Create a Python script that:
1. Uses a Sentence Transformer model
2. Converts 3–5 input sentences into embeddings
3. Calculates cosine similarity between each pair
4. Prints the first 5 dimensions of each embedding and a similarity score matrix

Sample Inputs:
- "GenAI is transforming software development"
- "Artificial Intelligence is changing how developers work"
- "I love playing cricket on weekends"

Key Tasks:
- Load model: all-MiniLM-L6-v2
- Use cosine_similarity from sklearn
- Display similarity in readable format

Expected Learning Outcome:
- Understand embeddings as vector representations
- Interpret similarity scores (semantic closeness) """

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def main():
    sentences = [
        "GenAI is transforming software development",
        "Artificial Intelligence is changing how developers work",
        "I love playing cricket on weekends"
    ]

    print("=" * 70)
    print("TEXT EMBEDDINGS & SIMILARITY COMPARISON")
    print("=" * 70)

    print("\nLoading Sentence Transformer model: all-MiniLM-L6-v2...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✓ Model loaded successfully\n")

    print("Input Sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"  {i}. {sentence}")

    print("\n" + "-" * 70)
    print("GENERATING EMBEDDINGS")
    print("-" * 70)

    embeddings = model.encode(sentences)

    print(f"\nEmbedding Dimensions: {embeddings.shape[1]}")
    print("\nFirst 5 Dimensions of Each Embedding:")
    for i, (sentence, embedding) in enumerate(zip(sentences, embeddings), 1):
        first_5 = embedding[:5]
        print(f"\nSentence {i}: {sentence}")
        print(f"  First 5 dims: {first_5}")

    print("\n" + "-" * 70)
    print("COSINE SIMILARITY MATRIX")
    print("-" * 70)

    similarity_matrix = cosine_similarity(embeddings)

    print("\nSimilarity Scores (0 = dissimilar, 1 = identical):\n")

    header = "         " + "".join(f"Sent{i}   " for i in range(1, len(sentences) + 1))
    print(header)
    print("-" * len(header))

    for i, row in enumerate(similarity_matrix, 1):
        row_str = f"Sent {i}:  "
        for score in row:
            row_str += f"{score:.3f}  "
        print(row_str)

    print("\n" + "=" * 70)
    print("INTERPRETATION")
    print("=" * 70)
    print("• Sentence 1 & 2: Both about AI/GenAI transforming development (high similarity)")
    print("• Sentence 1 & 3: Different topics - AI development vs playing cricket (low similarity)")
    print("• Sentence 2 & 3: Different topics - AI development vs playing cricket (low similarity)")
    print("=" * 70)

if __name__ == "__main__":
    main()