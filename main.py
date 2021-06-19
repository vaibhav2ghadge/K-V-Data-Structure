

if __name__ == "__main__":

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
                print(key,value)

        except ValueError:
            print("Enter Valid Input \n")

        except NameError:
            print("Enter key in numeric form and value in double quotes example key = 100, value =\"Apple\" ")



