import streamlit as st

st.title("Haris' To-Do Tracker ✅")
st.write("Welcome to your personal task tracker, powered by **Streamlit**. Add, check off, and stay on top of your day!")

if 'todo_items' not in st.session_state:
    st.session_state['todo_items'] = []

def insert_task(new_item):
    st.session_state['todo_items'].append(new_item)

def remove_task(selected_item):
    if selected_item in st.session_state['todo_items']:
        st.session_state['todo_items'].remove(selected_item)

st.header("📝 Add Something to Do")
new_task = st.text_input("What do you want to get done today?", "")
if st.button("➕ Add"):
    if new_task:
        insert_task(new_task)
        st.success(f"Added: '{new_task}' to your list!")
    else:
        st.warning("Don't leave it blank, bro. Type a task first!")

st.header("📋 Your Current To-Do List")
if st.session_state['todo_items']:
    for i, item in enumerate(st.session_state['todo_items'], 1):
        st.write(f"{i}. {item}")
        if st.button(f"❌ Remove {i}"):
            remove_task(item)
            st.success(f"Removed: '{item}'")
else:
    st.info("Nothing here yet. Add a task above to get started!")

st.write("✨ Built with Streamlit by Haris.")
