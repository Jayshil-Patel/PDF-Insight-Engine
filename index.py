import streamlit as st
# st.title('PDF-Insight-Engine')
from OpenAI_API import API_key
# def main():
st.set_page_config(page_title='PDF Insight engine')
st.header('Ask you PDF  ')

pdf = st.file_uploader('Upload your PDF',type='pdf')
    
    



# if __name__ == 'main':
#     main()