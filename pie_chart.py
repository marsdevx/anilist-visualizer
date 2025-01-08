#                                                             ⣛⣛⣛⣛⣛⣛⡛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣉⣉⣉⣙⣛⣛⣛⣛⣛⡛⠛⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿    #
#    File:         pie_chart.py                               ⣿⣿⣿⣿⡿⣻⡽⠟⠒⠒⠪⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣿⣿⣛⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶    #
#                                                             ⣿⣿⡿⣣⠌⠁⢀⣤⠀⠀⠀⠙⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠲⠿⠙⣙⣻⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #
#    Project:      anilist-visualizer                         ⣿⣟⠻⠂⠀⣴⣿⢏⡀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢀⣤⣤⢀⣀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠾⠽⠛⢻⣿⣿⣿⣿⣿⣿    #
#    Github:       marsdevx                                   ⡌⠉⠃⠀⣼⣿⡿⣘⣛⡣⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣠⣾⣿⣿⣿⢸⣿⠿⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣾⣯⣿⠿⣿⣿    #
#                                                             ⣿⣦⣄⠀⣿⣿⣿⣿⣿⣿⡆⠀⠀⢢⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢀⣴⣿⣿⣿⣿⣟⣼⣾⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⢀⣴⣿⣿    #
#    Created:      07:13   08/01/2025                         ⣿⣿⣿⣦⢻⣿⣿⣿⣿⣿⡇⠀⠀⢼⡃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⢰⣶⣶⣄⠀⢀⣴⣿⣿⣿⣿    #
#    Updated:      07:15   08/01/2025                         ⣿⣿⣿⣿⡏⣿⣿⣏⢭⣵⣄⣀⣴⣯⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿⣿⣿⠀⣸⣿⣿⣿⣿⣿    #
#                                                             ⣿⣿⣿⣿⣇⠸⢿⣿⣮⡻⣿⣿⣿⢟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡩⣟⣛⣛⣫⣦⣄⣀⣴⣎⢮⡻⣿⡟⣠⣿⣿⣿⣿⣿⣿    #
#    Path:         ./pie_chart.py                             ⣿⣿⣿⣿⣿⣿⣷⣶⣭⣭⣄⣉⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⣿⣿⣿⣿⣞⡿⢊⣼⣿⣿⣿⣿⣿⣿⣿    #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣙⠿⣿⣿⣿⣿⣿⡿⠛⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿    #
#                                                             ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣦⣤⣬⣭⣍⣀⡲⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    #

import matplotlib.pyplot as plt

def plot_pie_chart(my_dict, title):
  
  data_labels = list(my_dict.keys())
  data_amount = list(my_dict.values())

  colors = ['#664753', '#656432', '#33576E', '#385E63', '#655633', '#4C4766', '#404465']
  explode = [0.05] * len(data_amount)
  
  fig, ax = plt.subplots()

  fig.patch.set_facecolor('#323D44')
  
  wedges, texts, autotexts = ax.pie(data_amount, colors=colors, explode=explode, autopct='%1.0f%%', textprops={'color': "#B4BDB7"})
  
  for wedge, color in zip(wedges, colors):
    if color == '#664753':
      wedge.set_edgecolor('#FF6384')
      continue
    elif color == '#33576E':
      wedge.set_edgecolor('#37A2EB')
      continue
    elif color == '#656432':
      wedge.set_edgecolor('#FFD700')
      continue
    elif color == '#385E63':
      wedge.set_edgecolor('#4BC0C0')
      continue
    elif color == '#655633':
      wedge.set_edgecolor('#FFA500')
      continue
    elif color == '#4C4766':
      wedge.set_edgecolor('#9966CC')
      continue
    elif color == '#404465':
      wedge.set_edgecolor('#6A5ACD')
  
  ax.legend(wedges, data_labels, loc='center left', bbox_to_anchor=(0.85, 0, 0.5, 1), 
            facecolor='none', edgecolor='none', labelcolor='#B4BDB7')

  ax.set_title(title, color='#B4BDB7')

  ax.axis('equal')

  plt.show(block=False)