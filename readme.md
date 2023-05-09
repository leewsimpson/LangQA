### Create fresh Enviornment
python -m venv .venv         

### Install Packages:
* langchain
* openai
* atlassian-python-api
* html2text
* chromadb
* tiktoken
* youtube-transcript-api
#### If you include documents from confluence:
* docx2txt
* pdf2image
* Needs Tesseract installing - brew install tesseract
* pytesseract
* Pillow
* svglib

### Create .env
* OPENAI_API_KEY="xxx"
* CONFLUENCE_PAT="yyy"

## Note there is a bug with the confluence loader that incorrectly assigns the token to the wrong place.  In the constructor of the library - change it to use _token_ instead.

## Interesting Links
* List of LLMs - https://github.com/Hannibal046/Awesome-LLM
* Langflow - https://github.com/logspace-ai/langflow
* React paper - https://arxiv.org/abs/2210.03629
* Microsoft Semantic Kernel - https://github.com/microsoft/semantic-kernel
