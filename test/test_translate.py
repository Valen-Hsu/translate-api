import unittest

from translate.translate import app

class TranslateTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_translate_to_english(self):
        response = self.app.post(
            '/translate?lang=en',
            json={'text': '你好'}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['detected_language'], 'zh-cn')
        self.assertEqual(data['translated_text'], 'Hello')

    def test_translate_empty_text(self):
        response = self.app.post(
            '/translate?lang=es',
            json={'text': ''}
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Text input is required.')

    def test_invalid_language_code(self):
        response = self.app.post(
            '/translate?lang=zz',
            json={'text': 'Hello'}
        )
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
