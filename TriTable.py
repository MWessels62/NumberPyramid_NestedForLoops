#Task 15
#Compulsory task
# Write a program that uses nested For-loops to create a number pyramid.

for i in range(1,10):
    for j in range(1,i+1): #each row has entries equivalent to the starting number for that row, therefore we refer to i+1
        print(str(j*i),end="   ")   # The 'end' function allows me to print each iteration on the same row
    print("")                       #Makes new row print on a new line