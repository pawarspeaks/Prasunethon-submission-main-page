import streamlit as st

def main():
    st.title("Website Redirection")

    st.write("Click the links below to redirect to respective websites:")

    st.markdown("[User Page](https://hospital-management-user.streamlit.app/)")
    st.markdown("[Hospital Page](https://smart-healthcare-assistant-prasunethon.streamlit.app/)")
    st.markdown("[Smart City](https://smart-city-management.streamlit.app/)")

if __name__ == "__main__":
    main()
