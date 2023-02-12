from downloader import *
import subprocess


def mondstat1():
    video = video_downloader("https://youtu.be/3VtfVPCbNzk", "fishl")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("fishl.mp4", shell=True)


def mondstat2():
    video = video_downloader("https://youtu.be/QUioSVENXcI", "mona")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("mona.mp4", shell=True)


def mondstat3():
    video = video_downloader("https://youtu.be/t6BZjmGpq40", "venti")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("venti.mp4", shell=True)


def mondstat4():
    video = video_downloader("https://youtu.be/C_duDk5e8yU", "klee")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("klee.mp4", shell=True)