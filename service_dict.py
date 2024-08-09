import yaml


def load_services(compose_dict, services):
    for category, service in services.items():
        if not service:
            continue

        # Add media server service
        if 'plex' in service and 'plex' not in compose_dict["services"]:
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
                    "/path/to/config:/config",
                    "/path/to/tv:/tv",
                    "/path/to/movies:/movies",
                ],
                "restart": "unless-stopped"
            }

        # Add torrent service
        if 'qbittorrent' in service and 'qbittorrent' not in compose_dict["services"]:
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
                    "/path/to/config:/config",
                    "/path/to/downloads:/downloads"
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
        if "sonarr" in service and 'sonarr' not in compose_dict["services"]:
            compose_dict["services"]["sonarr"] = {
                "image": "lscr.io/linuxserver/sonarr:latest",
                "container_name": "sonarr",
                "ports": ["8989:8989"],
                "environment": [
                    "TZ=America/Denver",
                    "PUID=3000",
                    "PGID=3000"
                ],
                "volumes": [
                    "/path/to/config:/config",
                    "/path/to/tv:/tv",
                    "/path/to/downloads:/downloads"
                ],
                "restart": "unless-stopped"
            }
        if "radarr" in service and 'radarr' not in compose_dict["services"]:
            compose_dict["services"]["radarr"] = {
                "image": "lscr.io/linuxserver/radarr:latest",
                "container_name": "radarr",
                "ports": ["7878:7878"],
                "environment": [
                    "TZ=America/Denver",
                    "PUID=3000",
                    "PGID=3000"
                ],
                "volumes": [
                    "/path/to/config:/config",
                    "/path/to/movies:/movies",
                    "/path/to/downloads:/downloads"
                ],
                "restart": "unless-stopped"
            }

        # Add extra services
        if "overseerr" in service and 'overseerr' not in compose_dict["services"]:
            compose_dict["services"]["overseerr"] = {
                "image": "sctx/overseerr:latest",
                "container_name": "overseerr",
                "ports": ["5055:5055"],
                "environment": [
                    "TZ=America/Denver",
                    "PUID=3000",
                    "PGID=3000"
                ],
                "volumes": [
                    "/path/to/config:/config",
                ],
                "restart": "unless-stopped"
            }
        if "unpackerr" in service and 'unpackerr' not in compose_dict["services"]:
            compose_dict["services"]["unpackerr"] = {
                "image": "ghcr.io/hotio/unpackerr:latest",
                "container_name": "unpackerr",
                "environment": [
                    "TZ=America/Denver",
                    "PUID=3000",
                    "PGID=3000"
                ],
                "volumes": [
                    "/path/to/config:/config",
                    "/path/to/data:/data"
                ],
                "restart": "unless-stopped"
            }
        if "tautulli" in service and 'tautulli' not in compose_dict["services"]:
            compose_dict["services"]["tautulli"] = {
                "image": "lscr.io/linuxserver/tautulli:latest",
                "container_name": "tautulli",
                "ports": ["8181:8181"],
                "environment": [
                    "TZ=America/Denver",
                    "PUID=3000",
                    "PGID=3000"
                ],
                "volumes": [
                    "/path/to/config:/config",
                ],
                "restart": "unless-stopped"
            }
        if "prowlarr" in service and 'prowlarr' not in compose_dict["services"]:
            compose_dict["services"]["prowlarr"] = {
                "image": "lscr.io/linuxserver/prowlarr:latest",
                "container_name": "prowlarr",
                "ports": ["9696:9696"],
                "environment": [
                    "TZ=America/Denver",
                    "PUID=3000",
                    "PGID=3000"
                ],
                "volumes": [
                    "/path/to/config:/config",
                ],
                "restart": "unless-stopped"
            }

    return compose_dict
