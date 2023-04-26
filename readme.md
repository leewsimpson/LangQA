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