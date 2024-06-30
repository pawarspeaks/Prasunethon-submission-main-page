import streamlit as st
import webbrowser

def main():
    st.title("Website Redirection")

    st.write("Click the buttons below to redirect to respective websites:")

    if st.button("User Page"):
        webbrowser.open_new_tab("https://hospital-management-user.streamlit.app/")

    if st.button("Hospital Page"):
        webbrowser.open_new_tab("https://smart-healthcare-assistant-prasunethon.streamlit.app/")

    if st.button("Smart City"):
        webbrowser.open_new_tab("https://smart-city-management.streamlit.app/")

if __name__ == "__main__":
    main()
