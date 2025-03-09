# RAG_LangChain_FastAPI
A chatbot that is implement by using Framework: LangChain, LLM: Google Gemini, API Server: FastAPI , \ client Web UI: AngularJS



## Get the API for using Google Gemini LLM. It provides $300 free credits for 90 days
### Use LangChain to run Gemini: 
Reference: https://python.langchain.com/docs/integrations/chat/google_generative_ai/
Gemini API Key: \
AIzaSyA-U0j8Cxp6n0Q8YgvDTNfDGiVnQXWML2Y

### Create Gemini API Key from Google AI Studio:
https://aistudio.google.com/apikey



### Use LangChain to run Google Vertex AI text_embedding:
https://python.langchain.com/docs/integrations/text_embedding/google_vertex_ai_palm/
Google Cloud Project ID: \
sublime-amp-451213-j2
LOCATION: \
us-central1 


### Troubleshoot: Solution for 403 permission denied
Set the API Key as GOOGLE_API_KEY instead of Gemini_API_KEY environment variable



## Install requirements:
### Install RAG requirements: framwork:langchain LLM:Google gemini-1.5-pro
If you want to use Google colab to run the all the server side python program, \
you need to add ! at the front of each pip install xxxx
```
pip install --quiet --upgrade langchain-text-splitters langchain-community langgraph

pip install -qU "langchain[google-vertexai]"

pip install -qU langchain-google-vertexai
```

### Install FastAPI requirements:
If you want to use Google colab to run the all the server side python program, \
you need to add ! at the front of each pip install xxxx
```
pip install fastapi nest-asyncio pyngrok uvicorn
```

## Demo Google Colab page:
https://colab.research.google.com/drive/1DsCKNSydCq7DbJpsp4KST-myGiFyvzf5#scrollTo=p_aPBKrjtuzv



## Demo of this application(Run all the server side python programs on Google colab):
![RAG_Chatbot_Demo](https://github.com/user-attachments/assets/eae36727-babc-4839-b908-5b54676bd566)




## Reference:
https://python.langchain.com/docs/tutorials/llm_chain/
