import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI

def ingest_pdf(pdf_content: bytes):
   
    with open("temp.pdf", "wb") as f:
        f.write(pdf_content)

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()


    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local("faiss_index")

def query_pdf(question: str) -> str:
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    docs = vectorstore.similarity_search(question)

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-002",
        temperature=0.5,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=docs, question=question)
    return response
