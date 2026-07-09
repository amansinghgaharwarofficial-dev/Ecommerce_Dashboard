import streamlit as st

st.title("Simple Diet Planner: ")
st.header("Enter your Detail")
name =st.text_input("Enter your name ")
age = st.number_input("Enter your age",min_value=1,max_value=100)
weight = st.number_input("Enter your weight",min_value=1)
goal=st.selectbox(
    "Select your Goal",
    ["Weight loss","Weight Gain","Maintain Weight"]
)
if st.button("Get Diet Plan"):
    st.subheader(f"Hello,{name}")

    if goal == "Weight Loss":
        st.success("Diet Plan")
        st.write("Breakfast: Oats+Fruits")
        st.write("Lunch: Salad + Chicken")
        st.write("Dinner: Soup +Vegetables")
st.markdown("-----")
st.markdown( 
    "<p style ='text- align:center;'>@ 2026 Aman Stay Healthy | Built With FrameWork",
    unsafe_allow_html=True
)

