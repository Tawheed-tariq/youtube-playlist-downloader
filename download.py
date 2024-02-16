from pytube import YouTube
import os

def downloadVideo(videoUrl, number):
    path = os.path.expanduser('~/tawheed/Downloads/Youtube-videos')
    count = number
    try:
        filename = str(count)+ "." + YouTube(videoUrl).streams.get_highest_resolution().default_filename
        YouTube(videoUrl).streams.get_highest_resolution().download(path, filename)
        # When you request .streams, Pytube returns a list of available streams
        #  for that particular video. These streams represent different formats
        #  and qualities in which the video is available for download. 
        # The .first() method simply selects the first stream from this list, 
        # typically in the highest resolution available, which is usually the 
        # best quality stream.
        print(f"downloaded video number {count} to {path}")
    except:
        print(f"Error in downloading video number {count}")

