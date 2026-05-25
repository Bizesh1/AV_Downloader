import os
from YTSearch import YTSearch 
from AudioDownloader import AudioDownloader
from VideoDownloader import VideoDownloader

class App:
    def __init__(self):
        pass

    def main_menu(self):
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print(f"{'Audio and Video Downloader':^62}")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("1. Download Audio via Link.")
        print("2. Download Audio via YouTube Search.")
        print("3. Download Video via Link.")
        print("4. Download Video via YouTube Search.")
        print("5. Exit.")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        
    def download_method(self):
        while True:
            try:
                self.download_choice = int(input("\nChoose One Option: "))
                if self.download_choice <= 6 and self.download_choice >= 1:
                    return self.download_choice
                else:
                    print("Choose from 1-6 please!")
            except:
                ValueError, TypeError
                print("Oops! You didnt enter a Number.")

    def run(self, choice):
        match(choice):
            case 1:
                while True:
                    Link = input("Enter Audio Link: ")
                    Audio = AudioDownloader(Link)
                    Audio.download()
            
            case 2:
                query = input("Search Audio on YouTube: ")
                search = YTSearch(query)
                search.search()
                search.display_search_results()
                Link = search.user_choice()
                Audio = AudioDownloader(Link)
                Audio.download()
            
            case 3:
                Link = input("Enter Video Link: ")
                Video = VideoDownloader(Link)
                Video.download()

            case 4:
                query = input("Search Video on YouTube: ")
                search = YTSearch(query)
                search.search()
                search.display_search_results()
                Link = search.user_choice()
                Video = VideoDownloader(Link)
                Video.download()

            case 5:
                pass
                
                

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        clear_screen()
        Main = App()
        Main.main_menu()
        D_Method = Main.download_method()
        if D_Method == 5:
            clear_screen()
            print("Goodbye, have a nice day!")
            break
        clear_screen()
        Main.run(D_Method)
        os.system("pause")

if __name__ == "__main__":
    main()