from flask import Flask, request, jsonify
from langdetect import detect
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'Text input is required.'}), 400

    dest_lang = request.args.get('lang', 'en')
    try:
        detected_lang = detect(text)
        translated_text = translator.translate(text, dest=dest_lang).text
        return jsonify({
            'detected_language': detected_lang,
            'translated_text': translated_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
