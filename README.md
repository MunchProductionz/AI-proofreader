# AI Proofreader App ✏️🤖

A simple, visual AI-powered proofreading tool built with Python, OpenAI API, [Redlines](https://pypi.org/project/redlines/), and Streamlit.

## 🚀 Features

- Proofreads and improves input text using the OpenAI API
- Clearly highlights changes using Redlines
- Easy-to-use Streamlit interface for real-time feedback
- Supports uploading and proofreading of **PDF**, **Word**, and **PowerPoint** files
- Displays suggested corrections section-by-section for clarity

## 💼 Use Cases

This tool is ideal for internal use within organizations. It can be connected to a private or company-hosted LLM to automatically proofread business documents, client proposals, or internal memos before sharing. With simple prompt engineering, the app can be extended to perform a variety of language-focused tasks—such as tone adjustments, style checks, or rewriting for specific audiences.

## 🛠 Tech Stack

- Python
- OpenAI GPT API
- Redlines library
- Streamlit
- PyPDF, python-docx, python-pptx (for document extraction)

## 📦 Installation

```bash
git clone https://github.com/yourusername/ai-proofreader.git
cd ai-proofreader
pip install -r requirements.txt
