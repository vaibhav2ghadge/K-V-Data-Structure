from core.trie import TrieNode
from core.valuemetadata import ValueMetaDataNode

class KeyValueStorage:
    def __init__(self,no_of_blocks,trie_node):
        self.no_of_blocks = no_of_blocks
        self.blocks = [None for i in range(0,no_of_blocks)]
        self.trie = trie_node

    def put(self,key,value):
        """
            put value in given key if length less than length of block
            else put in trie
        """

        if key< self.no_of_blocks:
            self.blocks[key] = ValueMetaDataNode(value)
        else:
            self.trie.add(self.trie,str(key),value)


    def get(self,key):
        """
            get value from given key if key is less than no of blocks then it will return index of that block
            if key is greater than no of blocks then it will look into the trie
            return the value if present else return None
        """

        if key< self.no_of_blocks:
            if(self.blocks[key]==None):
                return None
            return self.blocks[key].value
        
        else:
            return self.trie.get(self.trie,str(key))

