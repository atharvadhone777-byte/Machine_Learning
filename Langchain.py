# Foundation Models - Predict in multiple domains
# Two Divisions - 1)User Perspective - Features which are build from models  2)Builders Perspective - Features which are used to build model

# Langchain - Framework to build LLM based applications - Parts: Models, Prompts, Chains, Memory, Indexes, Agents
# Retrieval-Augmented-Generation(RAG) - We provide our private documentation so it can answer questions from that document
# Need of Langchain Flowchart - Vectorization of users query -> Sematic search(Understanding query) inside database -> Inside the pages of database information feed to brain along with query to generate output

# Models - Interface between user and AI : Language model (LLMs) - Text-to-Text, Embedding model - Text-to-vector
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

# Load Hugging Face pipeline
pipe = pipeline(
    task="text-generation",
    model="microsoft/Phi-3-mini-4k-instruct",
    max_new_tokens=100,
    temperature=0.7
)

# Convert it into a LangChain LLM
llm = HuggingFacePipeline(pipeline=pipe)

# Invoke the model
response = llm.invoke("Explain Retrieval-Augmented Generation in simple terms.")

print(response) 

# Prompts - Input to AI : Static and Dynamic(Re-usable) Prompts
# Chains/Pipeline - sequence of components connected together, where the output of one component becomes the input of the next, each block performs a specific task
# Indexes - Connects application to external knowledge
# Memory - Stores Chat History : ConversationBufferMemory(Short history), ConversationBufferWindowMemory(last n chats), Summarizer-Based Memory(Big history summarized in small), Custom Memory(For advanced cases)
# AI Agents - Chatbots on steroids
# Models - 




















