'''
Parameters:
- 

'''

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt



url = "https://www.imdb.com/title/tt5348176/episodes?season=1&ref_=tt_eps_sn_1"
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')

ratings_html = soup.find_all('span', class_='ipl-rating-star__rating')
ratings = []
for rating in ratings_html:
  ratings.append(rating.get_text())

y_axis_title = "Rating"
x_axis_title = "Episode #"

show_title = "Barry"
show_season = "1"
graph_title = f'{show_title} (Season {show_season})'

file_extension = ".png"
file_name_to_save = show_title + file_extension
ratings = [float(rating) for rating in ratings if '.' in rating]
num_episodes = len(ratings)
episode_numbers = [x for x in range(1, num_episodes + 1)]

plt.suptitle(graph_title, fontsize=16)
plt.plot(episode_numbers, ratings)
plt.ylabel(y_axis_title)
plt.xlabel(x_axis_title)

plt.savefig(file_name_to_save)
plt.show()
