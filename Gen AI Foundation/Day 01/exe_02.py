"""Exercise 2: Calling LLM via API
Objective:
Learn how to interact with an LLM using an API endpoint and process responses.

Problem Statement:
Extend the given Python API script to:
1. Accept dynamic user input
2. Send it to the LLM endpoint
3. Extract and print full JSON response and assistant reply
4. Modify parameters like temperature and prompts

Additional Challenge:
- Add a second query and compare responses
- Handle API errors gracefully

Key Tasks:
- Use requests.post() with headers
- Parse response.json()
- Extract assistant reply from response

Bonus Exercise (Optional):
Combine both exercises:
- Generate embeddings for multiple prompts
- Select the most similar prompt
- Send only the best-matching query to the LLM"""

import requests
import json
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
API_KEY = os.getenv('ANTHROPIC_API_KEY')
BASE_URL = os.getenv('BASE_URL', 'https://api.anthropic.com/v1')

def call_llm(user_input, temperature=0.7, max_tokens=1024):
    """
    Call Claude LLM via API endpoint with error handling.
    Returns full response JSON and extracted assistant message.
    """
    url = f"{BASE_URL.rstrip('/')}/v1/messages"

    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": "global.anthropic.claude-haiku-4-5-20251001-v1:0",
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        response_json = response.json()

        assistant_reply = response_json['content'][0]['text']

        return response_json, assistant_reply

    except requests.exceptions.Timeout:
        print("ERROR: Request timed out (30 seconds)")
        return None, None
    except requests.exceptions.HTTPError as e:
        print(f"ERROR: HTTP {response.status_code} - {response.text}")
        return None, None
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Request failed - {str(e)}")
        return None, None
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"ERROR: Failed to parse response - {str(e)}")
        return None, None

def find_best_matching_prompt(user_prompts):
    """
    Generate embeddings for multiple prompts and find the most similar pair.
    Returns the index of the best matching prompt to use.
    """
    print("\n" + "=" * 70)
    print("BONUS: EMBEDDING ANALYSIS FOR PROMPT SELECTION")
    print("=" * 70)

    print(f"\nLoading Sentence Transformer model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✓ Model loaded successfully\n")

    print("Input Prompts:")
    for i, prompt in enumerate(user_prompts, 1):
        print(f"  {i}. {prompt[:60]}..." if len(prompt) > 60 else f"  {i}. {prompt}")

    embeddings = model.encode(user_prompts)
    similarity_matrix = cosine_similarity(embeddings)

    print("\nSimilarity Matrix:")
    header = "         " + "".join(f"Prompt{i}  " for i in range(1, len(user_prompts) + 1))
    print(header)
    print("-" * len(header))

    for i, row in enumerate(similarity_matrix, 1):
        row_str = f"Prompt {i}: "
        for score in row:
            row_str += f"{score:.3f}   "
        print(row_str)

    max_similarity = -1
    best_prompt_idx = 0

    for i in range(len(similarity_matrix)):
        for j in range(i + 1, len(similarity_matrix)):
            if similarity_matrix[i][j] > max_similarity:
                max_similarity = similarity_matrix[i][j]
                best_prompt_idx = i

    print(f"\n✓ Best matching prompt: Prompt {best_prompt_idx + 1}")
    print(f"  (Highest semantic relevance identified)\n")

    return best_prompt_idx

def main():
    print("\n" + "=" * 70)
    print("LLM API INTERACTION WITH PROMPT OPTIMIZATION")
    print("=" * 70)

    user_prompts = [
        "Explain what machine learning is in simple terms",
        "What is artificial intelligence and its applications?",
        "Tell me about your favorite food"
    ]

    best_idx = find_best_matching_prompt(user_prompts)

    print("=" * 70)
    print("QUERY 1: BASIC REQUEST (Temperature = 0.7)")
    print("=" * 70)

    query_1 = user_prompts[0]
    print(f"\nQuery: {query_1}")
    print("-" * 70)

    response_json_1, assistant_reply_1 = call_llm(query_1, temperature=0.7)

    if response_json_1 and assistant_reply_1:
        print("\n✓ Full JSON Response:")
        print(json.dumps(response_json_1, indent=2))

        print("\n" + "-" * 70)
        print("Assistant Reply:")
        print("-" * 70)
        print(assistant_reply_1)
    else:
        print("Failed to get response for Query 1")

    print("\n" + "=" * 70)
    print("QUERY 2: COMPARATIVE REQUEST (Temperature = 0.2 - More Deterministic)")
    print("=" * 70)

    query_2 = user_prompts[1]
    print(f"\nQuery: {query_2}")
    print("-" * 70)

    response_json_2, assistant_reply_2 = call_llm(query_2, temperature=0.2)

    if response_json_2 and assistant_reply_2:
        print("\n✓ Full JSON Response:")
        print(json.dumps(response_json_2, indent=2))

        print("\n" + "-" * 70)
        print("Assistant Reply:")
        print("-" * 70)
        print(assistant_reply_2)
    else:
        print("Failed to get response for Query 2")

    if response_json_1 and response_json_2 and assistant_reply_1 and assistant_reply_2:
        print("\n" + "=" * 70)
        print("RESPONSE COMPARISON")
        print("=" * 70)

        print(f"\nQuery 1 Token Usage: {response_json_1['usage']['input_tokens']} input, {response_json_1['usage']['output_tokens']} output")
        print(f"Query 2 Token Usage: {response_json_2['usage']['input_tokens']} input, {response_json_2['usage']['output_tokens']} output")

        print(f"\nReply 1 Length: {len(assistant_reply_1)} characters")
        print(f"Reply 2 Length: {len(assistant_reply_2)} characters")

        print("\nObservation:")
        print("- Query 1 (temp=0.7): More creative and varied responses")
        print("- Query 2 (temp=0.2): More focused and deterministic responses")

    print("\n" + "=" * 70)
    print("BONUS: TESTING WITH BEST MATCHING PROMPT")
    print("=" * 70)

    best_query = user_prompts[best_idx]
    print(f"\nSending best-matching prompt: {best_query}")
    print("-" * 70)

    response_json_best, assistant_reply_best = call_llm(best_query, temperature=0.5)

    if response_json_best and assistant_reply_best:
        print("\n✓ Response from best-matching prompt:")
        print(assistant_reply_best[:500] + "..." if len(assistant_reply_best) > 500 else assistant_reply_best)
    else:
        print("Failed to get response for best-matching prompt")

if __name__ == "__main__":
    main()
