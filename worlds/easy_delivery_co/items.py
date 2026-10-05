from __future__ import annotations

from typing import TYPE_CHECKING

import math

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld

ITEM_NAME_TO_ID = {
    # Inventory Items
    "Energy Drink": 100,
    "Empty Can": 101,
    "Lantern": 102,
    "Lighter": 103,
    "Firewood": 104,
    "Shovel": 105,
    "Bird Seed": 106,
    "Cooking Pot": 107,
    "Coffee": 108,
    "Coffee Powder": 109,
    "Tea": 110,
    "Tea Bags": 111,
    "Fish": 112,
    "Fishing Rod": 113,
    "Fish Soup": 114,
    "Duct Tape": 115,
    "Recovery Disc": 116,
    "Handheld Radio": 117,
    # Traps
    "Ice Trap": 130,
    "Shrink Trap": 131,
    # Car Upgrades
    "Map": 1,
    "Snow Tires": 2,
    "Bumper Bar": 3,
    "Ice Chains": 4,
    "Progressive Car Upgrade": 5,
    # Tunnels
    "Snowy Peaks Tunnel": 11,
    "Fishing Town Tunnel": 12,
    "Factory Tunnel": 13,
    # Towns
    "Upton": 30,
    "Weston": 31,
    "Easton": 32,
    "Winton": 33,
    "Munton": 34,
    "Lopton": 35,
    "Clifton": 36,
    "Damton": 37,
    "Smalton": 38,
    # Other
    "Money": 10,
    "Radio Tower": 20,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Energy Drink": ItemClassification.filler,
    "Empty Can": ItemClassification.filler,
    "Lantern": ItemClassification.filler,
    "Lighter": ItemClassification.progression,
    "Firewood": ItemClassification.filler,
    "Shovel": ItemClassification.filler,
    "Bird Seed": ItemClassification.filler,
    "Cooking Pot": ItemClassification.useful,
    "Coffee": ItemClassification.useful,
    "Coffee Powder": ItemClassification.filler,
    "Tea": ItemClassification.useful,
    "Tea Bags": ItemClassification.filler,
    "Fish": ItemClassification.filler,
    "Fishing Rod": ItemClassification.useful,
    "Fish Soup": ItemClassification.useful,
    "Duct Tape": ItemClassification.filler,
    "Recovery Disc": ItemClassification.progression,
    "Handheld Radio": ItemClassification.useful,
    "Ice Trap": ItemClassification.trap,
    "Shrink Trap": ItemClassification.trap,
    "Map": ItemClassification.progression,
    "Snow Tires": ItemClassification.progression,
    "Bumper Bar": ItemClassification.progression,
    "Ice Chains": ItemClassification.progression,
    "Progressive Car Upgrade": ItemClassification.progression,
    "Snowy Peaks Tunnel": ItemClassification.progression,
    "Fishing Town Tunnel": ItemClassification.progression,
    "Factory Tunnel": ItemClassification.progression,
    "Upton": ItemClassification.progression,
    "Weston": ItemClassification.progression,
    "Easton": ItemClassification.progression,
    "Winton": ItemClassification.progression,
    "Munton": ItemClassification.progression,
    "Lopton": ItemClassification.progression,
    "Clifton": ItemClassification.progression,
    "Damton": ItemClassification.progression,
    "Smalton": ItemClassification.progression,
    "Money": ItemClassification.filler,
    "Radio Tower": ItemClassification.progression,
}


class EasyDeliveryCoItem(Item):
    game = "Easy Delivery Co."


def get_random_filler_item_name(world: EasyDeliveryCoWorld) -> str:
    match (world.random.randint(0, 35)):
        case 0:
            return "Energy Drink"
        # case 1:
        #     return "Empty Can"
        case 2 | 3:
            return "Firewood"
        case 4:
            return "Bird Seed"
        case 5 | 6 | 7:
            return "Coffee"
        case 8 | 9:
            return "Coffee Powder"
        case 10 | 11 | 12:
            return "Tea"
        case 13 | 14:
            return "Tea Bags"
        case 15:
            return "Fish"
        case 16 | 17:
            return "Fish Soup"
        case 18 | 19:
            return "Duct Tape"
        case 20 | 21 | 22 | 23:
            return "Money"
        case _:
            return "Energy Drink"

def get_random_trap_name(world: EasyDeliveryCoWorld) -> str:
    match (world.random.randint(0, 1)):
        case 0:
            return "Ice Trap"
        case _:
            return "Shrink Trap"


def create_item_with_correct_classification(world: EasyDeliveryCoWorld, name: str) -> EasyDeliveryCoItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return EasyDeliveryCoItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: EasyDeliveryCoWorld) -> None:
    itempool: list[Item] = [
        # world.create_item("Fishing Rod"),
        # world.create_item("Cooking Pot"),
        world.create_item("Lighter")
    ]

    if world.options.progressive_car_upgrades == 0:
        itempool.append(world.create_item("Snow Tires"))
        itempool.append(world.create_item("Bumper Bar"))
        itempool.append(world.create_item("Ice Chains"))
    else:
        itempool.append(world.create_item("Progressive Car Upgrade"))
        itempool.append(world.create_item("Progressive Car Upgrade"))
        itempool.append(world.create_item("Progressive Car Upgrade"))

    if world.options.blocked_tunnels == 1:
        itempool.append(world.create_item("Snowy Peaks Tunnel"))
        itempool.append(world.create_item("Fishing Town Tunnel"))
        itempool.append(world.create_item("Factory Tunnel"))
    elif world.options.blocked_tunnels == 2:
        itempool.append(world.create_item("Factory Tunnel"))
    if world.options.radio_towers == 1 or world.options.radio_towers == 3:
        itempool.append(world.create_item("Radio Tower"))
        itempool.append(world.create_item("Radio Tower"))
        itempool.append(world.create_item("Radio Tower"))
        itempool.append(world.create_item("Radio Tower"))
    if world.options.lock_towns == 1:
        match (math.floor(world.random.random() * 3)):
            case 0:
                starting_town = world.create_item("Weston")
                itempool.append(world.create_item("Upton"))
                itempool.append(world.create_item("Easton"))
            case 1:
                starting_town = world.create_item("Easton")
                itempool.append(world.create_item("Upton"))
                itempool.append(world.create_item("Weston"))
            case _:
                starting_town = world.create_item("Upton")
                itempool.append(world.create_item("Weston"))
                itempool.append(world.create_item("Easton"))

        world.push_precollected(starting_town)

        if world.multiworld.players == 1:
            early_town = ["Upton", "Weston", "Easton"]
            early_town.remove(starting_town.name)
            world.multiworld.early_items[world.player][early_town.pop(world.random.randint(0, 1))] = 1

        itempool.append(world.create_item("Winton"))
        itempool.append(world.create_item("Munton"))
        itempool.append(world.create_item("Lopton"))
        itempool.append(world.create_item("Clifton"))
        itempool.append(world.create_item("Damton"))
        itempool.append(world.create_item("Smalton"))


    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    if world.options.trap_percentage > 0:
        number_of_traps = int(needed_number_of_filler_items * world.options.trap_percentage / 100)
        needed_number_of_filler_items -= number_of_traps
        itempool += [world.create_item(get_random_trap_name(world)) for _ in range(number_of_traps)]

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool


item_name_groups: dict[str, set[str]] = {
    "Town": {"Upton", "Weston", "Easton", "Winton", "Munton", "Lopton", "Clifton", "Damton", "Smalton"},
    "Car Upgrade": {"Snow Tires", "Bumper Bar", "Ice Chains", "Progressive Car Upgrade"},
    "Tunnel": {"Snowy Peaks Tunnel", "Fishing Town Tunnel", "Factory Tunnel"}
}
