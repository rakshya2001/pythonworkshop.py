# N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in
# the basket. How many apples will each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the question above.
N= int(input("Enter the number of students:"))
K= int(input("Enter the number of apples:"))
D= K/N
R= K//N
print(f'the number of apple got by the students are {D}')
print(f'the apples left in the basket is{R}')