'''
Parameters:
- show url
- show title
- show season

'''

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv
import os

def plot_graph(title, season, url):
  print(url)
  result = requests.get(url)
  soup = BeautifulSoup(result.content, 'html.parser')

  ratings_html = soup.find_all('span', class_='ipl-rating-star__rating')
  ratings = []
  for rating in ratings_html:
    ratings.append(rating.get_text())

  y_axis_title = "Rating"
  x_axis_title = "Episode #"

  show_title = title
  show_season = season
  graph_title = f'{show_title} (Season {show_season})'

  file_extension = ".png"
  file_name_to_save = f'{show_title}S{show_season}{file_extension}'
  ratings = [float(rating) for rating in ratings if '.' in rating]
  num_episodes = len(ratings)
  episode_numbers = [x for x in range(1, num_episodes + 1)]

  plt.suptitle(graph_title, fontsize=16)
  plt.plot(episode_numbers, ratings)
  plt.ylabel(y_axis_title)
  plt.xlabel(x_axis_title)

  plt.savefig(file_name_to_save)
  plt.show()

csv_file = "shows.csv"

with open(csv_file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    header = next(readCSV)
    for row in readCSV:
        title = row[0]
        season = row[1]
        url = row[2]
        plot_graph(title, season, url)



