import subprocess
from downloader import *


def inazuma1():
    video = video_downloader("https://youtu.be/zif0Lmhrivc", "kazuha")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("kazuha.mp4", shell=True)


def inazuma2():
    video = video_downloader("https://youtu.be/mvrW4aKwAXw", "raiden")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("raiden.mp4", shell=True)


def inazuma3():
    video = video_downloader("https://youtu.be/NHEE_-87mNE", "balladeer")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("balladeer.mp4", shell=True)


def inazuma4():
    video = video_downloader("https://youtu.be/RPAoXtU5Kgg", "sara")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("sara.mp4", shell=True)
