import os
import webbrowser
from os import name, system

os.system("color 08")

website_input = input("Enter the website you want to enter:\n")

website = website_input.split(" ")


def clear():
    if name == "nt":
        _ = system("cls")


if website[0].lower() == "youtube":
    try:
        search_words = []

        for keyword in website[1:]:
            search_words.append(keyword)

        search = " ".join(search_words)
        print(f"You on `{website[0]}` searched for `{search}`.")
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={search}")
    except IndexError:
        webbrowser.open("https://www.youtube.com/")

elif website[0].lower() == "music":
    try:
        search_words = []

        for keyword in website[1:]:
            search_words.append(keyword)

        search = " ".join(search_words)

        print(f"You on `{website[0]}` searched for `{website[1]}`.")
        webbrowser.open(
            f"https://music.apple.com/de/search?term={website[1]}")
    except IndexError:
        webbrowser.open("https://music.apple.com/de/")

elif website[0].lower() == "reddit":
    try:
        search_words = []

        for keyword in website[1:]:
            search_words.append(keyword)

        search = " ".join(search_words)
        print(f"You on `{website[0]}` searched for `{website[1]}`.")
        webbrowser.open(
            f"https://www.reddit.com/search/?q={website[1]}")
    except IndexError:
        webbrowser.open("https://www.reddit.com/")

elif website[0].lower() == "twitter":
    try:
        search_words = []

        for keyword in website[1:]:
            search_words.append(keyword)

        search = " ".join(search_words)
        print(f"You on `{website[0]}` searched for `{website[1]}`.")
        webbrowser.open(
            f"https://twitter.com/search?q={website[1]}&src=typed_query")
    except IndexError:
        webbrowser.open("https://twitter.com/home")

elif website[0].lower() == "pip":
    try:
        search_words = []

        for keyword in website[1:]:
            search_words.append(keyword)

        search = " ".join(search_words)
        print(f"You on `{website[0]}` searched for `{website[1]}`.")
        webbrowser.open(
            f"https://pypi.org/search/?q={website[1]}")
    except IndexError:
        webbrowser.open("https://pypi.org/")

elif website[0].lower() == "google":
    try:
        search_words = []

        for keyword in website[1:]:
            search_words.append(keyword)

        search = " ".join(search_words)
        print(f"You searched on `{website[0]}` searched for `{website[1]}`.")
        webbrowser.open(
            f"https://www.google.com/search?q={website[1]}")
    except IndexError:
        webbrowser.open("https://www.google.com/")
