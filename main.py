# Definition and Usage
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

# The enumerate() function adds a counter as the key of the enumerate object.

# Syntax
# enumerate(iterable, start)


# x = ('Man' , 'Woman' , 'Others')
# y = enumerate(x)
# print(y)
# new_format = list(y)
# print(new_format)



#to open any file (will give error)
# file = open('test.py' )

#write mode autmatically create file , if there isn't
file = open('youtube.txt' , 'w')

try:
    file.write('Writing in the file for testing purpose')
finally:
    file.close()