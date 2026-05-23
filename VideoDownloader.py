import yt_dlp as yt
from Downloader import Downloader

class VideoDownloader(Downloader):
    def __init__(self, URL, dl_path="./Downloads/Video_Downloads"):
        super().__init__(URL, dl_path)
    
    def build_options(self):
        options = super().build_options()
        options["format"] = "bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best"
        options["merge_output_format"] = "mp4"
        return options

    def download(self):
        super().download()


# -----Testing-----
# def main():
#     A = VideoDownloader("https://www.youtube.com/watch?v=Aq5WXmQQooo")
#     A.download()

# if __name__ == "__main__":
#     main()