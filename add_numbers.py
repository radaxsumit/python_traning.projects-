# Create a function to print add of "n" numbers

def addnumbers(n):
    answer = 0
    while n > 0:
        answer += n
        n -= 1
    return answer

sum = int(input("Enter the number: "))
print(addnumbers(sum))