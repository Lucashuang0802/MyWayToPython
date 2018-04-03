
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

    def __repr__(self):
        if not self.children: return ""
        chr_arr = [chr(level + ord('a')) for level in range(len(self.children)) if self.children[level]]
        return "".join(chr_arr)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def display(self):
        res = []
        self.display_helper(res, [], self.root)
        return res

    # simple recursion
    def display_helper_simple(self, res, temp, node):
        if node.isEndOfWord:
            res.append(temp)

        for level in range(len(node.children)):
            if not node.children[level]: continue
            self.display_helper(res, temp + chr(level + ord('a')), node.children[level])

    # backtrack
    def display_helper(self, res, temp, node):
        if node.isEndOfWord:
            res.append("".join(list(temp)))

        for level in range(len(node.children)):
            if not node.children[level]: continue
            temp.append(chr(level + ord('a')))
            self.display_helper(res, temp, node.children[level])
            del temp[-1]

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl != None and pCrawl.isEndOfWord

if __name__ == '__main__':
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","answer","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for key in keys:
        t.insert(key)
 
    # Search for different keys
    print("{} ---- {}".format("a",output[t.search("a")]))
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))

    print("display the trie {}".format(t.display()))