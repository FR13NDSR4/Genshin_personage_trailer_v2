import subprocess
from downloader import *


def li_yue1():
    video = video_downloader("https://youtu.be/_ndVJlqBYLY", "cici")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("cici.mp4", shell=True)


def li_yue2():
    video = video_downloader("https://youtu.be/sjozpa9DsZU", "xiao")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("xiao.mp4", shell=True)


def li_yue3():
    video = video_downloader("https://youtu.be/qrH9vMZBwAk", "hutao")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("hutao.mp4", shell=True)


def li_yue4():
    video = video_downloader("https://youtu.be/4oBpaBEMBIM", "zhongli")
    print(f'"{video}" downloaded successfully!!')
    subprocess.call("zhongli.mp4", shell=True)
