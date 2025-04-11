import json

# Function to display all videos with index, name, and duration
def list_all_videos(videos):
    print('\n') 
    print('*' * 70)

    # Using enumerate to show each video with a 1-based index
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']}")

    print('\n') 
    print('*' * 70)

# Function to add a new video
def add_video(videos):
    # Ask user for name and duration of video
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    # Append a new video dictionary to the list
    videos.append({'name': name, 'time': time})

    # Save the updated data
    save_data_helper(videos)

# Function to update an existing video
def update_video(videos):
    # Display current list of videos
    list_all_videos(videos)

    # Ask for the index of the video to update
    index = int(input("Enter the index for the video you want to update: "))

    # Validate the index
    if index < 1 or index > len(videos):
        print("Enter a valid index >>>")
    else:
        # Ask for updated name and duration
        name = input("Enter name of the video: ")
        time = input("Enter duration for the video: ")

        # Update the video at the given index (subtracting 1 for 0-based index)
        videos[index - 1] = {'name': name, 'time': time}

        # Save the updated data
        save_data_helper(videos)

# Function to delete a video from the list
def delete_video(videos):
    # Show the list before asking for index
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    # Validate the index
    if index < 1 or index > len(videos):
        print("Enter a valid index >>>")
    else:
        # Delete the video from the list
        del videos[index - 1]

        # Save the updated data
        save_data_helper(videos)

# Load video data from a file
def load_data():
    # Attempt to open the file in read mode and load JSON data
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        # If file not found, return an empty list
        return []

# Save video data to a file
def save_data_helper(videos):
    # Open the file in write mode and dump the list as JSON
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

# Main app loop
def main():
    videos = load_data()  # Load existing data
    print('\n') 
    print('*' * 70)

    while True:
        # Menu options
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your choice: \n")

        # Match-case for cleaner branching (Python 3.10+)
        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break  # Exit the loop and program

            case _:
                print("Invalid Choice")  # Catch all other inputs

        print('\n') 
        print('*' * 70)

# Standard Python entry-point guard
if __name__ == "__main__":
    main()