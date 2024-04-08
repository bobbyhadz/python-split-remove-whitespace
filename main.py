# Split string and remove whitespace in Python

my_str = 'bobby,   hadz,   com'

my_list = [word.strip() for word in my_str.split(',')]
print(my_list)  # 👉️ ['bobby', 'hadz', 'com']