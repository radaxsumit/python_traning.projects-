# Create a code to reverse the words of a string. Example: My name is SUMIT -> SUMIT is name My

string = input("Enter the string: ")
string = string.split(" ")
print(" ".join(string[::-1]))