import pickle
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Set your Gemini API key
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

os.environ['GOOGLE_API_KEY'] = api_key

# Load vectorstore from pkl
def load_vectorstore(path: str = "vectorstore.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

# Initialize LLM (Gemini)
gemini_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the Gemini model (e.g., gemini-1.5-pro or gemini-1.5-flash)
    temperature=0.7,
    max_tokens=500
)

# Try loading vectorstore + retriever
retriever = None
try:
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
except Exception as e:
    print("⚠️ Vectorstore not loaded:", e)

# Main response function
def get_response_from_query(query: str) -> str:
    """
    Takes a user query and returns the generated response using context from vectorstore.
    """
    context = ""
    if retriever:
        docs = retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in docs])

    prompt_template = """
You are a legal assistant AI helping answer questions from Indian legal documents.

Please provide a clear, concise, and professional explanation based on the context.

Question: {query}

Context:
{context}

Answer:
"""
    prompt = PromptTemplate(
        input_variables=["query", "context"],
        template=prompt_template
    )
    chain = prompt | gemini_model
    result = chain.invoke({"query": query, "context": context})
    return result.content

if __name__ == "__main__":
    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        print("\n💬 Response:")
        print(get_response_from_query(query))
        print("-" * 60)
