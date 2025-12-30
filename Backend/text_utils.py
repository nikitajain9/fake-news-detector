import re

def list_to_string(texts):
    return [" ".join(text) if isinstance(text, list) else text for text in texts]

def preprocessing(texts):
    cleaned = []
    for text in texts:
        text = text.lower()
        text = re.sub(r"http\S+|www\S+", "", text)
        text = re.sub(r"[^a-z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        cleaned.append(text)
    return cleaned

