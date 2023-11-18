import streamlit as st
import os

model_file = 'model.pkl'
if os.path.exists(model_file):
    model = pickle.load(open('model.pkl','rb'))
else:
    print(f"Error: File {model_file} not found.")
    
st.markdown("<h1 style='text-align: center;'>AMAA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>CROP PREDICTION SYSTEM🌱</h3>", unsafe_allow_html=True)

N = float(st.number_input('Nitrogen', 0,100))
P = float(st.number_input('Phosphorus', 0,100))
K = float(st.number_input('Potassium', 0,100))
temperature = float(st.number_input('Temperature', 0,100))
humidity = float(st.number_input('Humidity', 0,100))
ph = float(st.number_input('Ph', 0,100))

btn = st.button("Crop Prediction")

if btn:
    pred = model.predict(np.array([N,P,K,temperature,humidity,ph]).reshape(1,-1))
    print(pred)
    print(np.array(pred))
    pred = np.array([*pred])
    print(pred)
    st.subheader(*pred)
