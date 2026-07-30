import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

st.set_page_config(
    page_title="Potato Disease Classifier",
    page_icon="🥔",
    layout="centered"
)

st.title("🥔 Potato Disease Classification")
st.write("Upload a potato leaf image for disease detection")

@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model('potato_disease_model.keras')
        return model
    except:
        return None

def predict(image, model):
    img = image.convert("RGB").resize((224, 224))
    img_array = np.array(img, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array
    
    predictions = model.predict(img_array, verbose=0)
    
    # Get both probabilities
    early = float(predictions[0][0])
    late = float(predictions[0][1])
    
    return early, late

model = load_model()

if model is None:
    st.error("❌ Model not found. Please contact administrator.")
    st.stop()

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)
    
    if st.button("🔍 Predict Disease", type="primary"):
        with st.spinner("Analyzing image..."):
            early, late = predict(image, model)
        
        st.divider()
        st.subheader("📊 Results")
        
        # Display both classes with progress bars
        col1, col2 = st.columns(2)
        
        with col1:
            if early >= late:
                st.success(f"✅ **Early Blight**")
            else:
                st.write(f"**Early Blight**")
            st.progress(early)
            st.caption(f"{early:.1%}")
        
        with col2:
            if late > early:
                st.success(f"✅ **Late Blight**")
            else:
                st.write(f"**Late Blight**")
            st.progress(late)
            st.caption(f"{late:.1%}")
        
        st.divider()
        
        # Final prediction
        if early >= late:
            st.info("🌿 **Prediction: Early Blight**")
            st.warning("⚠️ Consider using fungicides.")
        else:
            st.info("🌿 **Prediction: Late Blight**")
            st.warning("⚠️ Immediate action recommended.")
