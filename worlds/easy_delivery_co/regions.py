from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld


def create_and_connect_regions(world: EasyDeliveryCoWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: EasyDeliveryCoWorld) -> None:
    upton = Region("Upton", world.player, world.multiworld)
    mountain_town = Region("Mountain Town", world.player, world.multiworld)
    snowy_peaks = Region("Snowy Peaks", world.player, world.multiworld)
    fishing_town = Region("Fishing Town", world.player, world.multiworld)
    all_towns = Region("All towns", world.player, world.multiworld)

    regions = [upton, mountain_town, snowy_peaks, fishing_town, all_towns]

    world.multiworld.regions += regions


def connect_regions(world: EasyDeliveryCoWorld) -> None:
    mountain_town = world.get_region("Mountain Town")
    snowy_peaks = world.get_region("Snowy Peaks")
    fishing_town = world.get_region("Fishing Town")
    all_towns = world.get_region("All towns")

    mountain_town.connect(snowy_peaks, "Mountain Town to Snowy Peaks")
    mountain_town.connect(fishing_town, "Mountain Town to Fishing Town")
    mountain_town.connect(all_towns, "Mountain Town to All towns")
