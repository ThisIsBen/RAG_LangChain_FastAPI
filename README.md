# RAG_LangChain_FastAPI
A chatbot that is implement by using Framework: LangChain, LLM: Google Gemini, API Server: FastAPI, 
client Web UI: AngularJS


## Demo of this application(Run all the server side python programs on Google colab):
![RAG_Chatbot_Demo](https://github.com/user-attachments/assets/eae36727-babc-4839-b908-5b54676bd566)


## Quick tryout with Google Colab page:
Run all the cells in the Google Colab page, and then paste the printed "Public URL" to "fastAPIServerURL" variable in chatbot_client.html. \
Open chatbot_client.html with browser, then you can try out this RAG chatbot real quick.  
https://colab.research.google.com/drive/1DsCKNSydCq7DbJpsp4KST-myGiFyvzf5#scrollTo=p_aPBKrjtuzv





# Procedure to deploy it to your own PC:
## Get the API for using Google Gemini LLM. It provides $300 free credits for 90 days
### Use LangChain to run Gemini: 
Guide: https://python.langchain.com/docs/integrations/chat/google_generative_ai/  \
Gemini API Key: \
AIzaSyA-U0j8Cxp6n0Q8YgvDTNfDGiVnQXWML2Y

### Create Gemini API Key from Google AI Studio:
Guide: https://aistudio.google.com/apikey



### Use LangChain to run Google Vertex AI text_embedding:
Guide: https://python.langchain.com/docs/integrations/text_embedding/google_vertex_ai_palm/ \
Google Cloud Project ID: \
sublime-amp-451213-j2 \
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

## Reference:
### - Using LangChain to buile RAG
https://python.langchain.com/docs/tutorials/llm_chain/

### - Apply for a Public URL to run your server side program
If your want to run server side program with a Public URL(For example, running with Google Colab), you need to register a free ngrok account and get the Authetication token
#### Step1 Create a ngrok acount from the following URL
ngrok homepage: https://ngrok.com/
#### Step2 Copy your Authentication token like below
![image](https://github.com/user-attachments/assets/e5897ed9-d4dc-4f3a-954b-b019de86ff17)
#### Step3 Apply your Authentication token to "ngrokAuthToken" in chatbot_server.py



