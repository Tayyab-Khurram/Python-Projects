my_list = []
for i in range(5):
    print(f'Enter the {i}th value : ')
    x = int(input())
    my_list.append(x)

index1 = int(input('Enter the first index : '))
index2 = int(input('Enter the second index : '))

temp = my_list[index2]
my_list[index2] = my_list[index1]
my_list[index1] = temp

print(f'\nList after swapping the {index1}th value with {index2}th value')
print(my_list)
