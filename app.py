from flask import Flask, request, jsonify
from flask_cors import CORS
from pytube import YouTube

app = Flask(__name__)
CORS(app)

@app.route('/api/video-details', methods=['POST'])
def get_video_details():
    data = request.json
    link = data.get('link')
    
    if not link:
        return jsonify({"error": "No link provided"}), 400

    try:
        y_tube = YouTube(link)
        video_details = {
            'title': y_tube.title,
            'description': y_tube.description,
            'streams': [(i, str(stream)) for i, stream in enumerate(y_tube.streams.filter(progressive=True))]
        }
        return jsonify(video_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
