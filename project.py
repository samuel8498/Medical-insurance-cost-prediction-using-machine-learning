import streamlit as st
import joblib

def main():
    # Custom HTML for styling the header
    html_temp = """
    <div style="background-color:#e1f5fe;padding:20px;border-radius:10px;">
        <h2 style="color:#01579b;text-align:center;">Health Insurance Cost Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Load the pre-trained model
    model = joblib.load('model_joblib_gr')

    # User input
    st.sidebar.header('Input Parameters')
    age = st.sidebar.slider('Enter Your Age', 18, 100)
    sex = st.sidebar.selectbox('Sex', ('Male', 'Female'))
    bmi = st.sidebar.number_input("Enter Your BMI Value", min_value=10.0, max_value=50.0, step=0.1)
    children = st.sidebar.slider("Enter Number of Children", 0, 4)
    smoker = st.sidebar.selectbox("Smoker", ("Yes", "No"))
    region = st.sidebar.selectbox("Enter Your Region", [1, 2, 3, 4], format_func=lambda x: f"Region {x}")

    # Convert categorical input to numerical
    sex_numeric = 1 if sex == 'Male' else 0
    smoker_numeric = 1 if smoker == 'Yes' else 0

    # Button for prediction
    if st.sidebar.button('Predict'):
        # Prediction
        prediction = model.predict([[age, sex_numeric, bmi, children, smoker_numeric, region]])
        st.sidebar.success(f"Your Estimated Insurance Cost is: ${prediction[0]:.2f}")

    # Display the input values and prediction
    st.write("### Your Input Values")
    st.write(f"- Age: {age}")
    st.write(f"- Sex: {sex}")
    st.write(f"- BMI: {bmi}")
    st.write(f"- Number of Children: {children}")
    st.write(f"- Smoker: {smoker}")
    st.write(f"- Region: {region}")

if __name__ == '__main__':
    main()
