import streamlit as st
st.set_page_config(
     page_title='Ayushmithra login',
     layout="centered"
)
def cs_body():
    st.title("Ayushmithra Login")
    print()
    with st.form(key="submit"):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')
cs_body()
def co():
    a,b=st.columns(2)
    a.button("Forgot password")
    b.button("New User")
co()