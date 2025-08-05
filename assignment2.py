import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string

# Load English tokenizer, POS tagger, lemmatizer, etc.
nlp = spacy.load("en_core_web_sm")

# Sample Text Input
sample_text = """
Hello this is a sample text !. Ok !
"""

# Pass the text through the NLP pipeline
doc = nlp(sample_text)

#  Step 1: Tokenization
tokens = [token.text for token in doc]
print("1️ Tokens:")
print(tokens)

#  Step 2: Remove Punctuation
tokens_no_punct = [token.text for token in doc if token.text not in string.punctuation]
print("\n2️ After Punctuation Removal:")
print(tokens_no_punct)

#  Step 3: Remove Stopwords
tokens_no_stopwords = [token.text for token in doc if not token.is_stop and token.text not in string.punctuation]
print("\n3️ After Stop Word Removal:")
print(tokens_no_stopwords)

#  Step 4: Lemmatization
lemmatized = [token.lemma_ for token in doc if not token.is_stop and token.text not in string.punctuation]
print("\n4️ Lemmatized Words:")
print(lemmatized)

#  Step 5: POS Tagging (Bonus from SpaCy)
pos_tags = [(token.text, token.pos_) for token in doc]
print("\n5️ POS Tags:")
print(pos_tags)
