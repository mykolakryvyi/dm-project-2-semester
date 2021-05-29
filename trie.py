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