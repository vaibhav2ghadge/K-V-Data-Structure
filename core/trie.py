from core.valuemetadata import ValueMetaDataNode
class TrieNode(object):
    """
        Trie object search by number in its childeren 
        for each object it store value meta data
    """
    
    def __init__(self, number):
        self.number = number
        self.children = [None for i in range(0,10)]
        self.value = None
    

    def add(self,key,value):
        """
        Add value in trie
        In each trie node check the given key  present
        if its not present then create the object do same for remaining key
        and store metadata at end of key object
        """
        node = None
        for digit in key:
            child = self.children[ord(digit)-ord('0')]
            if(child==None):
                self.children[ord(digit)-ord('0')] = TrieNode(digit)
            node = self.children[ord(digit)-ord('0')]
        
        node.value = ValueMetaDataNode(value)


    def get(root,key):
        """
            return the value for key
        """
        node = root
        for digit in key:
            node = node.children[ord(digit)-ord('0')]
            if(node==None):
                return None
        return node.value.value

