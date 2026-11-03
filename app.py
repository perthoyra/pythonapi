"""A small REST API that encodes and decodes text with a simple substitution cipher."""

import string

from flask import Flask, jsonify, request

PLAIN_ALPHABET = string.ascii_lowercase
CIPHER_ALPHABET = "qwertyuiopasdfghjklzxcvbnm"

ENCODE_TABLE = str.maketrans(
    PLAIN_ALPHABET + PLAIN_ALPHABET.upper(),
    CIPHER_ALPHABET + CIPHER_ALPHABET.upper(),
)
DECODE_TABLE = str.maketrans(
    CIPHER_ALPHABET + CIPHER_ALPHABET.upper(),
    PLAIN_ALPHABET + PLAIN_ALPHABET.upper(),
)


def encode(text: str) -> str:
    """Substitute each letter a-z/A-Z using the cipher alphabet. Other characters are kept."""
    return text.translate(ENCODE_TABLE)


def decode(text: str) -> str:
    """Reverse the substitution done by encode()."""
    return text.translate(DECODE_TABLE)


app = Flask(__name__)


def _get_text():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get("text"), str):
        return None
    return data["text"]


@app.post("/encode")
def encode_endpoint():
    text = _get_text()
    if text is None:
        return jsonify(error='Request body must be JSON like {"text": "..."}'), 400
    return jsonify(text=text, encoded=encode(text))


@app.post("/decode")
def decode_endpoint():
    text = _get_text()
    if text is None:
        return jsonify(error='Request body must be JSON like {"text": "..."}'), 400
    return jsonify(text=text, decoded=decode(text))


if __name__ == "__main__":
    app.run(debug=True)
