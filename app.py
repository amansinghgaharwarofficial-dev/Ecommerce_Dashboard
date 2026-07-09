import streamlit as st
#TITLE
st.title("My  first streamlit app : ")
st.write("Welcome to my first date analysis Dashboard :")
#Input functtion
num1 = st.number_input("Enter the first number :")
num2 = st.number_input("Enter the second number :")
#Select operation
operation = st.selectbox(
    "Choose Operation",
    ["Addition","Subtraction","Multiplication","Division"]
)
#Calculate
if st.button("calculate"):
    if operation == "Additon":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1*num2
    elif operation == "Division":
        if num2!=0:
            result=num1/num2
        else:
            result = "cannot divide by zero"
    st.success(f"Result:{result}")
#Addin Footer
st.markdown("----")
st.markdown(
    "<p style ='text- align:center;'>@ 2026 Aman | Built with calculator usin streamlit</p>",
    unsafe_allow_html=True
)