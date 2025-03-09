import getpass
import os
import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict

#If you're running this notebook on Google Colab, run the cell below to authenticate your environment.
import sys

if "google.colab" in sys.modules:
    from google.colab import auth

    auth.authenticate_user()


# Register necessary API Key
# For LANGSMITH
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "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"
# For Google API Key to use LLM (Gemini)
os.environ["GOOGLE_API_KEY"] = "AIzaSyA-U0j8Cxp6n0Q8YgvDTNfDGiVnQXWML2Y"

# For Google Cloud Platform Project to use the embedding model
from langchain_google_vertexai import VertexAIEmbeddings
os.environ["PROJECT_ID"]= "sublime-amp-451213-j2"
os.environ["LOCATION"]= "us-central1"


# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}
