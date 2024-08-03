# tests/test_main.py
import pytest
from unittest.mock import patch, MagicMock
import sys
from main import main


# Test the interactive mode of the main script, uncomment to run
# def test_main_interactive():
#     with patch('loadarr.generate_interactive') as mock_generate_interactive:
#         with patch.object(sys, 'argv', ['main.py', '--mode', 'interactive']):
#             main()
#             mock_generate_interactive.assert_called_once()


# Test the autonomous mode of the main script with all required arguments
def test_main_autonomous():
    with patch('loadarr.generate_autonomous') as mock_generate_autonomous:
        with patch.object(sys, 'argv', [
            'main.py', '--mode', 'autonomous', '--media_server', 'p', '--torrent_client', 'q',
            '--usenet_client', 'none', '--downloader', 'sr', '--extra_services', 'ou'
        ]):
            main()
            mock_generate_autonomous.assert_called_once_with('plex', 'qbittorrent', 'none', 'sonarr,radarr', 'overseerr,unpackerr')


# Test the autonomous mode of the main script without providing all required arguments
def test_main_autonomous_missing_args():
    with patch.object(sys, 'argv', ['main.py', '--mode', 'autonomous']):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert excinfo.value.code != 0