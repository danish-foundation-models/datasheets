from typing import Literal

DOMAIN = Literal[
    "Books",
    "Conversation",
    "Dialect",
    "Encyclopedic",
    "Governmental",
    "Legal",
    "News",
    "Other",
    "Readaloud",
    "Social Media",
    "Speeches",
    "Spoken",
    "Subtitles",
    "Web",
]

LICENSE = Literal["cc0-1.0", "other", "cc-by-sa-4.0", "apache-2.0"]

LICENSE_NAMES_MAPPING = {
    "cc0-1.0": "CC0",
    "cc-by-sa-4.0": "CC BY-SA 4.0",
    "apache-2.0": "Apache 2.0",
}

LANGUAGES = ["da", "en", "se", "nb", "nn", "de", "fr", "nl", "it"]
LANG_TYPE = Literal["da", "en", "se", "nb", "nn", "de", "fr", "nl", "it"]

LANGUAGE_NAMES_MAPPING = {
    "da": "Danish",
    "en": "English",
    "se": "Swedish",
    "nb": "Norwegian Bokmål",
    "nn": "Norwegian Nynorsk",
    "de": "German",
    "fr": "French",
    "nl": "Dutch",
    "it": "Italian",
}
