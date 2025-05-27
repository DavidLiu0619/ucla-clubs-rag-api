import os
import pandas as pd
from langchain.prompts import PromptTemplate
# from langchain.document_loaders import DataFrameLoader
from langchain_community.document_loaders import DataFrameLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI


# Env & paths
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DATA_PATH = "ucla_orgs_cleaned_unique.csv"
DB_DIR    = "./chroma_db"

# Models
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
llm_model       = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                         temperature=0.75, top_p=0.8)

# Build or load Chroma vectorstore
if not os.path.isdir(DB_DIR) or not os.listdir(DB_DIR):
    df     = pd.read_csv(DATA_PATH)
    loader = DataFrameLoader(df, page_content_column="description")
    docs   = loader.load()
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding_function=embedding_model,
        persist_directory=DB_DIR
    )
    vectorstore.persist()
else:
    vectorstore = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding_model
    )

retriever = vectorstore.as_retriever()

# Instructional prompt template
rag_prompt = PromptTemplate.from_template("""
You are a helpful advisor assisting UCLA students in exploring campus clubs and organizations.

Use the following context to accurately answer the student's question.

Context:
{context}

Question:
{question}

Instructions:
- If the answer cannot be found in the context, respond with: "I could not find that information. Please check the official UCLA Student Organizations page: https://community.ucla.edu/studentorgs."
- Keep your response clear and concise.
- If the student's interest is unclear or they ask for general recommendations, ask a follow-up question to better understand their interests before advising.
- If the student's interest is clear, recommend the top 3 most relevant clubs. For each, include:
  • the club name (as it appears in the context)  
  • a brief explanation of why it fits according to context and the student's interests 
  • the each club’s **detail URL from the `detail_url` field** in the context (do not make up URLs) and 
  • the detail URL exactly once, in plain text at the end, like `Link: https://…`
- When you provide club recommendations, your entire answer may be up to 10 sentences long; otherwise keep it under five sentences.
- Format your answer as a bulleted list.
""")

# Main answering function
def answer_question(question: str) -> str:
    docs = retriever.get_relevant_documents(question)

    # Format context with metadata
    context = "\n\n".join([
        f"Club Name: {doc.metadata.get('name', 'Unknown')}\n"
        f"Category: {doc.metadata.get('category', 'N/A')}\n"
        f"Detail URL: {doc.metadata.get('detail_url', 'N/A')}\n"
        f"Description: {doc.page_content}"
        for doc in docs[:5]
    ])

    # Format prompt
    prompt = rag_prompt.format(context=context, question=question)

    # Call Gemini model
    response = llm_model.invoke(prompt)
    return response.content
