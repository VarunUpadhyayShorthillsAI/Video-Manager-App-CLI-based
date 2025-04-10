import json

def list_all_videos(videos):
    print('\n') 
    print('*'*70)

    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']}")

    print('\n') 
    print('*'*70)

def add_video(videos):
    name = input("Enter video name:")
    time = input("Enter video time:")

    # format : [{name:"" , time:""} , {}]
    videos.append({'name':name , 'time': time})
    save_data_helper(videos  )

def update_video(videos):
    # First we will ask which video you want to update
    # So we have to show the videos list and pass the videos to list_all_videos
    list_all_videos(videos)
    
    index = int(input("Enter the index for the video you want to update: "))
    
    if index < 1 or index > len(videos):
        print("Enter a valid index >>>")
    else:
        name = input("Enter name of the video :")
        time = input("Enter duration for the video:")
    #you got the time and name , now update the video based on the index 
        videos[index -1] = {'name':name , 'time':time}
        save_data_helper(videos) 

def delete_video(videos):
    #to delete a video show the list and then we will choose index , and then proceed
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))


    if index < 1 or index > len(videos):
            print("Enter a valid index >>>")
    else:
        del[videos[index-1]]
        #del will return you modified list or original list??
        save_data_helper(videos) 
        

def load_data():
    #loading data , obvio we need a file to load data , we will use in the read mode , otherwise in write mode , it will keep creating files
    #two types of except , finenot found or file exist error 
    try:
        #you will generally use only two methods dump and load 
        with open('youtube.txt' , 'r') as file : 
            test = json.load(file)
            # #this is a list , but list in json
            # print(type (test))
            return test


    except FileNotFoundError:
        return []
        
#for saving data 
def save_data_helper(videos):
    with open('youtube.txt'  , 'w') as file:
        #kya likhna hai , kahaan par likhna hai 
        json.dump(videos , file)


videos = []

def main() : 
    videos = load_data()
    print('\n') 
    print('*'*70)
    while True:
        
        print("\n Youtube Manager | Choose an option")
        print("1. List all Youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice : \n")
        
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

        print('\n') 
        print('*'*70)
#you can also call main like this , but 
# we keep exporting , importing things , so we use dunder __i__ type 
# main()


if __name__ == "__main__":
    main()



# you have made tuples from the list , but you have this type of data this time:
# (1 , {'name': 'chai' , 'time': '2min'})
# (2 , {'name': 'code' , 'time': '3min'})
# for i in enumerate (list , start = 1):
#     print(i)


# obviously the count is your 'i' but in the right side you have the video
#     print(f"{i} , {video['name]}")