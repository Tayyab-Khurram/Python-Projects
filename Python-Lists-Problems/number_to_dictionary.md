#### Convert the user input in numbers to words
```python
mappings = {
    1: 'one', 2: 'two', 3: 'three',
    4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'
}

num = int(input('Input: '))
number = [int(n) for n in str(num)] # [7,8,6] breaking the number as individual items in a list
for each in number:
    print(mappings.get(each), end=' ') # get the value from the dictionary
```
