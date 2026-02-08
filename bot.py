import requests
from bs4 import BeautifulSoup as bt
import os 

url = 'https://store.steampowered.com/search/?maxprice=free&supportedlang=english&specials=1&ndl=1'
DISCORDWEBHOOK = os.environ.get('DISCORD_WEBHOOK')
request = requests.get(url)


def sendjson(gametittle,linkgame,gameimage):
    data = {
        "content": f"Nuevo juego reclamable gratis en steam por tiempo limitado, es {gametittle} / link: {linkgame}",
        "image": f"{gameimage}" #Image but with the link is enought
    }
    #requests.post(DISCORDWEBHOOK, json=data)
    if not webhook:
    raise ValueError("DISCORD_WEBHOOK environment variable not set")


if request.status_code == 200:
    html = request.text
    soup = bt(html, 'lxml')
    searcher = soup.find('div',id='search_result_container')
    searcher_games = searcher.find_all('div', id='search_resultsRows')

    for game in searcher_games:
        # main div (game)
        maintittles = game.find('a', class_='search_result_row ds_collapse_flag')
        # game tittle:
        div_game_tittle = maintittles.find('div', 'search_name ellipsis')
        game_tittle_span = div_game_tittle.find('span')
        game_tittle = game_tittle_span.get_text(strip=True)
        # link to buy
        link_buy = maintittles['href']
        # game_image
        search_capsules = maintittles.find('div', class_='search_capsule')
        game_image_img = search_capsules.find('img')
        game_image = game_image_img['src']
        sendjson(game_tittle,link_buy,game_image)

else:
    print("Error, not status_code 200 detected")


