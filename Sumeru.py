import subprocess
from downloader import *


def sumeru1():
    video = video_downloader("https://youtu.be/oSSCRUmaquo", "tignari")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("tignari.mp4", shell=True)


def sumeru2():
    video = video_downloader("https://youtu.be/dpZhGzZ3hNc", "nahida")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("nahida.mp4", shell=True)


def sumeru3():
    video = video_downloader("https://youtu.be/J9WuPBOC_S8", "syno")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("syno.mp4", shell=True)


def sumeru4():
    video = video_downloader("https://youtu.be/P08q5Y7r9Z4", "dori")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("dori.mp4", shell=True)
