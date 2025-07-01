from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # フロントエンドと連携するためにCORS許可

def extract_video_id(url):
    parsed = urlparse(url)
    if 'youtu.be' in parsed.netloc:
        return parsed.path[1:]
    elif 'youtube.com' in parsed.netloc:
        return parse_qs(parsed.query).get('v', [None])[0]
    return None

@app.route('/')
def home():
    return "YouTube字幕APIが動作中です"

@app.route('/get_subtitles', methods=['POST'])
def get_subtitles():
    data = request.get_json()
    url = data.get('url')
    video_id = extract_video_id(url)

    if not video_id:
        return jsonify({'error': '動画IDが見つかりません'}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        result = []
        for entry in transcript:
            result.append({
                'en': entry['text'],
                'ja': f"【仮訳】{entry['text']}"  # 仮訳（あとで翻訳APIで改善可）
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
s
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)