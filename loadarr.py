"""
Loadarr Docker Compose Generator
Author: InfernalPlacebo
Description:
This script generates a Docker Compose based on the user's container choices.
"""


def generate_interactive():
    # Prompt the user for container choices
    print("Loadarr Docker Compose Generator\n")
    
    # Media server choice
    media_server_choice = ""
    while media_server_choice.lower() not in ["y", "n"]:
        media_server_choice = input("Would you like a media server? [Y]es or [N]o: ").strip().lower()
        if media_server_choice == "y":
            while media_server_choice not in ["p", "e"]:
                media_server_choice = input("Which media server do you want to use? [P]lex or [E]mby: ").strip().lower()
                if media_server_choice == "p":
                    media_server_choice = "plex"  # Add Plex container choice
                    break
                elif media_server_choice == "e":
                    media_server_choice = "emby"  # Add Emby container choice
                    break
                else:
                    print("Invalid choice. Please enter 'P' or 'E'.")
            break
        elif media_server_choice != "n":
            print("Invalid choice. Please enter 'Y' or 'N'.")
    
    # Torrent client choice
    torrent_client_choice = ""
    while torrent_client_choice not in ["y", "n"]:
        torrent_client_choice = input("Would you like to add a torrent client? [Y]es or [N]o: ").strip().lower()
        if torrent_client_choice == "y":
            while torrent_client_choice not in ["q", "r"]:
                torrent_client_choice = input("Which client do you want to use? [q]Bittorent or [r]Torrent: ").strip().lower()
                if torrent_client_choice == "q":
                    torrent_client_choice = "qbittorrent"  # Add qBittorrent container choice
                    break
                elif torrent_client_choice == "r":
                    torrent_client_choice = "rtorrent"  # Add rTorrent container choice
                    break
                else:
                    print("Invalid choice. Please enter 'Q' or 'R'.")
            break
        elif torrent_client_choice != "n":
            print("Invalid choice. Please enter 'Y' or 'N'.")
    
    # Usenet client choice
    usenet_client_choice = ""
    while usenet_client_choice.lower() not in ["y", "n"]:
        usenet_client_choice = input("Would you like to add a Usenet client? [Y]es or [N]o: ").strip().lower()
        if usenet_client_choice == "y":
            print("Usenet support is not yet available.")
        break
    
    # Downloader choice
    downloader_choice = ""
    downloader = ""
    while downloader_choice not in ["y", "n"]:
        downloader_choice = input("Add an automatic downloader? (Sonarr/Radarr/Lidarr/Readerr) [Y]es or [N]o: ").strip().lower()
        if downloader_choice == "y":
            while downloader_choice:
                downloader_choice = input("Which downloader do you want to use? Separate with comma. [S]onarr, "
                                          "[R]adarr, [L]idarr, or R[e]aderr: ").strip().lower()
                downloader_choice = downloader_choice.split(",")
                print(downloader_choice)
                for choice in downloader_choice:
                    if "s" in choice:
                        downloader += "sonarr,"
                    elif "r" in choice:
                        downloader += "radarr,"
                    elif "l" in choice:
                        downloader += "lidarr,"
                    elif "e" in choice:
                        downloader += "readerr,"
                break
            break
        elif downloader_choice != "n":
            print("Invalid choice. Please enter 'Y' or 'N'.")

    # Extra services choice
    extra_services_choice = ""
    extra_services = ""
    while extra_services_choice not in ["y", "n"]:
        extra_services_choice = input("Add extra services? [Y]es or [N]o: ").strip().lower()
        if extra_services_choice == "y":
            while extra_services_choice:
                extra_services_choice = input(
                    "Which extra services do you want to add? Separate with comma. [O]verseerr, "
                    "[U]npackerr, [T]autulli: ").strip().lower()
                extra_services_choice = extra_services_choice.split(",")
                for choice in extra_services_choice:
                    if "o" in choice:
                        extra_services += "overseerr,"
                    elif "u" in choice:
                        extra_services += "unpackerr,"
                    elif "t" in choice:
                        extra_services += "tautulli,"
                break
            break
        elif extra_services_choice != "n":
            print("Invalid choice. Please enter 'Y' or 'N'.")
    
    choices = {
        "media_server": media_server_choice,
        "torrent_client": torrent_client_choice,
        "usenet_client": usenet_client_choice,
        "downloader": downloader,
        "extra_services": extra_services
    }
    
    # Output the selected options
    print("\nSelected options:")
    print(f"Media server: {choices['media_server']}")
    print(f"Torrent client: {choices['torrent_client']}")
    print(f"Usenet client: {choices['usenet_client']}")
    print(f"Downloader: {choices['downloader']}")
    print(f"Extra services: {choices['extra_services']}")


# Generate automatically using variables passed
def generate_autonomous(media_server_choice, torrent_client_choice, usenet_client_choice, downloader_choice, extra_services_choice):
    # Media server choice
    if "y" in media_server_choice:
        media_server_choice = "plex" if "p" in media_server_choice else "emby"
    else:
        media_server_choice = ""

    # Torrent client choice
    if "y" in torrent_client_choice:
        torrent_client_choice = "qbittorrent" if "q" in torrent_client_choice else "rtorrent"
    else:
        torrent_client_choice = ""

    # Usenet client choice
    if "y" in  usenet_client_choice:
        usenet_client_choice = "not available"
    else:
        usenet_client_choice = ""

    # Downloader choice
    downloader = ""
    if "y" in downloader_choice:
        for choice in downloader_choice.split(","):
            if "s" in choice:
                downloader += "sonarr,"
            elif "r" in choice:
                downloader += "radarr,"
            elif "l" in choice:
                downloader += "lidarr,"
            elif "e" in choice:
                downloader += "readerr,"

    # Extra services choice
    extra_services = ""
    if "y" in extra_services_choice:
        for choice in extra_services_choice.split(","):
            if "o" in choice:
                extra_services += "overseerr,"
            elif "u" in choice:
                extra_services += "unpackerr,"
            elif "t" in choice:
                extra_services += "tautulli,"

    choices = {
        "media_server": media_server_choice,
        "torrent_client": torrent_client_choice,
        "usenet_client": usenet_client_choice,
        "downloader": downloader,
        "extra_services": extra_services
    }

    # Output the selected options
    print("\nSelected options:")
    print(f"Media server: {choices['media_server']}")
    print(f"Torrent client: {choices['torrent_client']}")
    print(f"Usenet client: {choices['usenet_client']}")
    print(f"Downloader: {choices['downloader']}")
    print(f"Extra services: {choices['extra_services']}")

