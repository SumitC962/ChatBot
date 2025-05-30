# 📚 FastAPI Chatbot with PDF Q&A (Gemini API)

A FastAPI application that enables chatbot interactions and intelligent question-answering from uploaded PDF documents using Google's Gemini API and LangChain.

Requirements :-
Use Python and FastAPI to build the API. 
Integrate any open-source libraries for chatbot functionality (e.g., LangChain, Llamalndex, OpenAl API, Hugging Face, etc.).
Support t memory for better conversational context (optional but a plus).
Implement PDF processing to extract and answer questions based on uploaded files.
Bonus Points Implement a basic chat history/memory mechanism. Optimize responses for better accuracy and efficiency.
Write clean, well-structured, and maintainable code Deliverables A GitHub repository with the full implementation.


 Tech Stack

- FastAPI — for building the API
- Google Gemini API — for generating responses and embeddings
- LangChain— for PDF processing, chunking, and QA chain
- FAISS — for vector storage and similarity search
- Pydantic — for request validation
- Python 3.8+

 ## Project Structure
.
├── main.py                 
├── chatbot.py              
├── pdf_handler.py          
├── memory.py              
├── models.py              
├── .env                   
└── requirements.txt       


##  Setup Instructions

### 1. Clone the repository

git clone https://github.com/SumitC962/ChatBot.git
cd ChatBot



### 2. Install dependencies

pip install -r requirements.txt



### 3. Run the app


uvicorn main:app --reload


Open your browser and go to: [http://localhost:8000](http://localhost:8000)


## Author

Made with ❤️ by \[Sumit Chaudhari]
