import streamlit as st
from app_car import main as app1_main
from app_bike import main as app2_main


def main():
    selected_app = st.sidebar.radio("Select App", ["car", "bike"])
    if selected_app == "car":
        app1_main()
    else:
        app2_main()


if __name__ == "__main__":
    main()
