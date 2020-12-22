import webbrowser
import time

browser_path_open = open("chrome_path.txt", "r")
brower_path = f"{browser_path_open.read()} %s"
# C:/Program Files/Google/Chrome/Application/chrome.exe
time.sleep(1)
print("Mit welchem Dienst möchtest du dein Paket tracken?")
tracking_with = input("1. Parcello\n2. Direkt beim Zusteller\n")

if tracking_with == "1":
    time.sleep(1)
    tracking_number = input("Bitte gib deine Tracking Nummer ein:\n")
    time.sleep(1)
    print("Versuche Parcello zu erreichen...")
    time.sleep(1)
    print("Parcello erreicht!")
    webbrowser.get(brower_path).open_new_tab(f"https://www.parcello.org/tracking?tid={tracking_number}")
elif tracking_with == "2":
    time.sleep(1)
    print("Mit welchem Zusteller wird das Paket geliefert?")
    zusteller_input = input("1. DHL\n2. DPD\n3. GLS\n")
    tracking_number = input("Bitte gib deine Tracking Nummer ein:\n")
    if zusteller_input == "1":
        print("Verbinde mit DHL Servern...")
        time.sleep(1)
        webbrowser.get(brower_path).open_new_tab(f"https://www.dhl.de/de/privatkunden/dhl-sendungsverfolgung.html?piececode={tracking_number}")
    elif zusteller_input == "2":
        print("Verbinde mit DPD Servern...")
        time.sleep(1)
        webbrowser.get(brower_path).open_new_tab(f"https://tracking.dpd.de/status/de_DE/parcel/{tracking_number}")
    elif zusteller_input == "3":
        print("Verbinde mit GLS Servern...")
        time.sleep(1)
        webbrowser.get(brower_path).open_new_tab(f"https://www.gls-pakete.de/sendungsverfolgung?trackingNumber={tracking_number}")
