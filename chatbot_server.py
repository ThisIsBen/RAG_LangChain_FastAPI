from langchain_RAG import *
from fastapi_server import *

if __name__=="__main__":

  
  # Define the web site as Know-How Source
  know_How_Source="https://lilianweng.github.io/posts/2023-06-23-agent/"

  # if not os.environ.get("GOOGLE_API_KEY"):
  #   os.environ["GOOGLE_API_KEY"] = "AIzaSyA-U0j8Cxp6n0Q8YgvDTNfDGiVnQXWML2Y"

  # from langchain.chat_models import init_chat_model

  # llm = init_chat_model("gemini-2.0-flash-001", model_provider="google_vertexai")
  from langchain_google_genai import ChatGoogleGenerativeAI

  llm = ChatGoogleGenerativeAI(

      model="gemini-1.5-pro",
      temperature=0,
      max_tokens=None,
      timeout=None,
      max_retries=2,

      # other params...
  )




  import vertexai

  vertexai.init(project=os.environ["PROJECT_ID"], location=os.environ["LOCATION"])

  # Initialize the a specific Embeddings Model version
  embeddings = VertexAIEmbeddings(model_name="text-embedding-004")


  from langchain_core.vectorstores import InMemoryVectorStore

  vector_store = InMemoryVectorStore(embeddings)








  # Load and chunk contents of the blog
  loader = WebBaseLoader(
      web_paths=(know_How_Source,),
      bs_kwargs=dict(
          parse_only=bs4.SoupStrainer(
              class_=("post-content", "post-title", "post-header")
          )
      ),
  )
  docs = loader.load()

  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
  all_splits = text_splitter.split_documents(docs)

  # Index chunks
  document_ids = vector_store.add_documents(documents=all_splits)
  print(document_ids[:3])
  print(all_splits[:3])

  # Compile RAG
  # Define prompt for question-answering
  prompt = hub.pull("rlm/rag-prompt")

  # Compile application
  #Declare global var
  global graph
  graph_builder = StateGraph(State).add_sequence([retrieve, generate])
  graph_builder.add_edge(START, "retrieve")
  graph = graph_builder.compile()





  # Start FastAPI
  import uvicorn
  ngrokAuthToken="2u4Q4n0UlcNfhXzpZ3XEHSrm7pN_5FAzxrrh3wqqEjcgJMfUF"
  ngrok.set_auth_token(ngrokAuthToken)
  ngrok_tunnel = ngrok.connect(8000)
  print('Public URL:', ngrok_tunnel.public_url)
  nest_asyncio.apply()
  uvicorn.run(app, port=8000)


  # Notice: ngrok will give users a new public URL every time the program is run, 
  # so  users  need to copy the URL printed in the command line, 
  # and apply it to the "fastAPIServer_PostURL" in chatbot_client.html