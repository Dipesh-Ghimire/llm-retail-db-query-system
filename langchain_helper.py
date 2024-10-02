from langchain_google_genai import GoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX,_mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from few_shots import few_shots_list
import os
from dotenv import load_dotenv
load_dotenv()


def get_few_shot_db_chain():
    llm = GoogleGenerativeAI(model='gemini-pro',google_api_key=os.environ['GOOGLE_API_KEY'],temperature=0.1)
    db_user = 'root'
    db_password = 'password'
    db_host = 'localhost'
    db_name = 'neptech_store'
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(i.values()) for i in few_shots_list]
    vectorstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots_list)
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore, k=2
    )
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )
    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"]
    )
    new_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True, prompt=few_shot_prompt)
    return new_chain

if __name__=="__main__":
    chain = get_few_shot_db_chain()
    print(chain.run("how many Dell brand laptops are there?"))
