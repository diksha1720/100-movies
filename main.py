from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
data = response.text

soup = BeautifulSoup(data, "html.parser")
movie_titles = [movie.getText() for movie in soup.select("div h3")][::-1]
print(movie_titles)

for movie in movie_titles:
    with open('movies.txt', 'a') as file:
        file.write(f"{movie}\n")

