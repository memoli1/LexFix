from autocorrect import Speller

def correct_spelling(text):
    """Correct the spelling of the text."""
    spell = Speller()
    corrected_text = spell(text)
    return corrected_text

def ban_words(text, banned_words):
    """Replace banned words in the text with a placeholder."""
    for word in banned_words:
        text = text.replace(word, "[BANNED]")
    return text
