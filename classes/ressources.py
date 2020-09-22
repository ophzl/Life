from . import Player, Functions

class Ressources:

    def getRessources():

        possibilities = []
        player_tools = []

        for tools in Player.inventory:
            for item in tools:
                player_tools.append(item)

        # Wood Items
        wood_pickaxe = Functions.search_action('Wood Pickaxe', player_tools)
        wood_axe = Functions.search_action('Wood Axe', player_tools)

        # Stone Items
        stone_pickaxe = Functions.search_action('Stone Pickaxe', player_tools)
        stone_axe = Functions.search_action('Stone Axe', player_tools)

        # Legendary Items
        legendary_pickaxe = Functions.search_action('Legendary Pickaxe', player_tools)
        legendary_axe = Functions.search_action('Legendary Axe', player_tools)

        if legendary_pickaxe:
            possibilities.append('Arbre')

        elif stone_pickaxe:
            possibilities.append('Arbre')

        elif wood_pickaxe:
            possibilities.append('Arbre')

        if legendary_axe:
            possibilities.append('Stone', 'Gold')

        elif stone_axe:
            possibilities.append('Stone', 'Gold')

        elif wood_axe:
            possibilities.append('Stone')
