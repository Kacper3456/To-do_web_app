import streamlit as st
from Functions import write_todos,get_todos


st.title("To-do app")

todos=get_todos()

def add_todo():
    new_todo=st.session_state['new todo']+'\n'
    todos.append(new_todo)
    write_todos(todos)

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="New todo: ", placeholder="Enter a new todo here....",on_change=add_todo,key="new todo")

st.session_state