from typing import Literal

DOMAIN = [
    "Books",
    "Conversation",
    "Dialect",
    "Encyclopedic",
    "Financial",
    "Governmental",
    "Legal",
    "Medical",
    "News",
    "Other",
    "Readaloud",
    "Social Media",
    "Speeches",
    "Spoken",
    "Subtitles",
    "Web",
]
DOMAIN_TYPE = Literal[*DOMAIN]

LICENSE = Literal["cc0-1.0", "other", "cc-by-sa-4.0", "apache-2.0"]

LICENSE_NAMES_MAPPING = {
    "cc0-1.0": "CC0",
    "cc-by-sa-4.0": "CC BY-SA 4.0",
    "apache-2.0": "Apache 2.0",
}

LANGUAGES = ["da", "en", "se", "nb", "nn", "de", "fr", "nl", "it"]
LANG_TYPE = Literal[*LANGUAGES]

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
