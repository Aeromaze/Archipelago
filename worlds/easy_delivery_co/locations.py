from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld

LOCATION_NAME_TO_ID = {
    "Deliver Big Box": 1,
    "Deliver Big Box Stack": 2,
    "Deliver Box Bunch": 3,
    "Deliver Box Stack": 4,
    "Deliver Crate": 5,
    "Deliver Crate of Drinks": 6,
    "Deliver Crate Stack": 7,
    "Deliver Lots of Crates of Drinks": 8,
    "Deliver Pizza Stack": 9,
    "Deliver Pizza Stack Mega": 10,
    "Deliver Plant Pot": 11,
    "Deliver Plant Pot Bunch": 12,
    "Deliver Plant Pot Stack": 13,
    "Deliver Plant Pot Wide": 14,
    "Deliver Sack": 15,
    "Deliver Sack Stack": 16,
    "Deliver Drink": 17,
}

TOWN_NAME_TO_ID = {
    "Upton": 11,
    "Weston": 12,
    "Easton": 13,
    "Winton": 21,
    "Munton": 22,
    "Lopton": 23,
    "Clifton": 31,
    "Damton": 32,
    "Smalton": 33,
}

for startTown in TOWN_NAME_TO_ID:
    for endTown in TOWN_NAME_TO_ID:
        LOCATION_NAME_TO_ID[startTown + " to " + endTown + " Delivery"] = (
            int(str(TOWN_NAME_TO_ID[startTown]) + str(TOWN_NAME_TO_ID[endTown])))
        LOCATION_NAME_TO_ID[startTown + " to " + endTown + " Perfect Delivery"] = (
            int("1" + str(TOWN_NAME_TO_ID[startTown]) + str(TOWN_NAME_TO_ID[endTown])))

MOUNTAIN_TOWN_NAMES = [
    "Upton",
    "Weston",
    "Easton",
]

SNOWY_PEAKS_NAMES = [
    "Winton",
    "Munton",
    "Lopton",
]

FISHING_TOWN_NAMES = [
    "Clifton",
    "Damton",
    "Smalton",
]

remaining_deliveries = LOCATION_NAME_TO_ID.copy()


class EasyDeliveryCoLocation(Location):
    game = "Easy Delivery Co."


def get_delivery_location_names(town_names: list[str], world: EasyDeliveryCoWorld) -> list[str]:
    locations = []
    for startTown in town_names:
        for endTown in town_names:
            if world.options.perfect_deliveries == 0 or world.options.perfect_deliveries == 1:
                location = startTown + " to " + endTown + " Delivery"
                if location in remaining_deliveries:
                    locations.append(location)
                    del remaining_deliveries[location]
            if world.options.perfect_deliveries == 1 or world.options.perfect_deliveries == 2:
                location = startTown + " to " + endTown + " Perfect Delivery"
                if location in remaining_deliveries:
                    locations.append(location)
                    del remaining_deliveries[location]
    return locations


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: EasyDeliveryCoWorld) -> None:
    create_regular_locations(world)


def create_regular_locations(world: EasyDeliveryCoWorld) -> None:
    mountain_town = world.get_region("Mountain Town")
    snowy_peaks = world.get_region("Snowy Peaks")
    fishing_town = world.get_region("Fishing Town")
    all_towns = world.get_region("All towns")

    mountain_town_locations = get_location_names_with_ids(get_delivery_location_names(MOUNTAIN_TOWN_NAMES, world))
    snowy_peaks_locations = get_location_names_with_ids(get_delivery_location_names(MOUNTAIN_TOWN_NAMES + SNOWY_PEAKS_NAMES, world))
    fishing_town_locations = get_location_names_with_ids(get_delivery_location_names(MOUNTAIN_TOWN_NAMES + FISHING_TOWN_NAMES, world))
    all_towns_locations = get_location_names_with_ids(get_delivery_location_names(MOUNTAIN_TOWN_NAMES + SNOWY_PEAKS_NAMES + FISHING_TOWN_NAMES, world))

    if world.options.payload_checks:
        payload_locations = get_location_names_with_ids(
            ["Deliver Big Box", "Deliver Big Box Stack", "Deliver Box Bunch", "Deliver Box Stack",
             "Deliver Crate", "Deliver Crate of Drinks", "Deliver Crate Stack", "Deliver Lots of Crates of Drinks",
             "Deliver Pizza Stack", "Deliver Pizza Stack Mega", "Deliver Plant Pot", "Deliver Plant Pot Bunch",
             "Deliver Plant Pot Stack", "Deliver Plant Pot Wide", "Deliver Sack", "Deliver Sack Stack",
             "Deliver Drink"]
        )
        mountain_town.add_locations(payload_locations, EasyDeliveryCoLocation)

    mountain_town.add_locations(mountain_town_locations, EasyDeliveryCoLocation)
    snowy_peaks.add_locations(snowy_peaks_locations, EasyDeliveryCoLocation)
    fishing_town.add_locations(fishing_town_locations, EasyDeliveryCoLocation)
    all_towns.add_locations(all_towns_locations, EasyDeliveryCoLocation)
