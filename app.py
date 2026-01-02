import streamlit as st
from ai_engine.generator import generate_image

st.title("AI Text-to-Image Generator")
prompt = st.text_input("Enter a text prompt",placeholder="A cat sitting on the moon")

if st.button("Generate Image"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()
    
    with st.spinner("Generating image..."):
        image = generate_image(prompt)
        st.success("Image generated successfully!")
        st.image(image, caption=prompt)
    
    

