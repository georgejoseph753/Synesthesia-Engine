from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import io

app = Flask(__name__)

def get_dominant_colors(image_bytes, k=5):
    # 1. Open the image and convert to RGB
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    
    # 2. Resize the image drastically to speed up the math
    image = image.resize((50, 50))
    
    # 3. Convert image data to a numpy array and reshape it
    pixels = np.array(image).reshape(-1, 3)
    
    # 4. Apply K-Means Clustering
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(pixels)
    
    # 5. Extract the center points of these clusters
    dominant_colors = kmeans.cluster_centers_
    
    # Convert RGB arrays to Hex strings for the frontend
    hex_colors = []
    for color in dominant_colors:
        r, g, b = [int(c) for c in color]
        hex_colors.append(f"#{r:02x}{g:02x}{b:02x}")
        
    return hex_colors

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    try:
        image_bytes = file.read()
        colors = get_dominant_colors(image_bytes, k=5)
        return jsonify({'colors': colors})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
