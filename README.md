# LexFix - Court Document Text Corrector

LexFix is a Python-based tool designed to process and correct court documents, focusing on:
- Spelling correction
- Banned word filtering
- Margin fixing (future feature)

The tool extracts text from PDF documents, corrects spelling errors, and replaces banned words. The corrected text can be saved as a new PDF or text file.

## Features
- **Spelling Correction**: Automatically fixes misspelled words in the extracted text.
- **Banned Words**: Replaces predefined banned words with a placeholder.
- **PDF Handling**: Extracts text from PDF files and saves the corrected output.
- **Modular Structure**: Easily extendable to add more features like margin fixing or formatting adjustments.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/memoli1/LexFix.git
cd LexFix