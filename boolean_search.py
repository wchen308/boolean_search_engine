# homework 1
# goal: tokenize, index, boolean query
# exports: 
#   student - a populated and instantiated ir4320.Student object
#   Index - a class which encapsulates the necessary logic for
#     indexing and searching a corpus of text documents


# ########################################
# first, create a student object
# ########################################

import cs525
import PorterStemmer

MY_NAME = "Weishun Chen"
MY_ANUM  = 863846968 # put your WPI numerical ID here
MY_EMAIL = "wchen5@wpi.edu"

# the COLLABORATORS list contains tuples of 2 items, the name of the helper
# and their contribution to your homework
COLLABORATORS = [ 
    ('Ruonan Feng', 'discussed with me about how to read files, how to implement and/or logic in non-programming high level language'),  
    ('Hao Yin', 'discussed with me about the effect of porterstemmer, reminded me that I should return the name of documents instead of index'),
    ]

# Set the I_AGREE_HONOR_CODE to True if you agree with the following statement
# "I do not lie, cheat or steal, or tolerate those who do."
I_AGREE_HONOR_CODE = True

# this defines the student object
student = cs525.Student(
    MY_NAME,
    MY_ANUM,
    MY_EMAIL,
    COLLABORATORS,
    I_AGREE_HONOR_CODE
    )


# ########################################
# now, write some code
# ########################################

# our index class definition will hold all logic necessary to create and search
# an index created from a directory of text files 
class Index(object):
    def __init__(self):
        # _inverted_index contains terms as keys, with the values as a list of
        # document indexes containing that term
        self._inverted_index = {}
        # _documents contains file names of documents
        self._documents = []
        # example:
        #   given the following documents:
        #     doc1 = "the dog ran"
        #     doc2 = "the cat slept"
        #   _documents = ['doc1', 'doc2']
        #   _inverted_index = {
        #      'the': [0,1],
        #      'dog': [0],
        #      'ran': [0],
        #      'cat': [1],
        #      'slept': [1]
        #      }


    # index_dir( base_path )
    # purpose: crawl through a nested directory of text files and generate an
    #   inverted index of the contents
    # preconditions: none
    # returns: num of documents indexed
    # hint: glob.glob()
    # parameters:
    #   base_path - a string containing a relative or direct path to a
    #     directory of text files to be indexed
    def index_dir(self, base_path):
        num_files_indexed = 0
        # PUT YOUR CODE HERE
        import glob
        filename = glob.glob(base_path + '*.txt')
        print(filename)
        self._documents = filename
        n_files = len(filename)

        # generate inverted index
        # read each file
        # call tokenize
        # call stemming
        # update inverted index dictionary
        # update num_files_indexed

        for i in range(n_files):
        	with open(filename[i], 'r', encoding = 'utf-8') as f:
        		text = f.read().split('\n')
        		# print(text)

        	tokens = self.tokenize(text)
        	stemmed_tokens = self.stemming(tokens)

        	for j in stemmed_tokens:
        		if (j in self._inverted_index):
        			self._inverted_index[j].append(i)
        		else:
        			self._inverted_index[j] = [i]

        	num_files_indexed = num_files_indexed + 1

        return num_files_indexed

    # tokenize( text )
    # purpose: convert a string of terms into a list of tokens.        
    # convert the string of terms in text to lower case and replace each character in text, 
    # which is not an English alphabet (a-z) and a numerical digit (0-9), with whitespace.
    # preconditions: none
    # returns: list of tokens contained within the text
    # parameters:
    #   text - a string of terms
    def tokenize(self, text):
        tokens = []
        
        # convert to lower case
        # replace non valid character with whitespace
        # split with space

        for string in text:
        	string = string.lower()

        	for character in string:
        		if not(character.isalpha() or character.isdigit()):
        			string = string.replace(character, ' ')

        	string = string.split(' ')

        	for j in string:
        		if j not in tokens:
        			tokens.append(j)

        return tokens

    # purpose: convert a string of terms into a list of tokens.        
    # convert a list of tokens to a list of stemmed tokens,     
    # preconditions: tokenize a string of terms
    # returns: list of stemmed tokens
    # parameters:
    #   tokens - a list of tokens
    def stemming(self, tokens):
        stemmed_tokens = []
        # PUT YOUR CODE HERE
        p = PorterStemmer.PorterStemmer()
        for i in range(len(tokens)):
        	# print('tokens are :' + str(tokens))
        	# print('ith token is :' + str(i))
        	stemm_result = p.stem(tokens[i], 0, len(tokens[i]) - 1)
        	stemmed_tokens.append(stemm_result)

        return stemmed_tokens
    
    # boolean_search( text )
    # purpose: searches for the terms in "text" in our corpus using logical OR or logical AND. 
    # If "text" contains only single term, search it from the inverted index. If "text" contains three terms including "or" or "and", 
    # do OR or AND search depending on the second term ("or" or "and") in the "text".  
    # preconditions: _inverted_index and _documents have been populated from
    #   the corpus.
    # returns: list of document names containing relevant search results
    # parameters:
    #   text - a string of terms
    def boolean_search(self, text):
        results = []
        # PUT YOUR CODE HERE

        results_index = []

        # term in main function is a string, make it an item in list
        text = [text]

        # tokenize, stemming the query text
        tokens = self.tokenize(text)
        stemmed_tokens = self.stemming(tokens)

        # see length of stemmed_tokens
        # if length of stemmed tokens is 1, only 1 word, look up dictionary, return value
        if (len(stemmed_tokens) == 1):
        	results_index = self._inverted_index[stemmed_tokens[0]]

        # if length of stemmed tokens is 3, look up dictionary, return value for 1 and 3, see if 2nd one is and/or
        if (len(stemmed_tokens) == 3):
            stemmed_token1 = stemmed_tokens[0]
            list1 = self._inverted_index[stemmed_token1]

            stemmed_token2 = stemmed_tokens[2]
            list2 = self._inverted_index[stemmed_token2]

        # if and, implement and algorithm / for loop each element in list1, append if element is in list2
            if stemmed_tokens[1] == 'and':
        	    results_index = list(set(list1) & set(list2))

        # if or, implement or algorithm / add 2 lists together, set(), then transfer back to list
            if stemmed_tokens[1] == 'or':
        	    results_index = list(set(list1) | set(list2))

        for i in range(len(results_index)):
        	results.append(self._documents[i])

        return results
    

# now, we'll define our main function which actually starts the indexer and
# does a few queries
def main(args):
    print(student)
    index = Index()
    print("starting indexer")
    num_files = index.index_dir('data/')
    print("indexed %d files" % num_files)
    for term in ('football', 'mike', 'sherman', 'mike OR sherman', 'mike AND sherman'):
        results = index.boolean_search(term)
        # print('term is :' + str(term))
        # print('result is :' + str(results))
        print("searching: %s -- results: %s" % (term, ", ".join(results)))

# this little helper will call main() if this file is executed from the command
# line but not call main() if this file is included as a module
if __name__ == "__main__":
    import sys
    main(sys.argv)

