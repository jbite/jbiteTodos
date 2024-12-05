import streamlit as st
import functions

todos = functions.showTodos()
st.title("My Todo App")
st.subheader("This is my todo App.")
st.write("This app is to increase your productivity.")


for i,todo in enumerate(todos):
    st.checkbox(todo,key=i+1)

st.text_input(label="",placeholder="Add new todo...")