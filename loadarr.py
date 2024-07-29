"""
This script generates a Docker Compose based on the user's container choices.
"""

def generate_dockercompose():
    # Prompt the user for container choices
    print("Loadarr Docker Compose Generator\n")
    print("Choose from the following menus to build your Docker Compose: ")
    print("1. Would you like a media server? [Y]es or [N]o. (Plex or Emby) ")
    media_server_choice = input("Enter Y or N: ")
    if media_server_choice.strip().lower() == "y":
        print("Which media server do you want to use?\n")
        print("[P]lex or [E]mby")
        media_server_choice = input("Enter the first letter of the media server: ")
        if media_server_choice.strip().lower() == "p":
            media_server_choice = "plex"  # Add Plex container choice
        elif media_server_choice.strip().lower() == "e":
            media_server_choice = "emby"  # Add Emby container choice
    print("Would you like to add a torrent client? [Y]es or [N]o.")
    torrent_client_choice = input("Enter Y or N: ")
    if torrent_client_choice.strip().lower() == "y":
        print("Which client do you want to use?\n")
        print("[q]Bittorent or [r]Torrent")
        torrent_client_choice = input("Enter the first letter of the client: ")
        if torrent_client_choice.strip().lower() == "q":
            torrent_client_choice = "qbittorrent"  # Add qBittorrent container choice
        elif torrent_client_choice.strip().lower() == "r":
            torrent_client_choice = "rtorrent"  # Add rTorrent container choice
    print("Would you like to add a Usenet client? [Y]es or [N]o.")
    usenet_client_choice = input("Enter Y or N: ")
    if usenet_client_choice.strip().lower() == "y":
        print("Usenet support is not yet available.")
    print("Add a automatic downloader? (Sonarr/Radarr/Lidarr/Reader) [Y]es or [N]o.")
    downloader_choice = input("Enter Y or N: ")
    if downloader_choice.strip().lower() == "y":
        print("Which downloader do you want to use?\n")
        print("[S]onarr, [R]adarr, [L]idarr, or [R]eader")
        downloader_choice = input("Enter the first letter of the downloader: ")
        if downloader_choice.strip().lower() == "s":
            downloader_choice = "sonarr"  # Add Sonarr container choice
        elif downloader_choice.strip().lower() == "r":
            downloader_choice = "radarr"  # Add Radarr container choice
        elif downloader_choice.strip().lower() == "l":
            downloader_choice = "lidarr"  # Add Lidarr container choice
        elif downloader_choice.strip().lower() == "r":
            downloader_choice = "reader"  # Add Reader container choice
        print("By default, Prowlarr is added when adding downloaders.")
    print("Add extra services? [Y]es or [N]o.")
    extra_services_choice = input("Enter Y or N: ")
    if extra_services_choice.strip().lower() == "y":
        print("Which extra services do you want to add? Separate with comma.\n")
        print("[O]verseerr, [U]npackerr, [T]autulli")
        extra_services_choice = input("Enter the extra service: ")
        extra_services_choice = extra_services_choice.split(",")

    # Generate the Dockerfile based on the choices
    dockerfile = "FROM ubuntu:latest\n\n"
    for choice in choices:
        if choice.strip() == "1":
            dockerfile += "RUN apt-get update && apt-get install -y nginx\n"
        elif choice.strip() == "2":
            dockerfile += "RUN apt-get update && apt-get install -y mysql-server\n"
        elif choice.strip() == "3":
            dockerfile += "RUN apt-get update && apt-get install -y redis-server\n"

    # Write the Dockerfile to a file
    with open("Dockerfile", "w") as file:
        file.write(dockerfile)

    print("Dockerfile generated successfully!")

# Call the function to generate the Dockerfile
generate_dockercompose()