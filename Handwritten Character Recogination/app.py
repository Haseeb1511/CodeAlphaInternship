import streamlit as st
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model("final_model.h5")

dict_word = {i:chr(65+i) for i in range(26)}

st.title("Handwritten Character Recognition (A-Z)")

st.write("Upload image here")

uploaded_file = st.file_uploader("upload Image ",type=["jpeg","png","jpg"])

if uploaded_file is not None:
    file_byte = np.asarray(bytearray(uploaded_file.read()),dtype=np.uint8)  # convert the uploaded image to open cv format
    img = cv.imdecode(file_byte,cv.IMREAD_COLOR)    #load in color gray
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)    #convert image to gray scale
    gray = cv.medianBlur(gray,5)   #medianBLur remove noise 
    ret,gray = cv.threshold(gray,75,180,cv.THRESH_BINARY)
    element = cv.getStructuringElement(cv.MORPH_RECT,(90,90))
    gray = cv.morphologyEx(gray,cv.MORPH_GRADIENT,element)

    gray = gray/255.   # Normalizing between 0 and 1
    gray = cv.resize(gray,(28,28))  #resize the image to (28,28)    
    input_image = gray.reshape(1,28,28,1)  # 4D tensor as input con CNN


    # MOdel
    pred = model.predict(input_image)[0]   #give arrray of prediction with probability after softmax is applied
    pred_arr = np.argmax(pred) # Output the image with highest Probability
    pred_char = dict_word[pred_arr]
    percentage = np.round(np.max(pred),2)*100

    fig,ax = plt.subplots(1,2,figsize=(4,4))
    ax[0].imshow(img)
    ax[1].imshow(gray,cmap="gray")
    ax[0].set_title("Original Pic")
    ax[1].set_title(f"Prediction = {pred_char}")
    ax[0].grid()
    ax[1].grid()
    st.pyplot(fig)

    st.subheader(f"Prediction = {percentage} and character = {pred_char}")




