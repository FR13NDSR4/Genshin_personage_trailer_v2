from plyer import notification


def start_download():
    notification.notify(title="Genshin", message="Please wait, starting download",
                        app_icon="download.ico", timeout=1)


def download_complete():
    notification.notify(title="Genshin", message="Download complete",
                        app_icon="play.ico", timeout=5)
