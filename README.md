pythonThe Synesthesia Engine: Algorithmic Image-to-Audio Mapping
🎨 ➔ 🎵

The Synesthesia Engine is an interdisciplinary computer science tool designed to bridge the gap between visual arts and auditory composition. By leveraging Unsupervised Machine Learning (K-Means Clustering), the system extracts the dominant mathematical properties of an image and translates them into harmonious musical sequences.

🚀 Core Features

Automated Color Extraction: Uses the K-Means algorithm to identify the top 5 dominant colors from any uploaded JPEG/PNG.

Intelligent Data Mapping: Converts Hex/RGB data into HSL (Hue, Saturation, Lightness) to determine musical pitch and octave.

Harmonious Synthesis: Constraints output to a C Major Pentatonic scale to ensure musically useful results for artists.

Real-time Processing: Optimized image down-sampling for near-instantaneous feedback.

Web Audio Integration: High-fidelity synthesis powered by Tone.js.

🛠️ Technology Stack

Backend: Python 3.x / Flask

Machine Learning: Scikit-learn (K-Means Clustering)

Image Analysis: Pillow (PIL), NumPy

Frontend: JavaScript, HTML5, CSS3

Audio Engine: Tone.js (Web Audio API wrapper)

📥 Installation & Setup

Follow these steps to run the Synesthesia Engine locally:

Clone the repository:
Bash

git clone https://github.com/georgejoseph753/Synesthesia-Engine.git
cd Synesthesia-Engine

Create a virtual environment (Recommended):

Bash

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install dependencies:

Bash

pip install -r requirements.txt

Run the application:
Bash

python app.py

Access the UI:
Open your browser and navigate to http://127.0.0.1:5000.

📖 Methodology & Design

This project follows a strict 6-step computational pipeline:

Input: User uploads a raw image asset.

Preprocessing: The image is down-sampled to a 50×50 pixel grid to increase K-Means efficiency.

Clustering: K=5 clusters are identified in the RGB color space.

Extraction: Centroids are converted to Hexadecimal format.

Mapping: Hue determines the note; Lightness determines the octave.

Output: A generated arpeggio is played back via the Web Audio API.

📝 Academic Context

This project was developed as part of the DLMCSPCSP01 - Project: Computer Science portfolio. It demonstrates the application of machine learning techniques to solve the real-world problem of creative block in multimedia artists.

Author: George Joseph

Course: Master in Computer Science (DLMCSPCSP01)

🛡️ License

This project is open-source and available under the MIT License.
