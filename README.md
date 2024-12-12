---

# Dual-AI Experience: Immersive VR Shopping and Intelligent Text-to-Speech System

## Overview

This project combines the cutting-edge technologies of Virtual Reality (VR) and Artificial Intelligence (AI) to deliver an innovative and accessible e-commerce experience. The platform consists of two key systems:

1. **Virtual Reality Shopping App**: An immersive platform allowing users to explore and interact with 3D models of products in a 360-degree virtual environment.
2. **Text-to-Speech Assistant**: An intelligent tool that enhances accessibility by providing auditory feedback and voice-driven navigation for visually impaired users.

By integrating these technologies, the project aims to redefine usability, inclusivity, and engagement in digital commerce.

---

## Features

### Virtual Reality Shopping App
- **Immersive 360° Environment**: Navigate and explore a realistic virtual shopping space.
- **Interactive 3D Models**: View products in detail and interact with 3D assets.
- **Floating Product Info Cards**: Get detailed product information while exploring.
- **WASD Navigation**: Move seamlessly through the virtual space.
- **Cross-Platform Compatibility**: Accessible via VR headsets and web browsers.

### Text-to-Speech Assistant
- **Content Accessibility**: Convert product details into speech using AI-driven NLP.
- **Customizable Voice Parameters**: Adjust pitch, rate, and volume for a personalized experience.
- **Seamless Integration**: Synchronizes with the VR system for an inclusive user journey.

---

## Technology Stack

- **Frontend**: A-Frame (WebVR Framework), HTML5, CSS3, JavaScript
- **Backend**: Flask (Python Web Framework)
- **Database**: MySQL with SQLAlchemy
- **AI**: SpeechSynthesis API, Cosine Similarity for Recommendations
- **3D Models**: glTF format for high-performance rendering

---

## Architecture

1. **Frontend**: Interactive and responsive design powered by A-Frame and JavaScript.
2. **Backend**: Flask handles API routing, template rendering, and backend logic.
3. **Database**: Stores product metadata, ratings, and recommendations.

---

## Installation

### Prerequisites
- Python 3.8+
- Flask
- MySQL
- Node.js (for A-Frame support)
- Browser with WebVR support (Chrome, Firefox)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Shravlearner/VR-Retail-app-using-NLP-and-Recommendation-system
   cd VR-Retail-app-using-NLP-and-Recommendation-system
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix
   venv\Scripts\activate     # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - Configure `config.py` with your MySQL credentials.
   - Run the initialization script:
     ```bash
     python init_db.py
     ```
5. Start the application:
   ```bash
   flask run
   ```

---

## Usage

1. Launch the application in your browser:
   ```
   http://127.0.0.1:5000/
   ```
2. Navigate through the VR shopping environment.
3. Use the Text-to-Speech feature for product details.

---

## Project Structure

```plaintext
Dual-AI-Experience/
├── app/
│   ├── static/          # Static assets (CSS, JS, images)
│   ├── templates/       # HTML templates
│   ├── routes.py        # Flask routes
│   ├── models.py        # Database models
│   └── utils.py         # Utility functions
├── data/
│   ├── products.csv     # Product dataset
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── LICENSE              # License information
```

---

## Results

- **Personalization Score**: Achieved a perfect score of 1.0 for the content-based recommendation system.
- **Performance Metrics**:
  - Precision, Recall, F1-Score for recommendation evaluation.
  - Real-time rendering and interaction within the VR app.

---

## Future Scope

- Add support for multilingual Text-to-Speech.
- Enhance VR interactivity with AR components.
- Scale the platform for larger product catalogs and datasets.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to customize this template further based on your specific implementation and requirements!
