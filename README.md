# Substitution Cipher API

A small REST API built with Flask that encodes and decodes text using a simple substitution cipher.

## How the cipher works

Every letter is replaced with the letter at the same position in a fixed cipher alphabet:

```
Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: qwertyuiopasdfghjklzxcvbnm
```

- Upper/lower case is preserved (`A` → `Q`, `a` → `q`).
- Digits, spaces, punctuation and non-ASCII characters are left unchanged.

> Note: a substitution cipher is for learning purposes only. It is not secure encryption.

## Requirements

- Python 3.14
- Flask 3.1.3

## Setup

```bash
python -m venv .venv
# Windows (some Python builds use .venv\bin instead of .venv\Scripts)
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python app.py
```

The API starts on `http://127.0.0.1:5000`.

## Endpoints

### `POST /encode`

Request:

```json
{ "text": "Hello, World!" }
```

Response `200`:

```json
{ "text": "Hello, World!", "encoded": "Itssg, Vgksr!" }
```

### `POST /decode`

Request:

```json
{ "text": "Itssg, Vgksr!" }
```

Response `200`:

```json
{ "text": "Itssg, Vgksr!", "decoded": "Hello, World!" }
```

### Errors

If the body is not JSON or `text` is missing / not a string, both endpoints return `400`:

```json
{ "error": "Request body must be JSON like {\"text\": \"...\"}" }
```

## Examples with curl

```bash
curl -X POST http://127.0.0.1:5000/encode -H "Content-Type: application/json" -d "{\"text\": \"Hello, World!\"}"
curl -X POST http://127.0.0.1:5000/decode -H "Content-Type: application/json" -d "{\"text\": \"Itssg, Vgksr!\"}"
```

## Tests

```bash
python -m unittest -v
```

## Project structure

```
app.py            Flask app and cipher functions
test_app.py       Unit tests
rest.http         Example requests (VS Code REST Client / JetBrains HTTP Client)
requirements.txt  Dependencies
```
