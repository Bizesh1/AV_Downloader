
import yt_dlp as yt
from abc import ABC, abstractmethod

class Downloader(ABC):
    def __init__(self, URL, dl_path= "/downloads"):
        self.URL = URL
        self.download_path = dl_path

    @abstractmethod
    def build_options(self):  # to be overridden
        options = {
            "quiet" : True,
            "outtmpl": f"{self.download_path}/%(title)s.%(ext)s",
            "noplaylist" : True
        }
        return options
        
    def download(self): 
        with yt.YoutubeDL(self.build_options()) as ydl:
            ydl.download([self.URL])