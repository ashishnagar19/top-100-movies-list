import requests
import Beautifulsoup
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = Beautifulsoup(data, "html.parser")
title1 = soup.data.title
print(title1)