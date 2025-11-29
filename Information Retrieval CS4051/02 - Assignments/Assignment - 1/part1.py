from os import walk
from os.path import join, basename
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import stemmer

# Define the directory where your documents are stored
doc_directory = r"C:\Users\ammar\Desktop\Slides & Docs\Assignments + Notes\IR\Documents"

# Load stop words
with open("Urdu stopwords.txt", "r", encoding="utf8") as file:
    # Read the contents of the file and split it into lines
    stop_words = file.readlines()
    # Remove newline characters from each line
    stop_words = [word.strip() for word in stop_words]


# Initialize mappings between document names and unique document IDs
docid_to_filename = {}
filename_to_docid = {}

# Initialize mappings between token strings and unique term IDs
term_to_termid = {}
termid_to_term = {}
termid_counter = 0

# Initialize forward index
doc_index = {}

# Loop through each file in the directory
for filename in walk(doc_directory):
    # Skip directories
    if not filename[2]:
        continue
    file_path = join(filename[0], filename[2][0])
    
    # Read the contents of the file
    with open(file_path, "r", encoding="utf8") as file:
        contents = file.read()
        
        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(contents, "html.parser")
        
        # Remove headers and HTML tags from the document
        text = soup.get_text()
        
        # Tokenize the text
        tokens = word_tokenize(text)
        
        # Remove stop words and stem the tokens
        cleaned_tokens = []
        for token in tokens:
            if token.lower() not in stop_words:
                cleaned_token = stemmer.stem(token.lower())
                cleaned_tokens.append(cleaned_token)
                # Map the cleaned token to a unique term ID
                if cleaned_token not in term_to_termid:
                    termid_counter += 1
                    term_to_termid[cleaned_token] = termid_counter
                    termid_to_term[termid_counter] = cleaned_token
        
        # Map the filename to a unique document ID
        docid = len(docid_to_filename) + 1
        docid_to_filename[docid] = basename(file_path)
        filename_to_docid[basename(file_path)] = docid
        
        # Build forward index
        for position, token in enumerate(cleaned_tokens, start=1):
            termid = term_to_termid[token]
            if docid not in doc_index:
                doc_index[docid] = {}
            if termid not in doc_index[docid]:
                doc_index[docid][termid] = []
            doc_index[docid][termid].append(position)

# Write mappings to files
with open("docids.txt", "w") as file:
    for docid, filename in docid_to_filename.items():
        file.write(f"{docid}\t{filename}\n")

with open("termids.txt", "w") as file:
    for termid, term in termid_to_term.items():
        file.write(f"{termid}\t{term}\n")
