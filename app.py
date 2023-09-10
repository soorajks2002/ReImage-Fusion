import streamlit as st
from remove_bg import remove_bg
from generate_image import generate_image
from superimpose import superimpose_image

st.title("Background Brush")

input_image = st.file_uploader("Upload your target image", type=['png', 'jpg', 'jpeg'], label_visibility='hidden')
if input_image :
    segmented_image = remove_bg(input_image)

    st.image(segmented_image)
    
    prompt_input = st.text_input("Please Enter Prompt for new Background")
    
    if prompt_input :
        with st.spinner("Generating Background") :
            new_bg = generate_image(prompt_input)
        if new_bg['image_generated'] :
            st.image(new_bg['image'])
            with st.spinner("Superimposing Background") :
                st.image(superimpose_image(segmented_image, new_bg['image']))
        else :
            st.info("API BUSY!")