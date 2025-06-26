import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np


st.set_page_config(page_title="Smart Food Spoilage Detector", layout="centered")
st.title('Smart Food Spoilage Detector')
st.header('Image upload')
model=load_model('model.keras')
uploaded_file=st.file_uploader('Upload an image of fruit and vegetable:',type=['jpg','jpeg','png'])

if uploaded_file is not None:
    result=[]  
    image = Image.open(uploaded_file)
    image_resized = image.resize((128, 128))
    
    class_names = ['Fresh', 'Rotten']
    st.image(image,width=(300))
    
    img_array=np.array(image_resized)/255.0
    img_array=np.expand_dims(img_array,axis=0)
    
    prediction=model.predict(img_array)[0]
    predicted_class = class_names[np.argmax(prediction)]
    
    st.header(f'Predicted : {predicted_class}')
    
    st.subheader("Storage Tip")
    if predicted_class == "Fresh":
        st.info("Keep your produce refrigerated to extend freshness.")
    else:
        st.warning("Consider using or discarding soon. Check for visible spoilage before consumption.")
    
    spoilage_index = int(np.round(prediction[0] * 10))
       
    st.header(f'Predicted Spoilage Index: {spoilage_index}/10') 
    
    days_left = max(0, 10 - spoilage_index)
    st.header(f'Estimated days left before spoilage: {days_left} days')
    
    
    
    st.subheader("Spoilage Progression Line Plot")
    total_days = 10
    days = np.arange(0, total_days + 1)
    spoilage_values = days

    fig3, ax3 = plt.subplots(figsize=(7, 3))
    ax3.plot(days, spoilage_values, label="Spoilage Index", color="red", linewidth=2)
    ax3.scatter(spoilage_index, spoilage_index, color="orange", s=100, label="Today")
    ax3.axvline(spoilage_index, color="orange", linestyle="--", alpha=0.7)
    ax3.axvspan(spoilage_index, total_days, color="green", alpha=0.1, label="Days Left")
    ax3.set_xlabel("Days")
    ax3.set_ylabel("Spoilage Index")
    ax3.set_xticks(days)
    ax3.set_yticks(days)
    ax3.set_title("Estimated Spoilage Over Time")
    ax3.legend()
    st.pyplot(fig3)

    
    
    
    
        
