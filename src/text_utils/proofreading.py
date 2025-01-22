from language_tool_python import LanguageTool

def check_text_for_errors(text):
    """Check text for grammar, spelling, and punctuation errors."""
    tool = LanguageTool('en-US')
    matches = tool.check(text)
    errors = []
    for match in matches:
        errors.append({
            "text": match.context,
            "error": match.message,
            "suggestion": match.replacements
        })
    return errors