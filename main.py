from core.keyvalue import KeyValueStorage
from core.trie import TrieNode

if __name__ == "__main__":

    key_value_storage = KeyValueStorage(10,TrieNode("*"))
    
    while True:
        print("1. Insert \n")
        print("2. Retrive \n")
        print("3. Display current state \n")
        print("Choice (^C to exit): ")
        try:
            choice = int(input())
            if choice==1:
                print("Enter key: ")
                key = int(input())
                print("\nEnter value: ")
                value = input()
                key_value_storage.put(key,value)
            elif choice ==2:
                print("\nEnter key: ")
                key = int(input())
                print("Retrieved value: ", key_value_storage.get(key))

        except ValueError:
            print("Enter Valid Input \n")

        except NameError:
            print("Enter key in numeric form and value in double quotes example key = 100, value =\"Apple\" ")



