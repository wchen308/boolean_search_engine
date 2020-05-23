# boolean_search_engine
This is a practice to build a boolean search engine including tokenization, stemming, indexing and query components. 

## Query
The query component searchs for the terms in the string text in the inverted index. For example, if the boolean search is called with 'mike or sherman', the return value should be a list of documents that include 'mike' or 'sherman'. If the boolean_search is called with 'mike and sherman', then the return value should be a list of documents that include 'mike' and 'sherman'.

## Indexing
The indexing component crawl through a nested directory of text files and generate an inverted index of the contents of these files. For example, in this inverted index, given a term, we can know which documents include this term.

## Tokenization
The tokenization component takes a raw string and convert it to a list of valid tokens. If an element is not an English letter nor a number, then it is considered as a delimiter. For example, "http://www.cnn33.com" should result in "http", "www", "cnn33", "com".

## Stemming
The stemming component takes a list of tokens and convert to a list of stemmed tokens using PorterStemmer, so that we record each word using its root form. For example, a token "important" will become "import" after stemming.
