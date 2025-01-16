# textUtils/correct_spelling.py
from autocorrect import Speller
import language_tool_python

def correct_spelling_advanced(text):
    # Advanced correction using LanguageTool
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    advanced_correction = language_tool_python.utils.correct(text, matches)

    return advanced_correction


def correct_spelling_simple(text):
    spell = Speller()
    corrected_text = spell(text)
    return corrected_text