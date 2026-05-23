
import yt_dlp as yt
from abc import ABC, abstractmethod

class Downloader(ABC):
    def __init__(self, URL, dl_path):
        self.URL = URL
        self.download_path = dl_path

    @abstractmethod
    def build_options(self):  # to be overridden
        options = {
            "quiet" : True,
            "outtmpl": "%(title)s.%(ext)s",
            "paths" : {"home":self.download_path},
            "noplaylist" : True
        }
        return options
        
    def download(self): 
        with yt.YoutubeDL(self.build_options()) as ydl:
            ydl.download([self.URL])
            print("Download Complete.")