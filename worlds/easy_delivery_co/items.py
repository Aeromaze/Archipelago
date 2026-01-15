from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld

ITEM_NAME_TO_ID = {
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
    "Map": 1,
    "Snow Tires": 2,
    "Bumper Bar": 3,
    "Ice Chains": 4,
    "Money": 10,
    "Snowy Peaks Tunnel": 11,
    "Fishing Town Tunnel": 12,
    "Factory Tunnel": 13,
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
    "Map": ItemClassification.progression,
    "Snow Tires": ItemClassification.progression,
    "Bumper Bar": ItemClassification.progression,
    "Ice Chains": ItemClassification.progression,
    "Money": ItemClassification.filler,
    "Snowy Peaks Tunnel": ItemClassification.progression,
    "Fishing Town Tunnel": ItemClassification.progression,
    "Factory Tunnel": ItemClassification.progression,
    "Radio Tower": ItemClassification.progression,
}


class EasyDeliveryCoItem(Item):
    game = "Easy Delivery Co."


def get_random_filler_item_name(world: EasyDeliveryCoWorld) -> str:
    return "Energy Drink"


def create_item_with_correct_classification(world: EasyDeliveryCoWorld, name: str) -> EasyDeliveryCoItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return EasyDeliveryCoItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: EasyDeliveryCoWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Snow Tires"),
        world.create_item("Bumper Bar"),
        world.create_item("Ice Chains"),
        world.create_item("Lighter"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Money"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Coffee"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Tea"),
        world.create_item("Bird Seed"),
        world.create_item("Bird Seed"),
        world.create_item("Bird Seed"),
        world.create_item("Bird Seed"),
        world.create_item("Bird Seed"),
        world.create_item("Duct Tape"),
        world.create_item("Duct Tape"),
        world.create_item("Duct Tape"),
        world.create_item("Duct Tape"),
        world.create_item("Duct Tape"),
        # world.create_item("Fishing Rod"),
        # world.create_item("Cooking Pot"),
    ]

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


    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
