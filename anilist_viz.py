#                                                             ⠀⠀⠀⠀⠀⠀⠀⢻⣿⡿⣌⢿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⢀⣠⠄⣠⣶⣿⣿⣿⣿⣿⣿⣟⣠⣾⣿⣿⣿⠟⢡⣿⣿⢿⣟⡣⠞⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⢸⣽⠏⠘⣯⢻⣿⣿⣿⣿⣿⠯⠑⠛⣛⣿⣗⣋⠉⢉⢉⣛⠿⣿⣿⣿⣿⣿⣿⣮⣍⠀⠴⠒⠤⣾⣟⣭⡊⠰⢿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⠆⠻⡧⠘⣿⡅⠹⣿⠟⣋⣤⣶⢎⣾⣿⣿⣿⣿⣿⣿⣿⣮⣝⢆⠙⢿⣿⣿⣿⣿⣿⣷⣄⢨⣿⣿⠿⠿⠭⢬⣘⢿⣿⡟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⠀⢷⠦⢀⣽⡷⢀⣴⣿⣿⣿⣷⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣦⡢⠹⣮⢻⣿⣿⣿⣿⣧⡉⠿⠷⣶⠄⡀⢘⣿⣿⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠿⣡⣿⣿⢿⣿⣟⣽⣿⣿⣿⣿⣿⣎⣿⣿⣟⣿⣿⣿⣿⣿⣄⢎⠃⢻⣿⣿⣿⣿⣷⡨⣛⠺⠋⠠⠸⠟⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⣾⣿⣿⢏⣿⣿⢹⡏⣿⣿⣿⣿⣿⣿⡸⣿⣿⣮⢿⣿⣿⣿⣟⢧⡣⡀⢻⣿⡿⣿⣿⣷⡸⡗⠀⠀⣼⡿⠋⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#    File:         anilist_viz.py                             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡟⡼⣿⠏⣿⣧⣿⣿⣿⣿⠸⣿⡇⠘⢿⣿⣧⡙⣿⣟⣿⣶⡳⣅⠈⣿⣷⢹⣿⣿⣧⠀⡠⢀⡉⠀⢠⣧⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⠛⣸⡟⢠⢹⣿⢻⣿⣿⣿⣧⢻⣿⡰⣬⡻⣿⣜⣌⠻⣮⡻⣿⣜⢆⠸⣿⡏⣿⣿⣿⡌⣷⠏⠀⠀⡺⣧⠎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#    Project:      anilist-visualizer                         ⠀⠀⠀⠀⠀⠀⣰⡟⣼⣿⣿⣿⡟⢠⣿⢁⣿⢸⣿⣽⣿⣿⣿⡌⣇⢻⣧⠻⠘⢙⢫⣭⣧⡐⢦⡲⣭⣥⡁⢿⣯⢹⣿⡞⣇⢑⣀⡔⢸⣧⢻⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#    Github:       marsdevx                                   ⠀⠀⠀⠀⣠⣾⡟⣼⣿⣿⣿⣿⡇⣸⠇⣸⡟⡞⡿⡇⢿⣿⣿⣇⠘⡌⢟⡄⣿⣮⡣⠹⣧⣻⣮⡳⢌⢿⣿⣸⣿⠘⣿⡇⣿⠸⢏⣴⣿⣿⠈⣿⢿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⣠⣾⡿⠋⢰⣿⢻⣿⣿⣿⡇⡿⠀⢿⣛⡃⢡⢻⠈⢧⠹⣿⣆⠲⠈⢿⡜⣿⣿⠦⠄⠙⠛⠛⠒⠤⠍⠛⣿⡆⣿⣿⣿⠲⠟⠛⣾⢏⡀⣿⣏⢿⣎⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#    Created:      07:13   08/01/2025                         ⣴⡿⠟⠋⠀⠀⣾⣿⣾⣿⠇⣿⠁⣣⢰⣿⣿⣷⡀⢏⢧⠈⣧⠘⢿⣄⠀⠘⠿⠉⢀⡀⠀⠀⠀⠀⠀⢢⣄⠀⢉⣰⣿⣿⣿⡆⠀⠾⣣⢿⢀⠘⣿⢦⢻⣷⢝⢿⣿⣿⣿⣿⣿⣿⣿   #
#    Updated:      07:20   08/01/2025                         ⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡀⣿⠀⣿⣼⣿⡿⠿⠗⣈⢮⡃⠘⢂⠈⠻⢿⡄⢟⢰⣿⣇⣰⡆⠀⠀⣦⢸⣿⠃⢸⣿⣿⣿⢹⠱⢦⡸⢏⡾⢸⠀⠘⠀⡑⣝⢿⣿⣮⣝⢿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⢸⣿⣿⢸⣿⡇⢸⡄⣿⡯⠁⣠⠀⠀⠀⠨⣿⣷⣄⠹⣢⣜⡻⣷⣿⣿⣿⣏⠠⣆⡄⠀⣾⣿⣼⣾⣿⣿⡇⢸⠼⢾⡇⣾⠃⡘⡇⣦⢠⡈⠪⢳⣭⣛⠿⣿⣿⣿⣿⣿   #
#    Path:         ./anilist_viz.py                           ⠀⠀⠀⠀⠀⢸⡇⣿⠘⣿⣇⠈⣧⠻⠁⣸⣿⣀⣤⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⠾⣶⠾⠿⠿⡿⢾⣿⣿⡇⢻⢰⠞⡠⠀⠀⣇⣿⣻⣇⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⡄⠀⠀⢸⡇⢹⡆⢻⣿⡆⠘⠄⢄⠸⣿⣿⡏⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣠⡾⣟⣿⡇⣸⣿⣿⣇⣼⢨⠞⠁⢰⡀⣿⢸⢸⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠇⠀⠀⢸⡇⠈⢧⠈⢿⣷⠀⠀⠘⣷⣽⣿⣿⣶⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⠁⣿⣿⣿⠿⣿⠀⠀⡀⢸⡇⢻⣿⡖⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⡇⠀⠀⠀⣧⠀⠈⠆⠈⠻⣧⠱⡄⠸⣿⣫⡔⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⡇⣿⣿⣿⠀⡟⠀⢸⡇⢸⣿⡈⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⢀⠰⣦⡀⣧⣭⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⡿⠃⣿⢻⡟⢰⡇⠀⠘⣧⠀⣿⣷⠸⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢀⡾⠀⣿⣇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣠⠀⣿⣾⡇⢾⠃⠀⠀⣿⢠⢸⣿⣃⢿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⡠⢻⣿⡤⣝⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⣠⣾⡿⢰⣇⣿⠸⢹⠀⠀⠀⠸⠘⠀⢛⠉⠈⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   #
#                                                             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣇⢿⡇⢰⣬⠙⠛⠿⠿⣿⣿⣿⣿⣿⠿⠛⠁⠀⣠⣾⠟⣯⣾⣼⢹⡟⠁⡎⠀⢰⡶⠿⠟⠋⡛⠛⠓⠾⢭⣝⣛⠻⠿⢿⣿⣿⣿⣿⣿   #

import sys
import requests
import matplotlib.pyplot as plt
from pie_chart import plot_pie_chart
from urllib.parse import urlparse, parse_qs

if len(sys.argv) < 2:
  print("Usage: python anilist_viz.py <url>")
  sys.exit(1)

url = sys.argv[1]
fragment = urlparse(url).fragment
params = parse_qs(fragment)
ani_token = params.get("access_token", [None])[0]

ani_headers = {
  'Authorization': 'Bearer ' + ani_token,
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

ani_json = {
    'query': '''
    query {
      MediaListCollection(userId: 6725344, type: ANIME, status: COMPLETED) {
        lists {
          name
          entries {
            media {
              id
              title {
                english
              }
              season
              seasonYear
              genres
              averageScore
              countryOfOrigin
            }
            score
          }
        }
      }
    }
    '''
}

response = requests.post('https://graphql.anilist.co', headers=ani_headers, json=ani_json)
data = response.json()

def transform_dictionary(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)
    top_items = sorted_items[:6]
    bottom_items = sorted_items[6:]
    others_value = sum(item[1] for item in bottom_items)
    transformed_dict = dict(top_items)
    transformed_dict['Others'] = others_value
    return transformed_dict

season_count = {}
for list_item in data['data']['MediaListCollection']['lists']:
    for entry in list_item['entries']:
        season = entry['media']['season']
        if season is not None:
          if season in season_count:
              season_count[season] += 1
          else:
              season_count[season] = 1

country_count = {}
for list_item in data['data']['MediaListCollection']['lists']:
    for entry in list_item['entries']:
        country = entry['media']['countryOfOrigin']
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

proper_year_count = {
    "1990-2010": 0,
    "2011-2014": 0,
    "2015-2016": 0,
    "2017-2018": 0,
    "2019-2020": 0,
    "2021-2022": 0,
    "2023-2024": 0,
}
for list_item in data['data']['MediaListCollection']['lists']:
    for entry in list_item['entries']:
        year = entry['media']['seasonYear']
        if year is not None:
          if 1990 <= year < 2011:
              proper_year_count["1990-2010"] += 1
          elif 2011 <= year < 2015:
              proper_year_count["2011-2014"] += 1
          elif 2015 <= year < 2017:
              proper_year_count["2015-2016"] += 1
          elif 2017 <= year < 2019:
              proper_year_count["2017-2018"] += 1
          elif 2019 <= year < 2021:
              proper_year_count["2019-2020"] += 1
          elif 2021 <= year < 2023:
              proper_year_count["2021-2022"] += 1
          elif year >= 2023:
              proper_year_count["2023-2024"] += 1

proper_score_count = {
    "0-5.9": 0,
    "6-6.9": 0,
    "7-7.9": 0,
    "8-8.9": 0,
    "9-10": 0
}
for list_item in data['data']['MediaListCollection']['lists']:
    for entry in list_item['entries']:
        score = entry['score']
        if 0 <= score < 6:
            proper_score_count["0-5.9"] += 1
        elif 6 <= score < 7:
            proper_score_count["6-6.9"] += 1
        elif 7 <= score < 8:
            proper_score_count["7-7.9"] += 1
        elif 8 <= score < 9:
            proper_score_count["8-8.9"] += 1
        elif score >= 9:
            proper_score_count["9-10"] += 1

genre_count = {}
for list_item in data['data']['MediaListCollection']['lists']:
    for entry in list_item['entries']:
        genres = entry['media']['genres']
        for genre in genres:
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
proper_genere_count = transform_dictionary(genre_count)

proper_av_score_count = {
    "0-5.9": 0,
    "6-6.9": 0,
    "7-7.9": 0,
    "8-8.9": 0,
    "9-10": 0
}
for list_item in data['data']['MediaListCollection']['lists']:
    for entry in list_item['entries']:
        av_score = entry['media']['averageScore']
        if 0 <= av_score < 60:
            proper_av_score_count["0-5.9"] += 1
        elif 60 <= av_score < 70:
            proper_av_score_count["6-6.9"] += 1
        elif 70 <= av_score < 80:
            proper_av_score_count["7-7.9"] += 1
        elif 80 <= av_score < 90:
            proper_av_score_count["8-8.9"] += 1
        elif av_score >= 90:
            proper_av_score_count["9-10"] += 1

plot_pie_chart(season_count, 'Seasons')
plot_pie_chart(country_count, 'Country')
plot_pie_chart(proper_year_count, 'Years')
plot_pie_chart(proper_score_count, 'My Score')
plot_pie_chart(proper_av_score_count, 'Average Score')
plot_pie_chart(proper_genere_count, 'Genres')

plt.show()