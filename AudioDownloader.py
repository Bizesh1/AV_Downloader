import yt_dlp as yt
from Downloader import Downloader

class AudioDownloader(Downloader):
    def __init__(self, URL, dl_path="./Downloads/Audio_Downloads"):
        super().__init__(URL, dl_path)
    
    def build_options(self):
        options = super().build_options()
        options["format"] = "bestaudio"
        options["postprocessors"] = [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }]
        return options

    def download(self):
        super().download()


# -----Testing-----
def main():
    A = AudioDownloader("https://www.youtube.com/watch?v=Aq5WXmQQooo")
    A.download()

if __name__ == "__main__":
    main()