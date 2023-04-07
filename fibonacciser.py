k = int(input("Enter the lowest value: "))   # taking input from user > 0
n = int(input("Enter the highest value: "))  # taking input from user > 50

a = 0     # initialization of series
b = 1

while b <= n:     # checks for highest value
    if b >= k:    # checks for lowest value
        print(b, end=" ")
    a, b = b, a + b   # swapping the new values
    
 output:
 1 1 2 3 5 8 13 21 34
