"""
在线翻译小程序
使用 Google Translate API 进行文本翻译
"""

from flask import Flask, render_template, request, jsonify
import requests
import os


app = Flask(__name__)


class Translator:
    def __init__(self):
        # 使用免费的Google翻译API接口
        self.base_url = "https://translate.googleapis.com/translate_a/single"
    
    def translate(self, text, target_lang='en', source_lang='auto'):
        """
        翻译文本
        :param text: 待翻译的文本
        :param target_lang: 目标语言代码，默认为英文(en)
        :param source_lang: 源语言代码，默认自动检测(auto)
        :return: 翻译结果
        """
        params = {
            'client': 'gtx',
            'sl': source_lang,
            'tl': target_lang,
            'dt': 't',
            'q': text
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                # 提取翻译结果
                translated_text = ''.join([sentence[0] for sentence in data[0] if sentence[0]])
                return {
                    'success': True,
                    'original_text': text,
                    'translated_text': translated_text,
                    'target_language': target_lang,
                    'source_language': data[2] if len(data) > 2 else source_lang
                }
            else:
                return {
                    'success': False,
                    'error': f'API请求失败，状态码: {response.status_code}'
                }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }


@app.route('/')
def index():
    """主页路由"""
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate_text():
    """翻译接口"""
    data = request.get_json()
    
    text = data.get('text', '')
    target_lang = data.get('target_lang', 'en')
    source_lang = data.get('source_lang', 'auto')
    
    if not text:
        return jsonify({
            'success': False,
            'error': '未提供待翻译文本'
        })
    
    translator = Translator()
    result = translator.translate(text, target_lang, source_lang)
    
    return jsonify(result)


@app.route('/languages', methods=['GET'])
def get_languages():
    """返回支持的语言列表"""
    languages = {
        'auto': '自动检测',
        'zh': '中文',
        'en': '英语',
        'ja': '日语',
        'ko': '韩语',
        'fr': '法语',
        'de': '德语',
        'es': '西班牙语',
        'ru': '俄语',
        'ar': '阿拉伯语',
        'it': '意大利语',
        'pt': '葡萄牙语',
        'hi': '印地语'
    }
    
    return jsonify(languages)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)