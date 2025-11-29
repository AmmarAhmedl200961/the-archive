# encoding: utf-8
# read excel file
import pandas as pd
import numpy as np
# parse docx file
# !pip install python-docx
from docx import Document
import csv
# parse arguments
import argparse
import os,sys
# for computing scores
import math
# for counting term frequencies
from collections import Counter
# preprocess queries - as in part 1
from nltk.tokenize import word_tokenize
import stemmer

def read_qrels(file):
    qrels = {}
    df = pd.read_excel(file, sheet_name=None)
    for sheet in df:
        for index, row in df[sheet].iterrows():
            topic_id = row['Topic Id']
            doc_id = row['Doc Id']
            relevance = row['Doc Relevancy']
            if topic_id not in qrels:
                qrels[topic_id] = {}
            qrels[topic_id][doc_id] = relevance
    return qrels

def evaluate(qrels_file, scores):
    qrels = read_qrels(qrels_file)
    cutoffs = [5, 10, 20, 30]
    p_at_cutoffs = {c: [] for c in cutoffs}
    aps = []
    for topic_id in qrels:
        if topic_id not in scores:
            continue
        ranked_list = scores[topic_id]
        rels = [qrels[topic_id].get(doc_id, 0) for doc_id in ranked_list]
        p_at_k = []
        num_rel = 0
        for k in range(len(ranked_list)):
            if rels[k] > 0:
                num_rel += 1
                p_at_k.append(num_rel / (k + 1))
        ap = sum(p_at_k) / len(p_at_k) if p_at_k else 0
        aps.append(ap)
        for c in cutoffs:
            p_at_c = num_rel / c
            p_at_cutoffs[c].append(p_at_c)
    aps=np.array(aps) 
    map_score = np.divide(aps.sum(), len(aps))
    # Fix for ZeroDivisionError: division by zero
    p_at_cutoffs_avg = {}
    for c in cutoffs:
        if len(p_at_cutoffs[c]) == 0:
            raise ValueError("Denominator must not be zero")
        p_at_cutoffs_avg[c] = sum(p_at_cutoffs[c]) / len(p_at_cutoffs[c])
    return map_score, p_at_cutoffs_avg


def extract_queries(docx_file):
    """Extract queries from a docx file"""
    document = Document(docx_file)
    table = document.tables[0]
    queries = []
    for row in table.rows[1:]:
        queries.append(row.cells[3].text)
    return queries

def preprocess_query(query):
    # Load stop words
    with open(r"C:\Users\ammar\Desktop\Slides & Docs\Assignments + Notes\IR\Urdu stopwords.txt", "r", encoding="utf8") as file:
        # Read the contents of the file and split it into lines
        stop_words = file.readlines()
        # Remove newline characters from each line
        stop_words = [word.strip() for word in stop_words]
    
    # Tokenize the text
    tokens = word_tokenize(query)
    # following is not working as expected:
    # # Remove stop words and stem the tokens
    # cleaned_tokens = []
    # for token in tokens:
    #     if token.lower() not in stop_words:
    #         cleaned_token = stemmer.stem(token.lower())
    #         cleaned_tokens.append(cleaned_token)
    # return cleaned_tokens
    return [token for token in tokens if token.lower() not in stop_words]

def compute_idf(docs):
    N = len(docs)
    idf = {}
    for doc in docs:
        for term in set(doc):
            if term not in idf:
                idf[term] = 0
            idf[term] += 1
    for term in idf:
        idf[term] = np.log(N / idf[term])
    return idf

def compute_bm25(query, doc, docs, k1=1.2, b=0.75):
    idf = compute_idf(docs)
    tf = Counter(doc)
    avgdl = sum([len(doc) for doc in docs]) / len(docs)
    score = 0
    for term in query:
        if term in tf:
            score += idf[term] * ((tf[term] * (k1 + 1)) / (tf[term] + k1 * (1 - b + b * (len(doc) / avgdl))))
    return score

def compute_lm_dirichlet(query, doc, docs, mu=2000):
    tf = Counter(doc)
    pwc = {}
    for term in set(query):
        pwc[term] = np.sum([Counter(d)[term] for d in docs]) / np.sum([len(d) for d in docs])
    score = 0
    for term in query:
        if term in tf:
            score += np.log((tf[term] + mu * pwc[term]) / (len(doc) + mu))
        else:
            score += np.log(mu * pwc[term] / (len(doc) + mu))
    return score

def compute_tf_idf(query, doc, docs):
    idf = compute_idf(docs)
    tf = Counter(doc)
    score = 0
    for term in query:
        if term in tf:
            score += tf[term] * idf[term]
    return score

def parse_args():
    """Parse command line arguments and add positional arguments --score"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--score', type=str, help='scoring function to use=TF-IDF, BM25, or LM')
    return parser.parse_args()

if __name__ == "__main__":
    # extract queries from docx file
    urdu_queries = extract_queries(r"C:\Users\ammar\Desktop\Slides & Docs\Assignments + Notes\IR\queries.docx")
    print('raw queries: ', urdu_queries, '\n')
    
    
    # preprocess queries
    for i in range(len(urdu_queries)):
        urdu_queries[i] = preprocess_query(urdu_queries[i])
    
    parser = argparse.ArgumentParser(description='Search for a query in a collection of documents')
    args= parser.add_argument('--score', type=str, help='scoring function to use=TF-IDF, BM25, or LM')
    args= parser.add_argument('--query', type=str, help='query to search')
    args = parser.parse_args()
    
    if args.query is not None:
            query = preprocess_query(args.query)
            print(f"Search results for query: {' '.join(query)}\n")
            
            # read from forward index: doc_index.txt
            with open(r"C:\Users\ammar\Desktop\Slides & Docs\Assignments + Notes\IR\doc_index.txt", "r", encoding="utf8") as docs:
                docs.read()      
                # call appropriate scoring function
                if args.score in ["TF-IDF", 'tf-idf', 'tfidf']:
                    scores = [(i+1, compute_tf_idf(query, doc, docs)) for i, doc in enumerate(docs)]
                elif args.score in ['BM25', 'bm25']:
                    scores = [(i+1, compute_bm25(query, doc, docs)) for i, doc in enumerate(docs)]
                elif args.score in ['LM', 'lm']:
                    scores = [(i+1, compute_lm_dirichlet(query, doc, docs)) for i, doc in enumerate(docs)]
                elif args.score not in ["TF-IDF", "BM25", "LM"]:
                    print("Please enter a valid scoring function")
                    sys.exit(1)
                
            # sort and display search results
            scores_dict = {}
            scores_dict[args.query] = [score[0] for score in scores]
            
            # evaluate scores
            qrels_file = r'C:\Users\ammar\Desktop\Slides & Docs\Assignments + Notes\IR\qrels.xlsx'
            map_score, p_at_cutoffs_avg = evaluate(qrels_file, scores_dict)
            print(f'MAP: {map_score}')
            for c in sorted(p_at_cutoffs_avg.keys()):
                print(f'P@{c}: {p_at_cutoffs_avg[c]}')
                    
    else:
        print("Please enter a query to search")
        sys.exit(1)