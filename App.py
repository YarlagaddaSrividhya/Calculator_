import streamlit as st 
st.title("Calculator")
number1=st.number_input("Insert a number",placeholder="Enter your first number")
number2=st.number_input("Insert a number",placeholder="Enter your second number")
operation=st.selectbox("select the operation",("Addition","Substraction","Multiplication","Division"))
ret=st.button("calculate")
if ret:
    if operation=="Addition":
        st.write(number1+number2)
        st.balloons()
    elif operation=="Substraction":
        st.write(number1-number2)
    elif operation=="Multiplication":
            st.write(number1*number2)
    elif operation=="division":
            st.write(number1%number2)
    
    
