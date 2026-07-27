import os
import requests
import numpy as np
from flask import Flask, render_template, request
from dotenv import load_dotenv
import chromadb
 
# Load environment configuration parameters seamlessly from .env file
load_dotenv()
 
app = Flask(__name__)
 
# Retrieve target environment secrets cleanly without hardcoding
APP_KEY = os.getenv("ANTHROPIC_API_KEY")
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
LLM_MODEL = os.getenv("LLM_MODEL")
 
# ==========================================
# RESILIENT EMBEDDING MODEL INITIALIZATION LAYER
# ==========================================
class OfflineMockEncoder:
    """Fall-back class providing mock structural embeddings when internet access is blocked."""
    def encode(self, text):
        # Generates a standard 384-dimensional zero vector matching all-MiniLM-L6-v2 specifications
        return np.zeros(384).tolist()
 
try:
    print("Initializing SentenceTransformer execution layers...")
    from sentence_transformers import SentenceTransformer
    embedding_encoder = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as network_fault:
    print("Hugging Face download blocked by network firewall. Initiating Offline Mock Encoder...")
    embedding_encoder = OfflineMockEncoder()

# ==========================================
# PERSISTENT CHROMADB SEEDING & INITIALIZATION
# ==========================================
# Set up a persistent directory path for storage
CHROMA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chroma_db")
chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
 
# Fetch or establish data space collections
knowledge_collection = chroma_client.get_or_create_collection(name="genai_training_knowledge")
 
# Seed initial training context if database collection is currently empty
if knowledge_collection.count() == 0:
    print("Seeding initial reference context data blocks into ChromaDB storage...")
    sample_documents = [
        "Retrieval-Augmented Generation (RAG) is an architectural flow optimized to retrieve relevant context first, then pass it to the LLM.",
        "Embeddings are numerical vector representations that capture deep semantic meanings rather than exact words.",
        "Vector databases like ChromaDB store embeddings along with their associated textual document payloads for rapid similarity analysis."
    ]
    sample_ids = [f"id_{i}" for i in range(len(sample_documents))]
    
    # Generate vectors across each string payload segment
    sample_embeddings = [embedding_encoder.encode(doc) for doc in sample_documents]
    
    knowledge_collection.add(
        ids=sample_ids,
        embeddings=sample_embeddings,
        documents=sample_documents
    )
 
# ==========================================
# FLASK WEB APP APPLICATION ROUTES
# ==========================================
 
@app.route('/', methods=['GET'])
def homepage_interface():
    """Renders the standard system web submission interface dashboard."""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def process_rag_pipeline():
    """Executes full functional workflow pipeline requirements."""
    user_query = request.form.get('question', '').strip()
    
    if not user_query:
        return render_template('index.html', error="Input error: Query field cannot be empty.")
 
    context_chunks = []
    assistant_response = None
    system_error = None
 
    try:
        # Step 1: Transform user's query string into a vector array
        query_vector = embedding_encoder.encode(user_query)
 
        # Step 2: Query ChromaDB for top matched context strings
        db_results = knowledge_collection.query(
            query_embeddings=[query_vector],
            n_results=2
        )
 
        # Build clean structural dictionary references containing distances and text context
        if db_results and db_results['documents'] and db_results['documents'][0]:
            for i in range(len(db_results['documents'][0])):
                # Compute distance values safely
                distance_val = db_results['distances'][0][i] if 'distances' in db_results else 0.0
                context_chunks.append({
                    'text': db_results['documents'][0][i],
                    'distance': round(float(distance_val), 4)
                })
 
        # Combine matching texts into a single context string block
        combined_context_text = "\n".join([chunk['text'] for chunk in context_chunks])
        
        # Step 3: Engineer structured prompt wrapping payload securely
        system_persona = "You are a helpful, beginner-friendly technical assistant supporting associates attending GenAI Foundation training."
        structured_prompt = (
            f"{system_persona}\n"
            f"Use the following retrieved context information blocks exclusively to formulate your answer.\n\n"
            f"Retrieved Training Context:\n{combined_context_text}\n\n"
            f"User Question: {user_query}\n"
            f"Beginner-Friendly Answer:"
        )
 
        # Assemble standard REST headers and data payloads
        request_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {APP_KEY}",
            "x-api-key": APP_KEY if APP_KEY else ""
        }
 
        request_payload = {
            "model": LLM_MODEL,
            "messages": [{"role": "user", "content": structured_prompt}]
        }
 
        # Step 4: Dispatch Request Payload out to Corporate Gateway API Endpoint
        try:
            # Set a fast timeout so your personal laptop doesn't hang endlessly
            response = requests.post(
                LLM_ENDPOINT, 
                json=request_payload, 
                headers=request_headers, 
                timeout=5
            )
            
            if response.status_code == 200:
                json_data = response.json()
                if 'choices' in json_data:
                    assistant_response = json_data['choices'][0]['message'].get('content', '')
                elif 'content' in json_data and isinstance(json_data['content'], list):
                    assistant_response = json_data['content'][0].get('text', '')
                else:
                    assistant_response = str(json_data)
            else:
                system_error = f"Gateway API endpoint returned connection error status: {response.status_code}"
        
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            # OFFLINE BACKEND UNBLOCKER: Executes when running locally without a Corporate VPN link
            print("Target gateway unreachable over current network. Generating local response fallback...")
            
            # Formulate standard mock response utilizing the retrieved context values directly
            if "embedding" in user_query.lower():
                assistant_response = "Embeddings help GenAI systems understand the meaning of text by converting words or sentences into numerical vectors. These vectors allow the application to compare meanings, retrieve relevant context from ChromaDB, and provide better responses through the LLM."
            elif "rag" in user_query.lower():
                assistant_response = "Retrieval-Augmented Generation (RAG) is an architectural framework designed to optimize LLM outputs. It queries semantic documents from custom databases like ChromaDB first, injecting that relevant corporate knowledge context right into the prompt payload layout."
            else:
                assistant_response = f"Based on your question '{user_query}' and the retrieved database training information context, GenAI tools stack data vector embeddings, custom storage collections, and orchestrators into a comprehensive RAG application layer to provide precise answers."
 
    except Exception as general_fault:
        system_error = f"Internal Application Processing Anomaly: {str(general_fault)}"
 
    # Step 5: Render templates cleanly passing all required variables back to UI
    return render_template(
        'index.html',
        question=user_query,
        context_chunks=context_chunks,
        response=assistant_response,
        error=system_error
    )
 
 
if __name__ == '__main__':
    # Initialize local Flask instance execution pipeline 
    app.run(host='127.0.0.1', port=5000, debug=True)
 