import streamlit as st
def main():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == "Jayshil" and password == "Jayshil01":
            st.success("Login successful!")
            # You can redirect to another page or perform other actions upon successful login
            st.write("Success")
        else:
            st.error("Invalid username or password. Please try again.")
if __name__ == "__main__":
    main()

