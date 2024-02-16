from pytube import YouTube
import os

def downloadVideo(videoUrl):
    path = os.path.expanduser('~/tawheed/Downloads/Youtube-videos')
    try:
        YouTube(videoUrl).streams.get_highest_resolution().download(path)
        # When you request .streams, Pytube returns a list of available streams
        #  for that particular video. These streams represent different formats
        #  and qualities in which the video is available for download. 
        # The .first() method simply selects the first stream from this list, 
        # typically in the highest resolution available, which is usually the 
        # best quality stream.
        print(f"downloaded video to {path}")        
    except:
        print("Connection Error")

