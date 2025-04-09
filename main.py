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
# file = open('youtube.txt' , 'w')

# try:
#     file.write('Writing in the file for testing purpose')
# finally:
#     file.close()

# try , finally -> for error handling || 
#another syntax for files ,

# with open('youtube.txt' , 'w') as file:
#     file.write('just another syntax , it automatically take cares of the closing , easy syntax')

#functionality so that user keep asking questions :
while True:
    print("\n Youtube Manager | Choose an option")
    print(" 1. List all Youtube videos")
    print(" 2. Add a youtube video")
    print(" 3. Update a youtube video details")
    print("4. Delete a youtube video")
    print("5. Exit the app")
    choice = input("Enter your choice")

    