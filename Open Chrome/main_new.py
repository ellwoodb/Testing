import time
import webbrowser
from os import name, system

# system("color 08")
# system("cls")


def main():
    website_input = input("Please enter the website you want to open:\n")

    global search
    search = website_input.split(" ")

    keywords = " ".join(search[1:])

    global website
    website = search[0]

    if website.lower() == "youtube" or website.lower() == "video":
        websites.youtube(keywords)

    elif website.lower() == "music" or website.lower() == "apple music":
        websites.apple_music(keywords)

    elif website.lower() == "reddit":
        websites.reddit(keywords)

    elif website.lower() == "twitter":
        websites.twitter(keywords)

    elif website.lower() == "pip" or website.lower() == "python":
        websites.pip(keywords)

    elif website.lower() == "google" or website.lower() == "search":
        websites.google(keywords)

    else:
        print("Couldn't find that website.")

    time.sleep(3)
    system("cls")
    main()


class websites():
    def __init__(self):
        pass

    def youtube(args=None):
        if not args:
            print(f"Opening `{website}`...")
            webbrowser.open("https://youtube.com")

        else:
            print(f"Opening `{website}` with search `{args}`...")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={args}")

    def apple_music(args=None):
        if not args:
            print(f"Opening `{website}`...")
            webbrowser.open("https://music.apple.com/de/")

        else:
            print(f"Opening `{website}` with search `{args}`...")
            webbrowser.open(
                f"https://music.apple.com/de/search?term={args}")

    def reddit(args=None):
        if not args:
            print(f"Opening `{website}`...")
            webbrowser.open("https://www.reddit.com/")

        else:
            print(f"Opening `{website}` with search `{args}`...")
            webbrowser.open(
                f"https://www.reddit.com/search/?q={args}")

    def twitter(args=None):
        if not args:
            print(f"Opening `{website}`...")
            webbrowser.open("https://twitter.com/")

        else:
            print(f"Opening `{website}` with search `{args}`...")
            webbrowser.open(
                f"https://twitter.com/search?q={args}&src=typed_query")

    def pip(args=None):
        if not args:
            print(f"Opening `{website}`...")
            webbrowser.open("https://pypi.org/")

        else:
            print(f"Opening `{website}` with search `{args}`...")
            webbrowser.open(
                f"https://pypi.org/search/?q={args}")

    def google(args=None):
        if not args:
            print(f"Opening `{website}`...")
            webbrowser.open("https://google.com")

        else:
            print(f"Opening `{website}` with search `{args}`...")
            webbrowser.open(
                f"https://www.google.com/search?q={args}")


main()
