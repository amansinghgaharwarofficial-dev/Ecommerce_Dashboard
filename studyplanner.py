import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Study Planner",
    page_icon="📚",
    layout="wide"
)
import streamlit as st
st.markdown("""
<style>
.stApp{
    background:#0b1220;
}
div[data-testid="metric-container"]{
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:18px;
    padding:18px;
    backdrop-filter:blur(12px);
    transition:all .35s ease;
}
div[data-testid="metric-container"]:hover{
    transform:translateY(-8px) scale(1.03);
    box-shadow:
    0px 15px 35px rgba(0,255,170,.35);
    border:1px solid #00ffaa;
}
.stButton>button{
    width:100%;
    border-radius:12px;
    transition:0.3s;
    background:#00ffaa;
    color:black;
    font-weight:bold;
}
.stButton>button:hover{
    transform:scale(1.05);
    background:#00d98c;
    box-shadow:0 0 20px #00ffaa;
}
.stCheckbox{
    transition:.3s;
}
.stCheckbox:hover{
    transform:translateX(8px);
}
.stTextInput>div>div>input{
    border-radius:12px;
    transition:.3s;
}
.stTextInput>div>div>input:hover{
    border:2px solid #00ffaa;
    box-shadow:0 0 15px rgba(0,255,170,.35);
}
[data-testid="stDataFrame"]{
    transition:.3s;
}
[data-testid="stDataFrame"]:hover{
    transform:scale(1.01);
    box-shadow:0px 10px 30px rgba(0,255,170,.3);
}
[data-testid="stSidebar"]{
    background:rgba(20,20,20,.9);
}
[data-testid="stSidebar"] *{
    transition:.25s;
}
[data-testid="stSidebar"] label:hover{
    color:#00ffaa;
}
[data-testid="stProgressBar"]{
    filter:drop-shadow(0px 0px 12px #00ffaa);
}
h1,h2,h3{
    transition:.3s;
}
h1:hover,
h2:hover,
h3:hover{
    color:#00ffaa;
    transform:translateX(5px);
}
</style>
""", unsafe_allow_html=True)
st.title("📚 Weekly / Monthly Study Planner")
st.markdown("Plan your study schedule and track your daily progress.")
st.sidebar.header("Planner Settings")
number_of_weeks = st.sidebar.slider(
    "Select Planner Duration",
    min_value=1,
    max_value=4,
    value=1
)
subjects = [
    "Python",
    "Java",
    "DSA",
    "DBMS",
    "Operating System",
    "Computer Network",
    "Machine Learning",
    "Revision"
]
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
if "planner" not in st.session_state:
    planner = {}
    for week in range(1, number_of_weeks + 1):
        planner[f"Week {week}"] = {}
        for day in days:
            planner[f"Week {week}"][day] = []
            for i in range(3):
                planner[f"Week {week}"][day].append(
                    {
                        "Task": "",
                        "Completed": False
                    }
                )
    st.session_state.planner = planner
if len(st.session_state.planner) != number_of_weeks:
    planner = {}
    for week in range(1, number_of_weeks + 1):
        planner[f"Week {week}"] = {}
        for day in days:
            planner[f"Week {week}"][day] = []
            for i in range(3):
                planner[f"Week {week}"][day].append(
                    {
                        "Task": "",
                        "Completed": False
                    }
                )
    st.session_state.planner = planner
planner = st.session_state.planner
total_tasks = 0
completed_tasks = 0
for week in planner:
    st.header(f" {week}")
    tabs = st.tabs(days)
    for index, day in enumerate(days):
        with tabs[index]:
            st.subheader(day)
            tasks = planner[week][day]
            for i in range(len(tasks)):
                task_name = st.text_input(
                    f"Task {i+1}",
                    value=tasks[i]["Task"],
                    key=f"{week}_{day}_{i}_task"
                )
                completed = st.checkbox(
                    "Completed",
                    value=tasks[i]["Completed"],
                    key=f"{week}_{day}_{i}_check"
                )
                planner[week][day][i]["Task"] = task_name
                planner[week][day][i]["Completed"] = completed
                if task_name != "":
                    total_tasks += 1
                    if completed:
                        completed_tasks += 1
st.divider()
st.header("📈 Overall Progress")
if total_tasks == 0:
    progress = 0
else:
    progress = completed_tasks / total_tasks
st.progress(progress)
st.metric(
    "Completion Percentage",
    f"{progress*100:.1f}%"
)
st.metric(
    "Completed Tasks",
    f"{completed_tasks}/{total_tasks}"
)
st.divider()
st.header("Daily Progress Summary")
summary = []
for week in planner:
    for day in days:
        tasks = planner[week][day]
        total = len([t for t in tasks if t["Task"] != ""])
        done = len(
            [t for t in tasks if t["Task"] != "" and t["Completed"]]
        )
        if total == 0:
            percent = 0
        else:
            percent = round(done / total * 100)
        summary.append({
                "Week": week,
                "Day": day,
                "Completed": done,
                "Total": total,
                "Progress (%)": percent}
        )
summary_df = pd.DataFrame(summary)
st.dataframe(summary_df, use_container_width=True)
csv = summary_df.to_csv(index=False)
st.download_button(
    label="⬇ Download Progress Report",
    data=csv,
    file_name="study_progress.csv",
    mime="text/csv"
)