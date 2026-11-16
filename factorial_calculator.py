import streamlit as st

def calculate_factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*calculate_factorial(n-1)

def main():
    st.title("Factorial calculator")
    number = st.number_input("Enter a number",
                    min_value = 0,
                    max_value = 200
                    )
    if st. button ("Calculate"):
        result = calculate_factorial(number)
        st.write(f"Result is {result}")

if __name__ =="__main__":
    main()