#                                                                                           ⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⣥⣶⣖⣲⣖⣲⡖⠉⠙⠛⢿⣿⣿⣿⣿⣿⣿⣿    #
#                                                                                           ⣿⣿⣿⣿⣿⢟⢍⣮⡷⠗⣊⣵⣾⣿⣿⣿⣷⣍⡳⢄⠀⠉⠻⢿⣿⣿⣿⣿    #
#    File:         get_url.py                                                               ⣿⣿⣿⠟⢁⣵⣷⣶⣶⠮⠿⠿⣿⣿⣿⣿⣿⢉⡻⢷⡄⠀⣠⣄⠻⣿⣿⣿    #
#                                                                                           ⣿⣿⢯⢮⣾⡿⣰⡟⡡⣪⣥⣶⡄⠰⣿⣿⣿⣮⣿⡎⣿⣶⡸⣿⡆⠙⣿⣿    #
#    Project:      anilist-visualizer                                                       ⣿⣏⠃⣿⣿⣿⡏⢱⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣼⣿⣿⣷⣧⢠⡀⢸⣿    #
#    Github:       marsdevx                                                                 ⣿⡈⢀⡏⣬⣿⣿⡜⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣯⣿⡻⣻⣻⡜⠇⢀⣿    #
#                                                                                           ⣧⠇⣾⣇⣫⡿⢿⣿⣌⣙⡛⢉⣽⣿⣿⣿⣿⣿⣿⣿⣿⢿⣜⢹⣿⠀⠈⣽    #
#    Created:      11:07   08/01/2025                                                       ⣿⠀⣿⣿⣿⣷⣾⣿⣿⣿⣿⣬⣿⣿⣿⣿⣿⣿⣿⣯⣾⣿⠿⡿⣀⡀⠀⣿    #
#    Updated:      13:06   08/01/2025                                                       ⣿⣇⢸⡿⣿⣿⢿⣿⣿⣿⣿⡻⣿⣿⣿⢻⣿⣿⣿⣿⡿⢡⡾⣻⣿⠃⢸⣿    #
#                                                                                           ⣿⣿⣄⢳⡹⣏⢟⣯⣷⣿⠛⣣⣭⡝⣿⣿⣿⣝⣻⡿⠷⠻⡁⡋⢀⢠⣿⣿    #
#    Path:         ./get_url.py                                                             ⣿⣿⣿⣆⠳⢀⡻⣿⣿⣿⣜⠻⡿⣉⣼⣿⡿⠿⠿⠛⠀⡀⠉⠐⣵⣿⣿⣿    #
#                                                                                           ⣿⣿⣿⣿⣷⣤⡈⠢⢝⡫⢿⣷⣽⣛⣛⣿⡶⠆⣀⠔⠋⢀⣤⣾⣿⣿⣿⣿    #
#                                                                                           ⣿⣿⣿⣿⣿⣿⣿⣶⣤⣍⣛⠈⠙⠉⠉⠡⠤⣤⣀⣤⣴⣿⣿⣿⣿⣿⣿⣿    #

import sys
import webbrowser

def print_help():
    print("""
    AniList Visualizer - A tool for visualizing your AniList data.

    Usage:
    1. Create Your AniList Client:
        - Go to https://anilist.co/settings/developer
        - Click "Create New Client."
        - Fill in the "name" field (use any name) and leave the "redirect URL" blank.
        - Click "Save" and copy the Client ID (a series of five numbers under the "ID" field).

    2. Generate the Authorization URL:
        Run the following command, replacing <id> with the Client ID:
        python3 get_url.py <id>
        This will generate a URL for authorization.

    3. Authorize the Application:
        - Open the generated URL in your browser.
        - Click "Authorize" on the AniList authorization page.
        - Copy the URL from the address bar.

    4. Run the Main Program:
        Run the following command, replacing <url> with the copied URL:
        python3 anilist_viz.py <url>
        This will fetch your AniList data and display the visualization.
    """)

if len(sys.argv) != 2:
  print_help()
  sys.exit(1)

id = sys.argv[1]
if not id.isdigit():
    print("Invalid ID format. It must be a positive integer.") 
    sys.exit(1)

oauth_url = f"https://anilist.co/api/v2/oauth/authorize?client_id={id}&response_type=token"

print("Opening the browser for OAuth authorization")

webbrowser.open(oauth_url)