"""
Loadarr Docker Compose Generator

This script generates Docker Compose configurations for media server environments.
It can run in two modes:
- Interactive Mode: Prompts the user for input to configure the media server environment.
- Autonomous Mode: Takes command-line arguments to configure the media server environment without user interaction.

Usage:
    python main.py --mode interactive
    python main.py --mode autonomous --media_server <media_server> --torrent_client <torrent_client> --usenet_client <usenet_client> --downloader <downloader> --extra_services <extra_services>

Arguments:
    --mode: Choose the mode to run the script (interactive or autonomous). Defaults to autonomous.
    --media_server: Media server choice for autonomous mode.
    --torrent_client: Torrent client choice for autonomous mode.
    --usenet_client: Usenet client choice for autonomous mode.
    --downloader: Downloader choice for autonomous mode.
    --extra_services: Extra services choice for autonomous mode.
"""

import argparse
from loadarr import generate_interactive, generate_autonomous


# Main function to parse arguments and call the appropriate function based on the mode
def main():
    # Create an argument parser for the script
    parser = argparse.ArgumentParser(description="Loadarr Docker Compose Generator")

    # Add arguments to the parser
    parser.add_argument('--default', help="Use default settings", action="store")
    parser.add_argument('--mode', choices=['interactive', 'autonomous'], default='autonomous',
                        help="Choose the mode to run the script")
    parser.add_argument('--media_server', help="Media server choice for autonomous mode")
    parser.add_argument('--torrent_client', help="Torrent client choice for autonomous mode")
    parser.add_argument('--usenet_client', help="Usenet client choice for autonomous mode")
    parser.add_argument('--downloader', help="Downloader choice for autonomous mode")
    parser.add_argument('--extra_services', help="Extra services choice for autonomous mode")

    args = parser.parse_args()

    # Call the appropriate function based on the mode
    if args.mode == 'interactive':
        generate_interactive()
    elif args.mode == 'autonomous':
        # Check if all choices are provided for in autonomous mode
        if not all([args.media_server, args.torrent_client, args.usenet_client, args.downloader, args.extra_services]):
            parser.error("All choices must be provided for in autonomous mode")
        generate_autonomous(args.media_server, args.torrent_client, args.usenet_client, args.downloader,
                            args.extra_services)


if __name__ == "__main__":
    main()
