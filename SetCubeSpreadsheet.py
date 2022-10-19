import json
import time

import requests


def get_card_list(magic_set, rarity):

    request = requests.get('https://api.scryfall.com/cards/search?order=name&q=set:'+magic_set
                           + '+rarity:'+rarity
                           + '+is:booster'
                           + "&unique=prints")
    response = request.json()

    for card in response["data"]:
        card_needed = {
            'Name': card["name"],
            'Rarity': rarity.upper(),
            'Color': "",
            'In Cube': 0,
            'Needed': 0,
            'Owned': 0
        }
        for color in card["colors"]:
            card_needed["Color"] += color
        # # For Identifying Attractions, not needed in not Unfinity
        # if "attraction_lights" in card.keys():
        #     card_needed["Attraction lights"] = ""
        #     for value in card["attraction_lights"]:
        #         card_needed["Attraction lights"] += str(value) + "|"
        #     card_needed["Attraction lights"] = card_needed["Attraction lights"][:-1]

        if rarity == 'r' or rarity == 'm':
            card_needed['Needed'] = 1
        elif rarity == 'u':
            card_needed['Needed'] = 2
        elif rarity == 'c':
            card_needed['Needed'] = 3

        cards_in_cube.append(card_needed)


if __name__ == '__main__':

    cards_in_cube = []
    magic_set = "unf"

    file = open("cube.json", "a")
    get_card_list(magic_set, "m")
    time.sleep(0.5)
    get_card_list(magic_set, "r")
    time.sleep(0.5)
    get_card_list(magic_set, "u")
    time.sleep(0.5)
    get_card_list(magic_set, "c")
    time.sleep(0.5)
    file.write(json.dumps(cards_in_cube))


