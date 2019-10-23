#Chapter 4 Challenge 1
#
# Write a program that counts for the user. Let the user enter the starting 
# number, the ending number, and the amount by which to count.
#
# Prompt user for starting number, ending number and stepping amount
# Create a for loop that uses the varibles that it just got from the prompt
# for loop iterates using the information until it ends


# initiate program
print("let me count for you!")

# get values from user
start = int(input("What number do you want to start with? "))
end = int(input("What number do you want to end at? "))
step = int(input("What do you want to step by? "))

# initiate for loop
for i in range(start, end, step):
    print(i, end=" \n")




input("\n\nPress the enter key to exit.\n")



