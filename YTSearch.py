import yt_dlp as yt

class YTSearch:
    def __init__(self, query=None, max_result = 5):

        if query is None:
            query = input("Search in Youtube: ")

        self.query = query
        self.max_result = max_result
        self.results = []

    def search(self):
        options = {
            "quiet": True,
            "extract_flat": True,
            "noplaylist": True
    }

        with yt.YoutubeDL(options) as ydl:
            self.info = ydl.extract_info(f"ytsearch{self.max_result}:{self.query}", download= False)
            self.results = []

            for entry in self.info["entries"]:
                self.results.append({
                    "Title" : entry.get("title"),
                    "Duration" : f"{(entry.get("duration") / 60) : .2f} Minutes",
                    "Views" : f"{entry.get("view_count"):,}",  
                    "URL" : entry.get("url")
            })

    def display_search_results(self):     
        count = 1
        print("\n")
        for result in self.results:
            print("-"*109)
            print(f"Search no. {count}")
            print("-------------")

            for key, value in result.items():
                print(f"{key}: {value}")
            print("-"*109)
            print("\n")
            count +=1


    def user_choice(self):
        while True:
            try:
                choice = int(input(f"Enter your choice (1 - {self.max_result}): "))
                if 1 <= choice <= self.max_result:

                    Usr_choice_URL = self.results[choice - 1].get("URL")

                    print("\n")
                    print(f"You chose: {self.results[choice - 1].get("Title")}")
                    print("\n")

                    return Usr_choice_URL
                else:
                    print(f"Choose from 1-{self.max_result} please!\n")
            
            except:
                ValueError, TypeError, Exception
                print("Oops! You didnt enter a Number.\n")





#---- Testing ----
# def main():
#    query = input("Search YouTube: ")
#    A = YTSearch(query)
#    A.search()
#    A.display_search_results()
#    A.user_choice()

# if __name__ == "__main__":
#    main()


