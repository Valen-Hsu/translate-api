# translate.py
A simple API for language detection and translation, allowing users to automatically detect the language of a given text and translate it to a specified target language.

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Installation

You can install the required dependencies using pip
``` bash
pip install -r requirements.txt
```

Or manually install the required libraries:
``` bash
pip install Flask langdetect googletran==4.0.0-rc1
```

## Usage

### Running the API
To start the API server, run the following command: 

``` bash
python translate.py
```

This will start the API on 'http://localhost:5000'

### API Endpoints

#### 'Post /translate'
Translate text from one language to another, with automatic language detection

**Request Body:**
- `text` (string): The text you want to translate.
- `dest_lang` (string, optional): The language code to which you want to translate the text. Defaults to 'en' (English)

**Example Request:**
```json
{
  "text": "你好",
  "dest_lang": "en"
}
```

**Example Response:**
```json
{
  "detected_language": "zh-cn",
  "translated_text": "Hello"
}
```

#### `POST /translate?lang=<target_language>`

Translate text from one language to another, with automatic language detection. The target language is specified as a query parameter.

**Query Parameters:**

- `lang` (string, optional): The language code to which you want to translate the text. Defaults to `'en'` (English).

**Request Body:**

- `text` (string): The text you want to translate.

**Example Request:**

```json
{
  "text": "Hello"
}
```

### Error Handling
The API will return a '400 Bad Request' status code for invalid inputs, such as missing text or an invalid language code.

**Example Error Response:**
```json
{
  "error": "Text input is required."
}
```

## Languages
support 55 languages out of the box ([ISO-639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes))
```
af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw
```

## Testing

Run the following to execute the project's tests:

``` bash
python -m unittest discover -s test
```

or 

``` bash
python -m unittest test.test_translate
```