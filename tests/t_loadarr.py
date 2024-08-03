# tests/test_loadarr.py
import pytest
from io import StringIO
import sys

from loadarr import generate_autonomous


def test_generate_autonomous(capfd):
    media_server_choice = 'yp'
    torrent_client_choice = 'yq'
    usenet_client_choice = 'n'
    downloader_choice = 'y,s,r'
    extra_services_choice = 'y,o,u'

    generate_autonomous(media_server_choice, torrent_client_choice, usenet_client_choice, downloader_choice, extra_services_choice)
    captured = capfd.readouterr()
    output = captured.out

    assert "Media server: plex" in output
    assert "Torrent client: qbittorrent" in output
    assert "Usenet client: " in output
    assert "Downloader: sonarr,radarr," in output
    assert "Extra services: overseerr,unpackerr," in output


def test_generate_autonomous_no_services(capfd):
    media_server_choice = 'n'
    torrent_client_choice = 'n'
    usenet_client_choice = 'n'
    downloader_choice = 'n'
    extra_services_choice = 'n'

    generate_autonomous(media_server_choice, torrent_client_choice, usenet_client_choice, downloader_choice, extra_services_choice)
    captured = capfd.readouterr()
    output = captured.out

    assert "Media server: " in output
    assert "Torrent client: " in output
    assert "Usenet client: " in output
    assert "Downloader: " in output
    assert "Extra services: " in output