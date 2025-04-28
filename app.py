import streamlit as st

# In-memory storage for simplicity
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title("Simple Task Tracker")

# Input field to add a new task
new_task = st.text_input("Add a new task:")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Please enter a task name.")

st.subheader("Your Tasks")

# Display the tasks
for idx, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write(f"✅ {task['task']}" if task["completed"] else f"🔲 {task['task']}")
    with col2:
        if st.button("Toggle", key=f"toggle_{idx}"):
            st.session_state.tasks[idx]["completed"] = not st.session_state.tasks[idx]["completed"]
