from pytube import YouTube


def download_video(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Display video title and author
        print(f"Title: {yt.title}")
        print(f"Author: {yt.author}")

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video to the current directory
        print("Downloading...")
        stream.download()
        print("Download complete!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
