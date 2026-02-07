import streamlit as st
from agent.agent import Agent


st.title("Your Personal AI Agent")

agent = Agent()

with st.sidebar:
    st.header("Settings")
    st.selectbox("Choose a model", options=agent.models_list)
