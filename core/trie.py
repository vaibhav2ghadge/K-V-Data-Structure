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
    

    def add(self,root,key,value):
        """
        Add value in trie
        In each trie node check the given key  present
        if its not present then create the object do same for remaining key
        and store metadata at end of key object
        """
        node = root
        for digit in key:
            child = node.children[ord(digit)-ord('0')]
            if(child==None):
                node.children[ord(digit)-ord('0')] = TrieNode(digit)
            node = node.children[ord(digit)-ord('0')]
        
        node.value = ValueMetaDataNode(value)


    def get(self,root,key):
        """
            return the value for key
        """
        node = root
        for digit in key:
            node = node.children[ord(digit)-ord('0')]
            if(node==None):
                return None
        return node.value.value

    def getAllKeyValuePair(self,root,key):
        """
            Return list of key value pair recursively
            return [(key,value)]
        """

        if root==None:
            return []
        
        node = root
        result = []

        for index,child in enumerate(node.children):
            if(child!=None):
                if(child.value!=None):
                    result.append((key+str(index),child.value.value))
                
                result += self.getAllKeyValuePair(child,key+str(index))

        return result

        