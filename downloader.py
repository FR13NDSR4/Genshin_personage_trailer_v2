from pytube import YouTube
from Notification import *


def video_downloader(video_url, filename):
    start_download()
    my_video = YouTube(video_url)
    YouTube(video_url).streams.filter(res="720p").first().download(filename=filename + ".mp4")
    download_complete()
    return my_video.title
