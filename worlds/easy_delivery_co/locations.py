from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld

LOCATION_NAME_TO_ID = {}

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


def get_delivery_location_names(town_names: list[str]) -> list[str]:
    locations = []
    for startTown in town_names:
        for endTown in town_names:
            location = startTown + " to " + endTown + " Delivery"
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

    mountain_town_locations = get_location_names_with_ids(get_delivery_location_names(MOUNTAIN_TOWN_NAMES))
    snowy_peaks_locations = get_location_names_with_ids(get_delivery_location_names(MOUNTAIN_TOWN_NAMES + SNOWY_PEAKS_NAMES))
    fishing_town_locations = get_location_names_with_ids(get_delivery_location_names(MOUNTAIN_TOWN_NAMES + FISHING_TOWN_NAMES))
    all_towns_locations = get_location_names_with_ids(get_delivery_location_names(MOUNTAIN_TOWN_NAMES + SNOWY_PEAKS_NAMES + FISHING_TOWN_NAMES))

    mountain_town.add_locations(mountain_town_locations, EasyDeliveryCoLocation)
    snowy_peaks.add_locations(snowy_peaks_locations, EasyDeliveryCoLocation)
    fishing_town.add_locations(fishing_town_locations, EasyDeliveryCoLocation)
    all_towns.add_locations(all_towns_locations, EasyDeliveryCoLocation)
