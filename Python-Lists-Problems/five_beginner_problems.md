
1. **Merging Two Lists**:
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]
```

2. **Check for Empty List**:
```python
def check_empty(my_list):
    if len(my_list) == 0:
        return True
    return False

my_list = []
result = check_empty(my_list)
print(result)  # Output: True
```

3. **Square Each Element**:
```python
numbers = [1, 2, 3, 4, 5]
squared_list = []
for num in numbers:
    squared_list.append(num ** 2)
    
print(squared_list)  # Output: [1, 4, 9, 16, 25]
```

4. **Concatenate Elements**:
```python
words = ["Hello ", "world", "!"]
new_word = ''
for word in words:
    new_word += word
print(new_word)  # Output: Hello world!
```

5. **Find Even Numbers**:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [num for num in numbers if num % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8]
```

6. **Sum of Even Numbers:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for num in numbers:
    if num % 2 == 0:
        sum += num
print(sum)
```

7. **Remove Specific Element:**
```python
numbers = [1, 2, 3, 4, 5]
element_to_remove = 3
numbers.remove(element_to_remove)
print(numbers)
```

9. **Find Common Elements:**
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
final_list = [l1 for l1 in list1 if l1 in list2]
print(final_list)
```

10. **Check for Sublist:**
```python
def find_sublist(main_list, sub_list):
    final = [each_item for each_item in sub_list if each_item in main_list]
    if final == sub_list:
        return True
    return False
    
main_list = [1, 2, 3, 44, 5, 6, 7]
sub_list = [3, 44, 5]    
print(find_sublist(main_list, sub_list))
```
    
10. **Find the Second Largest Number:**
```python
numbers = [10, 20, 4, 45, 99, 6]
# print(sorted(numbers)[-2])
numbers.remove(max(numbers))
print(max(numbers))
```
