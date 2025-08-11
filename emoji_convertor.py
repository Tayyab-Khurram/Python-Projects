emojis_dictionary = {
    ':)': '🙂', ':(': '🙁', ':D': '😃',
    ':P': '😛', ';)': '😉', 'XD': '😆',
    'B)': '😎', ':/': '😕', ':|': '😐',
    '<3': '❤️', '</3': '💔', ':*': '😘',
    '>:(': '😠', ':o': '😮', ':O': '😲',
    ':$': '😳', ':@': '😡', ':^': '😤',
    '8)': '😎', ':]': '😊', ':^)': '😊',
    ':-)': '🙂', ':-(': '🙁', ':-D': '😃',
    ':-P': '😛', ':-O': '😲', ':-|': '😐',
    ':-*': '😘', ':-$': '😳', ':-@': '😡',
    ':-/': '😕', ':-]': '😊', ':-^': '😊',
    ':-S': '😖', ':-X': '🤐', ':-8': '😳',
    ':-V': '😖', ':-)': '🙂', ':-(': '🙁'
}


def convert_emoji(input_string):
    broken_string = input_string.split(' ')
    
    output_string = ''
    for broken in broken_string:
        ans = emojis_dictionary.get(broken, broken)
        output_string += ans + " "
        
    return '> ' + output_string


while(1):
    print("To exit type 'q'")
    input_string = input("Enter any string with keyboard emojis: ").lower().strip()
    if input_string == 'q':
        break
    else:
        print(convert_emoji(input_string))
