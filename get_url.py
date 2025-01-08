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

if len(sys.argv) < 2:
  print("Usage: python get_url.py <id>")
  sys.exit(1)

id = sys.argv[1]

oauth_url = f"https://anilist.co/api/v2/oauth/authorize?client_id={id}&response_type=token"

print("Opening the browser for OAuth authorization")

webbrowser.open(oauth_url)