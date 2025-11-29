# -*- coding: utf-8 -*-
import argparse
import os
import sys

def parse_args():
    """Parse command line arguments and add positional arguments --term and --doc"""
    parser = argparse.ArgumentParser(description='Pull term and/or document information from the index')
    parser.add_argument('--term', type=str, help='Term to look up in the index')
    parser.add_argument('--doc', type=str, help='Document to look up in the index')
    return parser.parse_args()

def read_term_info(term_info_file, term):
    """"Read term info from term_info_file"""
    with open(term_info_file, 'r') as f:
        for line in f:
            line = line.strip().split('\t')
            if line[4] == term:
                term_id = int(line[0])
                offset = int(line[1])
                num_occurrences = int(line[2])
                num_docs = int(line[3])
                return {
                    'term_id': term_id,
                    'offset': offset,
                    'num_occurrences': num_occurrences,
                    'num_docs': num_docs
                }
    return None

def read_term_index(term_index_file, offset):
    """"Read term index from term_index_file"""
    with open(term_index_file, 'r') as f:
        f.seek(offset)
        line = f.readline().strip().split('\t')
        term_id = int(line[0])
        # splits the list of (doc_id, positions) pairs on the tab character '\t', and then for each pair, splits on the colon character ':' to separate the doc_id from the list of positions
        doc_id_pos_list = [(int(x.split(':')[0]), list(map(int, x.split(':')[1:]))) for x in line[1:]]
        return {
            'term_id': term_id,
            'doc_id_pos_list': doc_id_pos_list
        }

def read_doc_index(doc_index_file, doc_name):
    """""Read doc index from doc_index_file"""
    with open(doc_index_file, 'r') as f:
        for line in f:
            line = line.strip().split('\t')
            if line[0] == doc_name:
                return {
                    'doc_id': int(line[1]),
                    'num_distinct_terms': int(line[2]),
                    'total_terms': int(line[3])
                }
    return None

def read_inverted_list(term_index_file, term_info, doc_id=None):
    """""Read inverted list from term_index_file"""
    inverted_list = read_term_index(term_index_file, term_info['offset'])
    if doc_id:
        inverted_list = {doc_id: inverted_list['doc_id_pos_list']}
    return inverted_list

if __name__ == '__main__':
    # parse command line arguments
    args = parse_args()
    
    # edge case: no term or doc specified
    if args.term is None and args.doc is None:
        print('Error: Please specify either --term or --doc')
        sys.exit(1)
    
    # file names
    term_info_file = 'term_info.txt'
    term_index_file = 'term_index.txt'
    doc_index_file = 'doc_index.txt'
    
    if args.term is not None:
        term_info = read_term_info(term_info_file, args.term)
        # edge case: term not found
        if term_info is None:
            print(f'Error: Term "{args.term}" not found')
            sys.exit(1)
        
        print(f'Listing for term: {args.term}')
        print(f'TERMID: {term_info["term_id"]}')
        print(f'Number of documents containing term: {term_info["num_docs"]}')
        print(f'Term frequency in corpus: {term_info["num_occurrences"]}')
        print(f'Inverted list offset: {term_info["offset"]}')
    
    if args.doc is not None:
        doc_index = read_doc_index(doc_index_file, args.doc)
        # edge case: doc not found
        if doc_index is None:
            print(f'Error: Document "{args.doc}" not found')
            sys.exit(1)
            
        print(f'\nListing for document: {args.doc}')
        print(f'DOCID: {doc_index["doc_id"]}')
        print(f'Distinct terms: {doc_index["num_distinct_terms"]}')
        print(f'Total terms: {doc_index["total_terms"]}')