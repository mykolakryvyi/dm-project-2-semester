<<<<<<< HEAD
'''
Module with trie node and trie realization.
'''
class TrieNode():
    '''
    Class for trie node representation.
    '''
    def __init__(self):
        '''
        Initialize the parameters.
        '''
        self.value = value
        self.end = end
        self.children = {}
        self.weight = -1
 

class Trie():
    '''
    Class for trie node representation.
    '''
    def __init__(self):
        '''
        Initialize the parameters.
        '''
        self.root = TrieNode()
        self.word_list = []
 

    def formTrie(self, keys):
         
        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key) # inserting one key to the trie.
 

    def insert(self, key):
         
        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root
 
        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()
 
            node = node.children[a]
 
        node.last = True


    def search(self, key):
         
        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True
 
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
 
            node = node.children[a]
 
        return node and node.last and found
 

    def suggestionsRec(self, node, word):
         
        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            self.word_list.append(word)
 
        for a,n in node.children.items():
            self.suggestionsRec(n, word + a)
 

    def printAutoSuggestions(self, key):
         
        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root
        not_found = False
        temp_word = ''
 
        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break
 
            temp_word += a
            node = node.children[a]
 
        if not_found:
            return 0
        elif node.last and not node.children:
            return -1
 
        self.suggestionsRec(node, temp_word)
 
        for s in self.word_list:
            print(s)
        return 1
 

keys = ["hello", "dog", "hell", "cat", "a",
        "hel", "help", "helps", "helping"] # keys to form the trie structure.
key = "hel" # key for autocomplete suggestions.
status = ["Not found", "Found"]
 
t = Trie()
t.formTrie(keys)
comp = t.printAutoSuggestions(key)
 
if comp == -1:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")
 
=======
class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False
        self.weight = -1

    def add(self, item, weight) -> None:
        i = 0
        while i < len(item):
            k = item[i]
            if not k in self.next:
                node = Trie()
                self.next[k] = node
            self = self.next[k]
            if i == len(item) - 1: 
                self.end_of_word = True
                self.weight = weight
            else:
                self.end_of_word = False
            i += 1
>>>>>>> c1639826d92e5c9f684cb20a594d70b1b8e66943
