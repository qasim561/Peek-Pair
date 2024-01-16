import streamlit as st
import pandas as pd
import pyodbc

server = 'DESKTOP-J2T6H2B\QASIM'
database = 'project_01'
username = 'qasim_01'
password = '561'

connection_str = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_str)

def get_chatbot_response(user_input):
    query = f"SELECT response FROM chatbot WHERE User_Input = '{user_input}'"
    df = pd.read_sql(query, connection)
    if not df.empty:
        return df.iloc[0]['response']
    else:
        return "I'm sorry, I don't understand that."

def main():
    st.write("# <u>InfoBuddy</u>",unsafe_allow_html=True)
    

    user_input = st.text_input('You:', '')
    if st.button('Ask'):
        chatbot_response = get_chatbot_response(user_input)
        #st.text(f'Chatbot: {chatbot_response}')
        st.info(f'{chatbot_response}')  # Concatenate the label and response

if __name__ == '__main__':
    main()
