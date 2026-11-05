#TF-IDF of a word in a set of documents
import math

documents = ["The cat was sitting on the mat",
             "I was bored of College life",
             "Calculus is his favourite subject"]
docs = [d.lower().split() for d in documents]

word = input("Enter the word to be checked: ").lower().strip()

#IDF = log(total no. of documents / no. of documents containing the word)
containing = sum(word in d for d in docs)
if containing == 0:
    print(f"'{word}' is not present in any document")
else:
    idf = math.log(len(docs) / containing)
    for i, d in enumerate(docs, 1):
        #TF = no. of occurrences in that document / total no. of words in that document
        tf = d.count(word) / len(d)
        print(f"Document {i}: TF = {tf:.4f}, IDF = {idf:.4f}, TF-IDF = {tf * idf:.4f}")