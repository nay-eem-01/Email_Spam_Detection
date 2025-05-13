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