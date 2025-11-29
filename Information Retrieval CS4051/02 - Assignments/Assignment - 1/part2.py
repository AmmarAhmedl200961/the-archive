def build_index(doc_index_file, term_index_file, term_info_file):
    # create an empty dictionary to store term index and term info
    term_index = {}
    term_info = {}

    # process the doc index file
    with open(doc_index_file, 'r') as dindexFile:
        for line in dindexFile:
            # read each line of doc index file, and split by tab to retrieve pairs of doc_id, term_id, and positions
            pairs = line.strip().split("\t")
            doc_id = int(pairs[0])
            term_id = int(pairs[1])
            positions = [int(pos) for pos in pairs[2:]]

            # update term_index and term_info
            if term_id not in term_index:
                term_index[term_id] = {}
            if doc_id not in term_index[term_id]:
                term_index[term_id][doc_id] = []

            # extend the positions list if the doc_id already exists
            term_index[term_id][doc_id].extend(positions)
            if term_id not in term_info:
                term_info[term_id] = [0, 0]
            term_info[term_id][0] += len(positions)
            term_info[term_id][1] += 1

    # process term index file
    with open(term_index_file, 'w') as tindexFile:
        for term_id, postings in term_index.items():
            postings_list = []
            for doc_id, positions in postings.items():
                # encode delta positions to reduce the index size
                delta_positions = []
                last_position = 0
                for position in positions:
                    delta_positions.append(position - last_position)
                    last_position = position
                postings_list.append((doc_id, delta_positions))

            # sort the postings list by document id
            postings_list = sorted(postings_list, key=lambda x: x[0])

            # write the inverted index to the term index file
            line = "{}\t{}\n".format(term_id, "\t".join(["{}:{}".format(doc_id, ",".join(map(str, positions))) for doc_id, positions in postings_list]))
            tindexFile.write(line)

    # process term info file
    with open(term_info_file, 'w') as tinfoFile:
        for term_id, info in term_info.items():
            # write the term info to term info file
            line = "{}\t{}\t{}\t{}\n".format(term_id, info[0], info[1], 0)
            tinfoFile.write(line)

# build the index
if __name__=="__main__":
    build_index("doc_index.txt", "term_index.txt", "term_info.txt")
    print("Index built successfully!")
