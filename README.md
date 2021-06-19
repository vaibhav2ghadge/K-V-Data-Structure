# K-V Data Structure

Store numeric key and string value in the data structure.
## Design Choices / Implementation
- To retrieve any key's value in O(1) we can directly store the key in the index of the list because our key is numeric so if the key is 10 then we can store it to index number 10.  By this implementation, we can get any value in O(1). for example, we have a list of 10 lengths, bucket = [None,None,None,None,None,None,None,None,None,None] initially they all are none if we want to store key=9 and value = "Maserati" we can store directly to 9 index. bucket[9] = "Maserati" so list after inserting 9 key is [None, None,None, None,None, None,None, None,"Maserati", None] and if just get 9th index bucket[9] we can get value Maserati in O(1).
- Trade of this implementation is that we have to create a list before inserting value so if we create a list of 100 length then we can only store keys less than 100 we cant store keys greater than 100 because of fixed list size to tackle this problem we can create a big list but then this way maybe our storage not be get fully unutilized like suppose we create a list of 1 Million of length and if we only storing keys less than 100 then our lots of storage get waisted.
- To solve this problem we can compromise some time complexity and save some space, another option is that we can store the keys that are greater than 100(length of the list) in another data structure have decided to store it in trie data structure so we can retire and store any key in O(length(Key)) it's more near to O(1) other option is to balanced binary search tree but it has a time complexity of O(log(N)) for insertion and retrieval so have decided to store it to the trie data structure. in this implementation if any key is greater than list size its get stored in trie.
by this we can get most of the keys in O(1) and the remaining keys can we get in O(length(key))
- Have made this list size configurable in makefile if your sure your keys less than some number then you can initialize that size of list there by default its 1000 if any key is less than 1000 its retrieval and store time complexity is O(1) and keys greater than 1000 retrieval and store time complexity is O(length(key)). so end-user has the choice to configure his list by this he is ready to get everything in O(1) by compromising space and vice-versa   

## How To Run / Installation
- Make sure you have python2.7 installed
- ``````

