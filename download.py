from pytube import YouTube


def downloadVideo(videoUrl):
    try:
        YouTube(videoUrl).streams.first().download()
        print("downloaded video ")
    except:
        print("Connection Error")

