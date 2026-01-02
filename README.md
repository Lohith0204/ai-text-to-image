# AI Text-to-Image Generator

## Live Demo
Try out the deployed application here:

🚀 **Streamlit App** → (paste the deployed streamlit link here)

## Overview
An artificial intelligence–based system that generates images from natural language text prompts.
This project demonstrates the practical use of diffusion-based generative models to convert textual descriptions into visually meaningful images.

The application leverages pre-trained text-to-image models to provide high-quality image generation without the need for training from scratch, making it efficient, scalable, and suitable for real-world applications.

## Features
- Accepts natural language text prompts as input
- Generates images based on the semantic meaning of the text
- Uses diffusion-based generative architecture
- Clean and modular project structure
- Fast inference using pre-trained models
- Easily extendable for advanced customization or deployment

## Tech Stack
- Python  
- Streamlit  
- Hugging Face Diffusers
- PyTorch  
- PIL (Pillow)

## Project Structure
```text
AI-Text-to-Image/
│
├── app.py                # Streamlit UI and application logic
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├──.gitignore             # Ignore Files
│
├── ai_engine/
│   └── generator.py      # Text-to-image generation logic
│
│
└── screenshots/          # Application screenshots
    ├── home.png
    ├── prompt.png
    └── output.png
```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2025-12-30 151517.png>)

### Text Prompt Input
![Text Prompt Input](<screenshots/Screenshot 2025-12-30 151559.png>)

### Generated Image Output
![Generated Image Output](<screenshots/Screenshot 2025-12-30 152604.png>)

## How It Works
Once all required dependencies are installed, the application is launched using Streamlit. The user is presented with a simple and interactive web interface.

The user enters a descriptive text prompt (for example, “a futuristic city at sunset”) and initiates the generation process. The text input is processed and passed to a pre-trained diffusion model, which iteratively transforms noise into a coherent image that aligns with the given description.

After a short inference period, the generated image is returned and displayed directly in the user interface.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application is useful for generating custom images from textual descriptions.

It can be applied in areas such as:
- Creative design and illustration
- Marketing and advertising visuals
- Concept art generation
- Educational demonstrations of generative AI
- Rapid prototyping of visual ideas
- Simply enter a text prompt and receive a generated image within seconds.

## Future Improvements
- Add multiple image generation per prompt
- Enable image resolution and style customization
- Integrate prompt enhancement techniques
- Save generated images locally or to cloud storage
- Deploy as a REST API for external applications

## Learning Outcomes
This project provided practical experience in implementing diffusion-based text-to-image generation using pre-trained models, understanding prompt-to-image inference workflows, and integrating generative AI pipelines into a Streamlit-based user interface. It strengthened skills in efficient model loading, modular project structuring, and deploying a complete, production-ready AI application suitable for real-world use and portfolio demonstration.