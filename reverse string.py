string = input("Enter a word:")

reverse = ("")

for i in string:
    reverse = i + reverse

print("Here is your word backwards:", reverse)