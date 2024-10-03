from langchain_helper import get_few_shot_db_chain

import streamlit as st

st.title("NepTech Retail Store: Database 💻")

if 'question' not in st.session_state:
    st.session_state.question = ""
with st.form(key='my_form'):
    question = st.text_input("Question:", value=st.session_state.question)
    col1, col2 = st.columns(2)

    # Submit button in the first column
    with col1:
        submit_button = st.form_submit_button(label='Submit')

    # Clear button in the second column
    with col2:
        clear_button = st.form_submit_button(label='Clear')

if clear_button:
    st.session_state.question = ""

if submit_button and question:
    chain = get_few_shot_db_chain()
    result = chain.invoke(question)
    #answer = chain.run(question)
    answer = result['result']
    st.header("Answer:")
    st.code(answer,language='')

    intermediate_steps = result["intermediate_steps"]
    sql_query = intermediate_steps[2]['sql_cmd'] if 'sql_cmd' in intermediate_steps[2] else intermediate_steps[1]
    # Display the SQL query and the final answer
    st.header("Generated SQL Query:")
    st.code(sql_query, language='sql')
    
    