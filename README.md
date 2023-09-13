
# ReImage Fusion 🌟

ReImage Fusion: Unleash Your Imagination with AI-Powered Background Alchemy

### Description:
ReImage Fusion is an innovative project that revolutionizes background replacement by integrating advanced AI and natural language processing. This tool enables users to provide a description of the background they envision for their images. The project then utilizes the state-of-the-art Stable Diffusion XL (SDXL) image generation model to bring that description to life, seamlessly replacing the original background.

### How It Works:

**1. Background Description :** Users input a textual description of the background they envision for their image through the user-friendly interface.

**2. AI Background Generation :** ReImage Fusion utilizes the SDXL model to generate a background image based on the provided description. This background is designed to perfectly match the user's vision.

**3. Resizing and Alignment :** The generated background is resized to fit the dimensions of the target image, ensuring a seamless integration.

**4. Automated Segmentation :** The tool employs advanced image processing techniques to automatically segment the main subject from the original image, creating a precise mask.

**5. Background Replacement :** The segmented subject with the transparent background is superimposed onto the newly generated background, creating a final image that aligns with the user's description.

### Benefits:

**1. Natural Language Input :** ReImage Fusion allows users to describe their desired background using natural language, making it accessible to a wide audience.

**2. AI-Generated Backgrounds :** The use of the powerful SDXL model ensures that the generated backgrounds are high-quality, contextually relevant, and visually appealing.

**3. Effortless Integration :** With automated subject segmentation, resizing, and superimposition, the tool streamlines the process of creating visually stunning images with custom backgrounds.

**4. Creative Freedom :** Users can enhance their images with backgrounds that match their specific vision, whether for artistic compositions, product photography, or storytelling.

##
**ReImage Fusion** redefines background replacement by combining user-provided descriptions with AI-generated backgrounds. It's a versatile tool that caters to both creative professionals and individuals seeking to elevate their visual content effortlessly and imaginatively.

##  Demo

https://github.com/soorajks2002/ReImage-Fusion/assets/59795959/6f713b0c-fbc0-4edd-b04e-6a917716d1be


## Run Locally

#### 1. Clone the project

```bash
  git clone https://github.com/soorajks2002/ReImage-Fusion.git
```

#### 2. Go to the project directory

```bash
  cd ReImage-Fusion
```

#### 3. Install packages

```bash
  pip install streamlit rembg Pillow
```

#### 4. Add API key

```bash
/api_key.py
        hugging_face_api_key = "HuggingFace access token"
```
If you don't have one, create one from [here](https://huggingface.co/settings/tokens).

#### 5. Start the application
```bash
  streamlit run app.py
```
## Screenshots

![App Screenshot](https://github.com/soorajks2002/ReImage-Fusion/blob/master/Screenshots/Screenshot%201.png?raw=true)

![App Screenshot](https://github.com/soorajks2002/ReImage-Fusion/blob/master/Screenshots/Screenshot%202.png?raw=true)

![App Screenshot](https://github.com/soorajks2002/ReImage-Fusion/blob/master/Screenshots/Screenshot%203.png?raw=true)

![App Screenshot](https://github.com/soorajks2002/ReImage-Fusion/blob/master/Screenshots/Screenshot%204.png?raw=true)

![App Screenshot](https://github.com/soorajks2002/ReImage-Fusion/blob/master/Screenshots/Screenshot%205.png?raw=true)

![App Screenshot](https://github.com/soorajks2002/ReImage-Fusion/blob/master/Screenshots/Screenshot%206.png?raw=true)
