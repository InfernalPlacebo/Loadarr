"""
Loadarr Docker Compose Generator
Author: InfernalPlacebo
Description:
This script generates a Docker Compose based on the user's container choices.
"""
# TODO: Finish YAML generation
# TODO: Refactor generate functions to use single parser function
# TODO: Add Usenet support
# TODO: Add Bazarr, Mylar, and Headphones support to extra services
# TODO: Implement support for services in README (Lidarr, Readarr, LazyLibrarian, etc.)
# TODO: Add configuration options for services
# TODO: Add image documentation links to README
import yaml


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
                torrent_client_choice = (input("Which client do you want to use? [q]Bittorent or [r]Torrent: ")
                                         .strip().lower())
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
        downloader_choice = (input("Add an automatic downloader? (Sonarr/Radarr/Lidarr/Readerr) [Y]es or [N]o: ")
                             .strip().lower())
        if downloader_choice == "y":
            while downloader_choice:
                downloader_choice = input("Which downloader do you want to use? Separate with comma. [S]onarr, "
                                          "[R]adarr, [L]idarr, or R[e]aderr: ").strip().lower()
                downloader_choice = downloader_choice.split(",")
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
                    elif "p" in choice:
                        extra_services += "prowlarr,"
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

    create_docker_compose(choices['media_server'], choices['torrent_client'], choices['usenet_client'],
                          choices['downloader'], choices['extra_services'])


# Generate automatically using variables passed
def generate_autonomous(media_server_choice, torrent_client_choice, usenet_client_choice, downloader_choice,
                        extra_services_choice):
    # Media server choice
    if media_server_choice.lower() == "p":
        media_server_choice = "plex"
    elif media_server_choice.lower() == "e":
        media_server_choice = "emby"
    else:
        media_server_choice = ""

    # Torrent client choice
    if torrent_client_choice.lower() == "q":
        torrent_client_choice = "qbittorrent"
    elif torrent_client_choice == "r":
        torrent_client_choice = "rtorrent"
    else:
        torrent_client_choice = ""

    # Usenet client choice
    if usenet_client_choice == "y":
        usenet_client_choice = "not available"
    else:
        usenet_client_choice = ""

    # Downloader choice
    downloader = ""
    if "s" in downloader_choice:
        downloader += "sonarr,"
    if "r" in downloader_choice:
        downloader += "radarr,"
    if "l" in downloader_choice:
        downloader += "lidarr,"
    if "e" in downloader_choice:
        downloader += "readerr,"

    # Extra services choice
    extra_services = ""
    if "o" in extra_services_choice:
        extra_services += "overseerr,"
    if "u" in extra_services_choice:
        extra_services += "unpackerr,"
    if "t" in extra_services_choice:
        extra_services += "tautulli,"

    choices = {
        "media_server": media_server_choice,
        "torrent_client": torrent_client_choice,
        "usenet_client": usenet_client_choice,
        "downloader": downloader,
        "extra_services": extra_services
    }

    create_docker_compose(choices['media_server'], choices['torrent_client'], choices['usenet_client'],
                          choices['downloader'], choices['extra_services'])


# Create the Docker Compose file based on the selected services
def create_docker_compose(media_server, torrent_client, usenet_client, downloader, extra_services):
    # Print for debugging
    print("\nSelected options:")
    print(f"Media server: {'media_server'}")
    print(f"Torrent client: {'torrent_client'}")
    print(f"Usenet client: {'usenet_client'}")
    print(f"Downloader: {'downloader'}")
    print(f"Extra services: {'extra_services'}")

    # Create dictionary to be used for the YAML format
    compose_dict = {
        "services": {}
    }

    # Add media server service
    if media_server == 'plex':
        compose_dict["services"]["plex"] = {
            "image": "lscr.io/linuxserver/plex:latest",
            "container_name": "plex",
            "network_mode": "host",
            "environment": [
                "DOCKER_MODS=linuxserver/mods:plex-absolute-hama",
                "TZ=America/Denver",
                "VERSION=docker",
                "PUID=1000",
                "PGID=1000"
            ],
            "volumes": [
                ":/config",
                ":/tv",
                ":/movies",
            ],
            "restart": "unless-stopped"
        }

    # Add torrent service
    if torrent_client == 'qbittorrent':
        compose_dict["services"]["qbittorrent"] = {
            "image": "ghcr.io/hotio/qbittorrent:latest",
            "container_name": "qbittorrent",
            "ports": [
                "6881:6881",
                "6881:6881/udp",
                "8080:8080"
            ],
            "environment": [
                "TZ=America/Denver",
                "WEBUI_PORT=8080",
                "PUID=1000",
                "PGID=1000",
                "UMASK=002",
                "WEBUI_USERNAME=admin",
                "WEBUI_PASSWORD=password",
                "WEBUI_PORTS=8080/tcp, 8080/udp",
                "TORRENT_PORT=6881",
                "VPN_ENABLED=true",
                "VPN_CONF=wg0",
                "VPN_PROVIDER=custom",
                "VPN_LAN_NETWORK=192.168.1.0/24",
                'VPN_EXPOSE_PORTS_ON_LAN=',
                "VPN_AUTO_PORT_FORWARDING=true",
                "VPN_AUTO_PORT_FORWARDING_PORT=",
                "VPN_KEEP_LOCAL_DNS=false",
                "VPN_FIREWALL_TYPE=auto",
                "VPN_HEALTHCHECK_ENABLED=true",
                "PRIVOXY_ENABLED=false",
                "UNBOUND_ENABLED=false"
            ],
            "hostname": "qbittorrent.internal",
            "volumes": [
                ":/config",
                ":/downloads"
            ],
            "cap_add": [
                "NET_ADMIN"
            ],
            "sysctls": {
                "net.ipv4.conf.all.src_valid_mark=1",
                "net.ipv6.conf.all.disable_ipv6=1"
            },
            "healthcheck": {
                "test": "curl --fail https://icanhazip.com/ || exit 1",
                "interval": "120s",
                "timeout": "10s",
                "retries": 5,
                "start_period": "30s"
            },
            "labels": {
                "autoheal": "true"
            },
            "restart": "unless-stopped"
        }

    # Add downloader services
    if "sonarr" in downloader:
        compose_dict["services"]["sonarr"] = {
            "image": "lscr.io/linuxserver/sonarr:latest",
            "container_name": "sonarr",
            "ports": "8989:8989",
            "environment": [
                "TZ=America/Denver",
                "PUID=3000",
                "PGID=3000"
            ],
            "volumes": [
                ":/config",
                ":/tv",
                ":/downloads"
            ],
            "restart": "unless-stopped"
        }
    if "radarr" in downloader:
        compose_dict["services"]["radarr"] = {
            "image": "lscr.io/linuxserver/radarr:latest",
            "container_name": "radarr",
            "ports": "7878:7878",
            "environment": [
                "TZ=America/Denver",
                "PUID=3000",
                "PGID=3000"
            ],
            "volumes": [
                ":/config",
                ":/movies",
                ":/downloads"
            ],
            "restart": "unless-stopped"
        }

    # Add extra services
    if "overseerr" in extra_services:
        compose_dict["services"]["overseerr"] = {
            "image": "sctx/overseerr:latest",
            "container_name": "overseerr",
            "ports": "5055:5055",
            "environment": [
                "TZ=America/Denver",
                "PUID=3000",
                "PGID=3000"
            ],
            "volumes": [
                ":/config",
            ],
            "restart": "unless-stopped"
        }
    if "unpackerr" in extra_services:
        compose_dict["services"]["unpackerr"] = {
            "image": "ghcr.io/hotio/unpackerr:latest",
            "container_name": "unpackerr",
            "environment": [
                "TZ=America/Denver",
                "PUID=3000",
                "PGID=3000"
            ],
            "volumes": [
                ":/config",
                ":/data"
            ],
            "restart": "unless-stopped"
        }
    if "tautulli" in extra_services:
        compose_dict["services"]["tautulli"] = {
            "image": "lscr.io/linuxserver/tautulli:latest",
            "container_name": "tautulli",
            "ports": "8181:8181",
            "environment": [
                "TZ=America/Denver",
                "PUID=3000",
                "PGID=3000"
            ],
            "volumes": [
                ":/config",
            ],
            "restart": "unless-stopped"
        }
    if "prowlarr" in extra_services:
        compose_dict["services"]["prowlarr"] = {
            "image": "lscr.io/linuxserver/prowlarr:latest",
            "container_name": "prowlarr",
            "ports": "9696:9696",
            "environment": [
                "TZ=America/Denver",
                "PUID=3000",
                "PGID=3000"
            ],
            "volumes": [
                ":/config",
            ],
            "restart": "unless-stopped"
        }
