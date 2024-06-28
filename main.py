from pytube import YouTube

url = "https://www.youtube.com/watch?v=pX0jXyuj7QE"
yt = YouTube(url)  # Create a YouTube object with the URL
stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
stream.download()  # Download the stream
