import streamlit as st
import pickle
import string
import download_nltk
from download_nltk.corpus import stopwords
from download_nltk.stem.porter import PorterStemmer

# Ensure NLTK resources are downloaded at runtime
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')  # Correct resource name for tokenizer
    nltk.download('stopwords')

# Initialize the PorterStemmer
ps = PorterStemmer()

def transform_text(text):
    # Text preprocessing
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Remove non-alphanumeric characters
    y = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]

    # Stem the words
    y = [ps.stem(i) for i in y]

    return " ".join(y)

# Load vectorizer and model
cv = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("Email/SMS Spam Classifier")
input_email = st.text_area("Enter the email")

if st.button('Predict'):
    transformed_text = transform_text(input_email)
    vector_input = cv.transform([transformed_text])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
