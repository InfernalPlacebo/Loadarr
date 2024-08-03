import argparse
from loadarr import generate_interactive, generate_autonomous


# Main function to parse arguments and call the appropriate function based on the mode
def main():
    # Create an argument parser for the script
    parser = argparse.ArgumentParser(description="Loadarr Docker Compose Generator")

    # Add arguments to the parser
    parser.add_argument('--default', help="Use default settings", action="store")
    parser.add_argument('--mode', choices=['interactive', 'autonomous'], default='autonomous', help="Choose the mode"
                                                                                                    " to run the script")
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
