# Consolidated Specifications for Document Preparation

## Introduction
This document consolidates specifications and workflows for preparing court petitions, briefs, and appendices. The goal is to streamline the process by defining clear guidelines and identifying opportunities for automation.

## Document Handling and Formats

### Word Documents
1. **Editing**:
    - Open the document in Microsoft Word.
    - Under the Review tab, select **Accept All Changes** and stop tracking changes.
    - Save the file with the appropriate naming convention.

2. **Conversion to WordPerfect**:
    - Open the document in WordPerfect.
    - Save the file to the designated directory: `P:\WordPerfect\USSC\[Petitioner Name PFC]`.

### WordPerfect Documents
1. **Initial Setup**:
    - Select the entire document (Ctrl+A), copy it (Ctrl+C), and paste it (Ctrl+V) into a new WordPerfect document.
    - Save with the specified format and naming convention.

2. **Macro Execution**:
    - Run the macro: `Tools > Macro > USSC Apx X5 macro.wcm`.
    - If the document crashes or contains unmanageable codes:
        - Use **Find and Replace** to remove problematic codes.
        - Replace codes with nothing and select **Replace All**.

## Formatting Guidelines

### General Styles
1. **Font**: Century Schoolbook, 12-point.
2. **Margins**: Left: 2.18", Right: 2.18", Top: 1.6", Bottom: 2.2".
3. **Line Height**: Automatic.
4. **Justification**: Full.

### Tabs
- Tab type: Left.
- Tab position: 0.25".
- Repeat every: 0.25".

### Footnotes
1. **Font**: Century Schoolbook, 10-point.
2. **Line Height**: Fixed at 0.167".
3. **Indentation**: Remove left indent.

### Widow/Orphan Control
- Ensure "Keep Text Together" is enabled.

## Table of Contents (TOC) and Table of Authorities (TOA)

### TOC Creation
1. Use the pre-defined template: `P:\USSC\0000 Templates\TOC`.
2. Verify TOC entries manually after generation.

### TOA Creation
1. Click the **Perfect Authority** button in WordPerfect.
2. Validate the entries and ensure all references are correct.

## File Naming and Storage
1. Save files in the designated directories with clear naming conventions:
    - `P:\WordPerfect\USSC\[Petitioner Name PFC]`.
2. Include versions or timestamps to avoid overwriting.

## Compliance and Review

### Word Count
1. Verify the word count complies with court limitations.
2. Notify the attorney immediately if the document exceeds the limit.

### Signature Block
1. Check for complete attorney information, including email address.
2. Confirm formatting aligns with court requirements.

## Appendices

### Formatting
1. Apply consistent styles across all appendices.
2. Remove extraneous codes or formatting errors.

### OCR and Quality Checks
1. Ensure all scanned pages are OCR-processed for text recognition.
2. Review scanned pages for legibility.

## Printing and Submission

### Printing Requirements
1. Use **Adobe Acrobat** to print to PDF.
2. Merge the cover page into the PDF:
    - Open the document in Adobe Acrobat.
    - Use the **Insert Page** option under the Document menu.

### Submission Checklist
1. Include the following:
    - Certificate of Service.
    - Certificate of Compliance.
    - Cost Estimate.
2. Email the attorney with the finalized PDF for review and approval.

## Automation Opportunities

### Tasks Suitable for Automation (Inferred from Documents)

#### Document Conversion
- **Source**: Instructions repeatedly mention converting documents between Word, WordPerfect, and PDF formats.
- **Opportunity**: Automating file format conversions using libraries like `python-docx` or external tools for WordPerfect.

#### Macro Execution
- **Source**: WordPerfect macro processes are described in multiple places (e.g., running specific macros like `USSC Apx X5 macro.wcm`).
- **Opportunity**: Automate macro execution using Python's COM interface or PerfectScript for WordPerfect.

#### Formatting Enforcement
- **Source**: Formatting instructions like applying specific fonts, line heights, margins, etc., are detailed (e.g., Century Schoolbook font, 12 pt, justification, tab stops).
- **Opportunity**: Automate style application using Python for Word documents (`python-docx`) or macros for WordPerfect.

#### PDF Manipulation
- **Source**: Merging PDFs and adding cover pages is described in several steps (e.g., using Adobe Acrobat).
- **Opportunity**: Use libraries like `PyPDF2` or `pikepdf` for programmatically handling PDFs.

#### Compliance Checks
- **Source**: Manual tasks like checking word count limits, ensuring proper page numbering, and validating TOC entries are emphasized.
- **Opportunity**: Automate word count validation, TOC/TOA checks, and format validation using Python.

#### Email Notifications
- **Source**: Emailing attorneys with updated PDFs and revisions is a common task in the workflow.
- **Opportunity**: Automate email generation using libraries like `smtplib` or `yagmail`.

### Why Include Automation Opportunities?
- **Relevance**: The purpose of the project is to reduce manual effort and streamline processes, making automation a key focus.
- **Utility**: Highlighting tasks that can be automated helps prioritize development efforts for the Python application.

---

## Conclusion
This document outlines the standardized specifications and processes for preparing legal documents. By automating repetitive tasks, significant time savings and error reduction can be achieved. This structure serves as a foundation for developing a Python-based solution to streamline the workflow.
