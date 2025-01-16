# textUtils/restore_punctuation.py

from transformers import pipeline

def restore_punctuation(text):
    """Restore punctuation using a transformer model."""
    punctuation_model = pipeline("text2text-generation", model="facebook/bart-large-cnn")
    # The model expects input with appropriate formatting.
    restored_text = punctuation_model(text)[0]['generated_text']
    return restored_text