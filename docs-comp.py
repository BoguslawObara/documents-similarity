import gensim
# print(dir(gensim))

# create some documents
raw_documents = ["I'm taking the show on the road.",
                "My socks are a force multiplier.",
                "I am the barber who cuts everyone's hair who doesn't cut their own.",
                "Legend has it that the mind is a mad monkey.",
                "I make my own fun."]
# print("Number of documents:",len(raw_documents))

# document will now be a list of tokens
from nltk.tokenize import word_tokenize
gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in raw_documents]
# print(gen_docs)

# create a dictionary from a list of documents;  dictionary maps every word to a number
dictionary = gensim.corpora.Dictionary(gen_docs)
# print(dictionary[5])
# print(dictionary.token2id['road'])
# print("Number of words in dictionary:",len(dictionary))
# for i in range(len(dictionary)):
#     print(i, dictionary[i])

# create a corpus = a list of bags of words
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
# print(corpus)

# create a tf-idf model from the corpus
tf_idf = gensim.models.TfidfModel(corpus)
# print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
# print(s)

# similarity measure object in tf-idf space
sims = gensim.similarities.Similarity('./',tf_idf[corpus],
                                      num_features=len(dictionary))
# print(sims)
# print(type(sims))

# query document and convert it to tf-idf
query_doc = [w.lower() for w in word_tokenize("Socks are a force for good.")]
# print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
# print(query_doc_bow)
query_doc_tf_idf = tf_idf[query_doc_bow]
# print(query_doc_tf_idf)

# array of document similarities to query
sims[query_doc_tf_idf]