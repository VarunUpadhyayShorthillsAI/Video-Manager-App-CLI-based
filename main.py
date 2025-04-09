import json

def list_all_videos (videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def load_data():
    #loading data , obvio we need a file to load data , we will use in the read mode , otherwise in write mode , it will keep creating files
    #two types of except , finenot found or file exist error 
    try:
        #you will generally use only two methods dump and load 
        with open('youtube.txt' , 'r') as file : 
            return json.load(file)


    except FileNotFoundError:
        return []
        
   

videos = []

def main() : 
    vidoes = load_data()

    while True:

        print("\n Youtube Manager | Choose an option")
        print(" 1. List all Youtube videos")
        print(" 2. Add a youtube video")
        print(" 3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice")

        #match syntax
        match choice:
            case '1' : 
                list_all_videos(videos)
            
            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break

            #if any one enters random number

            case _:
                print("Invalid Choice")


#you can also call main like this , but 
# we keep exporting , importing things , so we use dunder __i__ type 
# main()


if __name__ == "__main__":
    main()