from flask import Flask, request,render_template
import os

from fetch import youtubeSubtitles as ys

app = Flask(__name__)


@app.route('/transcribe', methods=['POST'])
def transcribe():
    data = request.get_json()
    video_url = data['video_url']
    text = ys.get_plain_transcript(video_url)
    return render_template('transcription.html', output= text)


if __name__ == '__main__':
    app.run(debug=True)
