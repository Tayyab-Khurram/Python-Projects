my_list = []
for i in range(5):
    print(f'Enter the {i}th value : ')
    x = int(input())
    my_list.append(x)

temp = my_list[0]
my_list[0] = my_list[len(my_list)-1]
my_list[len(my_list)-1] = temp

print(f'List after updation : {my_list}')
