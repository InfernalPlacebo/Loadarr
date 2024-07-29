"""Tests for loadarr.py. Doesn't work in current state, needs to be updated."""

import unittest
from unittest.mock import patch
from io import StringIO
import sys

from loadarr import generate_dockercompose


class TestGenerateDockerCompose(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'y', 'p',    # Media server: yes, Plex
        'y', 'q',    # Torrent client: yes, qBittorrent
        'n',         # Usenet client: no
        'y', 's,r',  # Downloader: yes, Sonarr and Radarr
        'y', 'o,u'   # Extra services: yes, Overseerr and Unpackerr
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_dockercompose(self, mock_stdout, mock_input):
        generate_dockercompose()
        output = mock_stdout.getvalue()

        self.assertIn("Media server: plex", output)
        self.assertIn("Torrent client: qbittorrent", output)
        self.assertIn("Usenet client: ", output)
        self.assertIn("Downloader: ['s', 'r']", output)
        self.assertIn("Extra services: o, u", output)

    @patch('builtins.input', side_effect=[
        'n',         # Media server: no
        'n',         # Torrent client: no
        'n',         # Usenet client: no
        'n',         # Downloader: no
        'n'          # Extra services: no
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_dockercompose_no_services(self, mock_stdout, mock_input):
        generate_dockercompose()
        output = mock_stdout.getvalue()

        self.assertIn("Media server: ", output)
        self.assertIn("Torrent client: ", output)
        self.assertIn("Usenet client: ", output)
        self.assertIn("Downloader: ", output)
        self.assertIn("Extra services: None", output)


if __name__ == '__main__':
    unittest.main()
