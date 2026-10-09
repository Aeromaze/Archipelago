from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld

LOCATION_NAME_TO_ID = {
    # Payload Deliveries
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
    # Blind Bags
    "Blind Bag 1 Mountain Town": 20,
    "Blind Bag 2 Mountain Town": 21,
    "Blind Bag 3 Mountain Town": 22,
    "Blind Bag 4 Mountain Town": 23,
    "Blind Bag 1 Snowy Peaks": 24,
    "Blind Bag 2 Snowy Peaks": 25,
    "Blind Bag 3 Snowy Peaks": 26,
    "Blind Bag 4 Snowy Peaks": 27,
    "Blind Bag 1 Fishing Town": 28,
    "Blind Bag 2 Fishing Town": 29,
    "Blind Bag 3 Fishing Town": 30,
    "Blind Bag 4 Fishing Town": 31,
    # Snowcats
    "Snowcat Theo": 40,
    "Snowcat Cici": 41,
    "Snowcat Fortino": 42,
    "Snowcat Ellie": 43,
    "Snowcat Foreman": 44,
    "Snowcat Tooey": 45,
    "Snowcat Reed": 46,
    "Snowcat Fives": 47,
    "Snowcat Sixo": 48,
    "Snowcat Ada": 49,
    "Snowcat Fit": 50,
    "Snowcat Gus": 51,
    "Snowcat Seb": 52,
    # Radio Towers
    "Upton Radio Tower": 60,
    "Easton Radio Tower": 61,
    "Snowy Peaks Radio Tower": 62,
    "Fishing Town Radio Tower": 63,
    # Vending Machines
    "Vending Machine in Upton": 100,
    "Vending Machine in Weston": 101,
    "Vending Machine in Easton": 102,
    "Vending Machine in Winton": 103,
    "Vending Machine in Lower Munton": 104,
    "Vending Machine in Upper Munton": 105,
    "Vending Machine in Lopton": 106,
    "Vending Machine in Clifton": 107,
    "Vending Machine in Upper Damton": 108,
    "Vending Machine in Lower Damton": 109,
    "Vending Machine in Smalton (Left)": 110,
    "Vending Machine in Smalton (Right)": 111,
    # Bins
    "Upton Red Bin Easy Flowers": 121,
    "Upton Blue Bin Easy Flowers": 122,
    "Upton Blue Bin Between Easy Flowers and Easy Eats": 123,
    "Upton Blue Bin Easy Eats": 124,
    "Upton Red Bin Easy Eats": 125,
    "Upton Red Bin Town Edge": 126,
    "Weston Blue Bin Entry": 127,
    "Weston Red Bin Entry": 128,
    "Weston Blue Bin Across EZ Bakery": 129,
    "Weston Red Bin EZ Bakery": 130,
    "Weston Blue Bin EZ Bakery": 131,
    "Weston Red Bin Bar Upper": 132,
    "Weston Blue Bin Easy Depot": 133,
    "Weston Blue Bin Bar Lower": 134,
    "Weston Red Bin EZ Cafe": 135,
    "Easton Blue Bin EZ Mart": 136,
    "Easton Red Bin Fuel": 137,
    "Easton Blue Bin Fuel": 138,
    "Easton Blue Bin Easy Pizza": 139,
    "Easton Red Bin Easy Pizza": 140,
    "Winton Blue Bin Easy Flowers": 141,
    "Winton Red Bin Easy Eats": 142,
    "Winton Blue Bin Fuel": 143,
    "Winton Red Bin Fuel": 144,
    "Munton Red Bin Pawn Shop": 145,
    "Munton Red Bin EZ Mart": 146,
    "Munton Blue Bin EZ Mart": 147,
    "Lopton Red Bin Bar": 148,
    "Lopton Red Bin Easy Depot": 149,
    "Lopton Blue Bin Easy Depot": 150,
    "Clifton Red Bin Bar": 151,
    "Clifton Blue Bin Bar": 152,
    "Clifton Blue Bin EZ Mart": 153,
    "Clifton Red Bin EZ Mart": 154,
    "Damton Red Bin Bar": 155,
    "Damton Blue Bin Bar": 156,
    "Damton Red Bin Easy Depot": 157,
    "Damton Blue Bin Easy Depot": 158,
    "Smalton Blue Bin Easy Pizza": 159,
    "Smalton Red Bin Easy Pizza": 160,
    "Smalton Red Bin Easy Eats": 161,
    "Smalton Blue Bin Easy Eats": 162,
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

CITY_NAME_TO_ID = {
    "Mountain Town": 10,
    "Snowy Peaks": 20,
    "Fishing Town": 30,
}

for startTown in TOWN_NAME_TO_ID:
    for endTown in TOWN_NAME_TO_ID:
        LOCATION_NAME_TO_ID[startTown + " to " + endTown + " Delivery"] = (
            int(str(TOWN_NAME_TO_ID[startTown]) + str(TOWN_NAME_TO_ID[endTown])))
        LOCATION_NAME_TO_ID[startTown + " to " + endTown + " Perfect Delivery"] = (
            int("1" + str(TOWN_NAME_TO_ID[startTown]) + str(TOWN_NAME_TO_ID[endTown])))

for startCity in CITY_NAME_TO_ID:
    for endCity in CITY_NAME_TO_ID:
        LOCATION_NAME_TO_ID[startCity + " to " + endCity + " Delivery"] = (
            int(str(CITY_NAME_TO_ID[startCity]) + str(CITY_NAME_TO_ID[endCity])))
        LOCATION_NAME_TO_ID[startCity + " to " + endCity + " Perfect Delivery"] = (
            int("1" + str(CITY_NAME_TO_ID[startCity]) + str(CITY_NAME_TO_ID[endCity])))

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


class EasyDeliveryCoLocation(Location):
    game = "Easy Delivery Co."


def get_delivery_location_names(town_names: list[str], remaining_deliveries, world: EasyDeliveryCoWorld) -> list[str]:
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
    snowy_peaks_early = world.get_region("Snowy Peaks early")
    snowy_peaks = world.get_region("Snowy Peaks")
    fishing_town_entry = world.get_region("Fishing Town entry")
    fishing_town = world.get_region("Fishing Town")
    all_towns = world.get_region("All towns")
    upton = world.get_region("Upton")
    weston = world.get_region("Weston")
    easton = world.get_region("Easton")
    winton = world.get_region("Winton")
    munton_early = world.get_region("Munton early")
    munton = world.get_region("Munton")
    lopton = world.get_region("Lopton")
    clifton = world.get_region("Clifton")
    damton = world.get_region("Damton")
    smalton = world.get_region("Smalton")

    remaining_deliveries = LOCATION_NAME_TO_ID.copy()
    all_towns_locations = {}

    mountain_town_locations = get_location_names_with_ids(
        get_delivery_location_names(MOUNTAIN_TOWN_NAMES, remaining_deliveries, world))
    if world.options.perfect_deliveries == 0 or world.options.perfect_deliveries == 1:
        snowy_peaks_early_locations = get_location_names_with_ids(["Winton to Munton Delivery", "Munton to Winton Delivery"])
        del remaining_deliveries["Winton to Munton Delivery"]
        del remaining_deliveries["Munton to Winton Delivery"]
        snowy_peaks_early.add_locations(snowy_peaks_early_locations, EasyDeliveryCoLocation)
    if world.options.perfect_deliveries == 1 or world.options.perfect_deliveries == 2:
        snowy_peaks_early_locations = get_location_names_with_ids(["Winton to Munton Perfect Delivery", "Munton to Winton Perfect Delivery"])
        del remaining_deliveries["Winton to Munton Perfect Delivery"]
        del remaining_deliveries["Munton to Winton Perfect Delivery"]
        snowy_peaks_early.add_locations(snowy_peaks_early_locations, EasyDeliveryCoLocation)
    if world.options.intercity_deliveries == 1 or world.options.intercity_deliveries == 3:
        snowy_peaks_locations = get_location_names_with_ids(
            get_delivery_location_names(MOUNTAIN_TOWN_NAMES + SNOWY_PEAKS_NAMES, remaining_deliveries, world))
        fishing_town_locations = get_location_names_with_ids(
            get_delivery_location_names(MOUNTAIN_TOWN_NAMES + FISHING_TOWN_NAMES, remaining_deliveries, world))
        all_towns_locations = get_location_names_with_ids(
            get_delivery_location_names(MOUNTAIN_TOWN_NAMES + SNOWY_PEAKS_NAMES + FISHING_TOWN_NAMES, remaining_deliveries, world))
    else:
        snowy_peaks_locations = get_location_names_with_ids(
            get_delivery_location_names(SNOWY_PEAKS_NAMES, remaining_deliveries, world))
        fishing_town_locations = get_location_names_with_ids(
            get_delivery_location_names(FISHING_TOWN_NAMES, remaining_deliveries, world))
    if world.options.intercity_deliveries == 2 or world.options.intercity_deliveries == 3:
        mountain_town_locations.update(get_location_names_with_ids(
            get_delivery_location_names(["Mountain Town"], remaining_deliveries, world)
        ))
        snowy_peaks_locations.update(get_location_names_with_ids(
            get_delivery_location_names(["Mountain Town", "Snowy Peaks"], remaining_deliveries, world)
        ))
        fishing_town_locations.update(get_location_names_with_ids(
            get_delivery_location_names(["Mountain Town", "Fishing Town"], remaining_deliveries, world)
        ))
        all_towns_locations.update(get_location_names_with_ids(
            get_delivery_location_names(["Mountain Town", "Snowy Peaks", "Fishing Town"], remaining_deliveries, world)
        ))

    if world.options.payload_checks:
        payload_locations = get_location_names_with_ids(
            ["Deliver Big Box", "Deliver Big Box Stack", "Deliver Box Bunch", "Deliver Box Stack",
             "Deliver Crate", "Deliver Crate of Drinks", "Deliver Crate Stack", "Deliver Lots of Crates of Drinks",
             "Deliver Pizza Stack", "Deliver Pizza Stack Mega", "Deliver Plant Pot", "Deliver Plant Pot Bunch",
             "Deliver Plant Pot Stack", "Deliver Plant Pot Wide", "Deliver Sack", "Deliver Sack Stack",
             "Deliver Drink"]
        )
        mountain_town.add_locations(payload_locations, EasyDeliveryCoLocation)

    if world.options.blind_bags:
        blind_bag_locations_mt = get_location_names_with_ids(
            ["Blind Bag 1 Mountain Town", "Blind Bag 2 Mountain Town", "Blind Bag 3 Mountain Town",
             "Blind Bag 4 Mountain Town"]
        )
        blind_bag_locations_sp = get_location_names_with_ids(
            ["Blind Bag 1 Snowy Peaks", "Blind Bag 2 Snowy Peaks", "Blind Bag 3 Snowy Peaks",
             "Blind Bag 4 Snowy Peaks"]
        )
        blind_bag_locations_ft = get_location_names_with_ids(
            ["Blind Bag 1 Fishing Town", "Blind Bag 2 Fishing Town", "Blind Bag 3 Fishing Town",
             "Blind Bag 4 Fishing Town"]
        )
        mountain_town.add_locations(blind_bag_locations_mt, EasyDeliveryCoLocation)
        snowy_peaks_early.add_locations(blind_bag_locations_sp, EasyDeliveryCoLocation)
        fishing_town.add_locations(blind_bag_locations_ft, EasyDeliveryCoLocation)

    if world.options.snowcats != 0:
        snowcats_mt = get_location_names_with_ids(
            ["Snowcat Theo", "Snowcat Cici", "Snowcat Tooey", "Snowcat Gus"]
        )
        if world.options.snowcats == 1:
            mountain_town.add_locations(get_location_names_with_ids(["Snowcat Ada"]), EasyDeliveryCoLocation)
        snowcats_sp = get_location_names_with_ids(
            ["Snowcat Fives", "Snowcat Sixo", "Snowcat Foreman", "Snowcat Seb"]
        )
        snowcats_ft = get_location_names_with_ids(
            ["Snowcat Fortino", "Snowcat Ellie", "Snowcat Fit"]
        )
        mountain_town.add_locations(snowcats_mt, EasyDeliveryCoLocation)
        snowy_peaks.add_locations(snowcats_sp, EasyDeliveryCoLocation)
        fishing_town.add_locations(snowcats_ft, EasyDeliveryCoLocation)
        fishing_town_entry.add_locations(get_location_names_with_ids(["Snowcat Reed"]), EasyDeliveryCoLocation)

    if world.options.radio_towers == 1 or world.options.radio_towers == 2:
        radio_mt = get_location_names_with_ids(
            ["Upton Radio Tower", "Easton Radio Tower"]
        )
        mountain_town.add_locations(radio_mt, EasyDeliveryCoLocation)
        snowy_peaks.add_locations(get_location_names_with_ids(["Snowy Peaks Radio Tower"]), EasyDeliveryCoLocation)
        fishing_town.add_locations(get_location_names_with_ids(["Fishing Town Radio Tower"]), EasyDeliveryCoLocation)

    if world.options.vending_machines == 1:
        upton.add_locations(get_location_names_with_ids(["Vending Machine in Upton"]), EasyDeliveryCoLocation)
        weston.add_locations(get_location_names_with_ids(["Vending Machine in Weston"]), EasyDeliveryCoLocation)
        easton.add_locations(get_location_names_with_ids(["Vending Machine in Easton"]), EasyDeliveryCoLocation)
        winton.add_locations(get_location_names_with_ids(["Vending Machine in Winton"]), EasyDeliveryCoLocation)
        munton_early.add_locations(get_location_names_with_ids(["Vending Machine in Lower Munton"]), EasyDeliveryCoLocation)
        munton.add_locations(get_location_names_with_ids(["Vending Machine in Upper Munton"]), EasyDeliveryCoLocation)
        lopton.add_locations(get_location_names_with_ids(["Vending Machine in Lopton"]), EasyDeliveryCoLocation)
        clifton.add_locations(get_location_names_with_ids(["Vending Machine in Clifton"]), EasyDeliveryCoLocation)
        damton.add_locations(get_location_names_with_ids(["Vending Machine in Upper Damton",
                                                          "Vending Machine in Lower Damton"]), EasyDeliveryCoLocation)
        smalton.add_locations(get_location_names_with_ids(["Vending Machine in Smalton (Left)",
                                                           "Vending Machine in Smalton (Right)"]), EasyDeliveryCoLocation)

    if world.options.trash_bins == 1:
        upton_bins = get_location_names_with_ids([
            "Upton Red Bin Easy Flowers",
            "Upton Blue Bin Easy Flowers",
            "Upton Blue Bin Between Easy Flowers and Easy Eats",
            "Upton Blue Bin Easy Eats",
            "Upton Red Bin Easy Eats",
            "Upton Red Bin Town Edge",
        ])
        weston_bins = get_location_names_with_ids([
            "Weston Blue Bin Entry",
            "Weston Red Bin Entry",
            "Weston Blue Bin Across EZ Bakery",
            "Weston Red Bin EZ Bakery",
            "Weston Blue Bin EZ Bakery",
            "Weston Red Bin Bar Upper",
            "Weston Blue Bin Easy Depot",
            "Weston Blue Bin Bar Lower",
            "Weston Red Bin EZ Cafe",
        ])
        easton_bins = get_location_names_with_ids([
            "Easton Blue Bin EZ Mart",
            "Easton Red Bin Fuel",
            "Easton Blue Bin Fuel",
            "Easton Blue Bin Easy Pizza",
            "Easton Red Bin Easy Pizza",
        ])
        winton_bins = get_location_names_with_ids([
            "Winton Blue Bin Easy Flowers",
            "Winton Red Bin Easy Eats",
            "Winton Blue Bin Fuel",
            "Winton Red Bin Fuel",
        ])
        munton_early_bins = get_location_names_with_ids([
            "Munton Red Bin Pawn Shop"
        ])
        munton_bins = get_location_names_with_ids([
            "Munton Red Bin EZ Mart",
            "Munton Blue Bin EZ Mart"
        ])
        lopton_bins = get_location_names_with_ids([
            "Lopton Red Bin Bar",
            "Lopton Red Bin Easy Depot",
            "Lopton Blue Bin Easy Depot",
        ])
        clifton_bins = get_location_names_with_ids([
            "Clifton Red Bin Bar",
            "Clifton Blue Bin Bar",
            "Clifton Blue Bin EZ Mart",
            "Clifton Red Bin EZ Mart",
        ])
        damton_bins = get_location_names_with_ids([
            "Damton Red Bin Bar",
            "Damton Blue Bin Bar",
            "Damton Red Bin Easy Depot",
            "Damton Blue Bin Easy Depot",
        ])
        smalton_bins = get_location_names_with_ids([
            "Smalton Blue Bin Easy Pizza",
            "Smalton Red Bin Easy Pizza",
            "Smalton Red Bin Easy Eats",
            "Smalton Blue Bin Easy Eats",
        ])

        upton.add_locations(upton_bins, EasyDeliveryCoLocation)
        weston.add_locations(weston_bins, EasyDeliveryCoLocation)
        easton.add_locations(easton_bins, EasyDeliveryCoLocation)
        winton.add_locations(winton_bins, EasyDeliveryCoLocation)
        munton_early.add_locations(munton_early_bins, EasyDeliveryCoLocation)
        munton.add_locations(munton_bins, EasyDeliveryCoLocation)
        lopton.add_locations(lopton_bins, EasyDeliveryCoLocation)
        clifton.add_locations(clifton_bins, EasyDeliveryCoLocation)
        damton.add_locations(damton_bins, EasyDeliveryCoLocation)
        smalton.add_locations(smalton_bins, EasyDeliveryCoLocation)

    mountain_town.add_locations(mountain_town_locations, EasyDeliveryCoLocation)
    snowy_peaks.add_locations(snowy_peaks_locations, EasyDeliveryCoLocation)
    fishing_town.add_locations(fishing_town_locations, EasyDeliveryCoLocation)
    all_towns.add_locations(all_towns_locations, EasyDeliveryCoLocation)
