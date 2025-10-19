import streamlit as st
import pickle
import pandas as pd

# Step 1: Load the model
model = pickle.load(open('model-reg-67130701706.pkl', 'rb'))

st.title('Sales Prediction with Regression Model')

st.write('Enter the advertising budgets for each platform to predict sales.')

# Get input from the user
youtube_budget = st.slider('YouTube Budget', 0, 1000, 50)
tiktok_budget = st.slider('TikTok Budget', 0, 1000, 50)
instagram_budget = st.slider('Instagram Budget', 0, 1000, 50)

# Step 2: Create a new DataFrame with user input
new_data = pd.DataFrame({
    'youtube': [youtube_budget],
    'tiktok': [tiktok_budget],
    'instagram': [instagram_budget]
})

# Step 3: Make predictions
predictions = model.predict(new_data)

st.subheader('Estimated Sales')
st.write(f"The estimated sales are: {predictions[0]:.2f}")
