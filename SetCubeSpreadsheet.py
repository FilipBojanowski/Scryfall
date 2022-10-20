import json
import time

import requests


def get_card_list(magic_set):

    get_query_from_scryfall('https://api.scryfall.com/cards/search?order=rarity&q=set:'+magic_set +
                            '+is:booster' +
                            "&unique=prints")


def get_query_from_scryfall(url):
    request = requests.get(url)
    response = request.json()

    for card in response["data"]:
        card_needed = {
            'Name': card["name"],
            'Rarity': card["rarity"][0].upper(),
            'Color': "",
            'In Cube': 0,
            'Needed': 0,
            'Left': 0
        }
        rarity = card["rarity"][0]
        for color in card["colors"]:
            card_needed["Color"] += color
        # For Identifying Attractions, not needed in not Unfinity
        if "attraction_lights" in card.keys():
            card_needed["Attraction lights"] = ""
            for value in card["attraction_lights"]:
                card_needed["Attraction lights"] += str(value) + "|"
            card_needed["Attraction lights"] = card_needed["Attraction lights"][:-1]

        if rarity == 'r' or rarity == 'm':
            card_needed['Needed'] = 1
        elif rarity == 'u':
            card_needed['Needed'] = 2
        elif rarity == 'c':
            card_needed['Needed'] = 3

        cards_in_cube.append(card_needed)
    if response["has_more"]:
        time.sleep(0.5)
        get_query_from_scryfall(response["next_page"])


if __name__ == '__main__':

    cards_in_cube = []
    magic_set = "unf"

    file = open("cube.json", "a")
    get_card_list(magic_set)
    file.write(json.dumps(cards_in_cube))


