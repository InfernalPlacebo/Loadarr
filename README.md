# Loadarr

Loadarr is a Docker Compose generator script that helps you set up media server environments with various services.

## Description

The script can run in two modes:
- **Interactive Mode**: Prompts the user for input to configure the media server environment.
- **Autonomous Mode**: Takes command-line arguments to configure the media server environment without user interaction.

## Usage

### Interactive Mode

To run the script in interactive mode, use the following command:

```sh
python main.py --mode interactive
```

### Autonomous Mode

To run the script in autonomous mode, use the following command with the required arguments:

```sh
python main.py --mode autonomous --media_server <media_server> --torrent_client <torrent_client> --usenet_client <usenet_client> --downloader <downloader> --extra_services <extra_services>
```

#### Example

```sh
python main.py --mode autonomous --media_server p --torrent_client q --usenet_client none --downloader sr --extra_services ou
```

#### Arguments
 - --mode: Choose the mode to run the script 
   - Interactive or Autonomous. Defaults to autonomous. 
 - --media_server: Media server choice for autonomous mode
   - Available Options: 
     - p: Plex
     - j: Jellyfin *(Not yet implemented)*
     - e: Emby
     - k: Kodi *(Not yet implemented)*
     - n: None
 - --torrent_client: Torrent client choice for autonomous mode
   - Available Options: 
     - q: qBittorrent
     - r: rTorrent
     - d: Deluge *(Not yet implemented)*
     - t: Transmission *(Not yet implemented)*
     - n: None
 - --usenet_client: Usenet client choice for autonomous mode
   - *(Not yet implemented)*
   - Available Options: 
       - s: SABnzbd *(Not yet implemented)*
       - n: None
 - --downloader: Downloader choice for autonomous mode
 - Available Options: 
     - sr: Sonarr + Radarr *(Example of multiple services)*
     - s: Sonarr
     - r: Radarr
     - l: Lidarr *(Not yet implemented)*
     - e: Readarr *(Not yet implemented)*
     - a: LazyLibrarian *(Not yet implemented)*
     - b: BookSonic *(Not yet implemented)*
     - n: None
 - --extra_services: Extra services choice for autonomous mode
 - Available Options: 
     - ou: Overseerr + Unpackerr *(Example of multiple services)*
     - o: Overseerr
     - u: Unpackerr
     - t: Tautulli
     - n: None

#### Notes
 - Ensure all required arguments are provided when running in autonomous mode.
 - The script will output the selected options for verification.