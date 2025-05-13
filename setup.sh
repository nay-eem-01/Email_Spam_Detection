#!/bin/bash

# Create .streamlit config folder
mkdir -p ~/.streamlit/

# Create Streamlit config file
echo "\
[server]\n\
port = \$PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

# Download NLTK data listed in nltk.txt
python -c "import nltk; [nltk.download(line.strip()) for line in open('nltk.txt')]"
