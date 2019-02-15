
options = ["1. ", "2. ", "3. "]

#used to display options
for option in options:
    print(option)


#used to read user input and porcess response
x = int(input("Enter the number associated with your desired response: "))
for idx, val in enumerate(options):
    if idx == x-1:
        return idx
