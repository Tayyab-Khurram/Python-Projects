real = []
print ('Enter some numbers in the list: (press "-1" to exit)')
while True:
    x = int(input())
    if x == -1:
        break
    real.append(x)

even_nums = []
odd_nums = []

for num in real:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

print ('Even Numbers: ')
print (even_nums)

print ('Odd Numbers: ')
print (odd_nums)
