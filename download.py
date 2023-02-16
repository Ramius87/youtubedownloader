from pytube import YouTube

def download_video(link):
    # Create Youtube-Instance
    yt = YouTube(link)

    #print(yt.streams.filter(progressive=True))

    #ys = yt.streams.get_highest_resolution()
    ys = yt.streams.get_by_itag('140')

    ys.download()
    #ys.download('location')

def get_video_information(link):
    yt = YouTube(link)
    #print(yt.streams)
    return str(yt.title + "\n" + str(yt.length) + " seconds")


#printing all the available streams
#print(yt.streams)
#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(only_video=True))

