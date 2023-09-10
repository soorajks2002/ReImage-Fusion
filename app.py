import streamlit as st
from remove_bg import remove_bg
from generate_bg import generate_image
from superimpose import superimpose_image

st.set_page_config(page_title="ReImage Fusion", page_icon="🌟")
st.title("ReImage Fusion 🌟")

st.markdown("#### Select Your Image")
input_image = st.file_uploader("Upload your target image", type=['png', 'jpg', 'jpeg'], label_visibility='collapsed')
if input_image :
    st.markdown("#### Enter background description")
    prompt_input = st.text_input("Please Enter Prompt for new Background", label_visibility='collapsed')
    if st.button("Get New Background") :
        if prompt_input :
            with st.spinner("Generating Background") :
                new_bg = generate_image(prompt_input)
                
            if new_bg['image_generated'] :
                with st.spinner("Removing background") :
                    segmented_image = remove_bg(input_image)
                 
                img1, img2 = st.columns(2)
                with img1 :
                    st.markdown("#### Segmentated Image")
                    st.image(segmented_image)
                    
                with img2 :   
                    with st.spinner("Superimposing Background") :
                        st.markdown("#### New Image")
                        st.image(superimpose_image(segmented_image, new_bg['image']))
            else :
                st.info("API BUSY!")
            
        else :
            st.warning("Please Enter The Prompt")