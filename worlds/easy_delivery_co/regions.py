from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld


def create_and_connect_regions(world: EasyDeliveryCoWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: EasyDeliveryCoWorld) -> None:
    mountain_town = Region("Mountain Town", world.player, world.multiworld)
    snowy_peaks_tunnel = Region("Snowy Peaks tunnel", world.player, world.multiworld)
    snowy_peaks_early = Region("Snowy Peaks early", world.player, world.multiworld)
    snowy_peaks = Region("Snowy Peaks", world.player, world.multiworld)
    fishing_town_tunnel = Region("Fishing Town tunnel", world.player, world.multiworld)
    fishing_town_entry = Region("Fishing Town entry", world.player, world.multiworld)
    fishing_town = Region("Fishing Town", world.player, world.multiworld)
    all_towns = Region("All towns", world.player, world.multiworld)

    regions = [mountain_town, snowy_peaks, fishing_town, all_towns, snowy_peaks_tunnel, snowy_peaks_early,
               fishing_town_tunnel, fishing_town_entry]

    world.multiworld.regions += regions


def connect_regions(world: EasyDeliveryCoWorld) -> None:
    mountain_town = world.get_region("Mountain Town")
    snowy_peaks_tunnel = world.get_region("Snowy Peaks tunnel")
    snowy_peaks_early = world.get_region("Snowy Peaks early")
    snowy_peaks = world.get_region("Snowy Peaks")
    fishing_town_tunnel = world.get_region("Fishing Town tunnel")
    fishing_town_entry = world.get_region("Fishing Town entry")
    fishing_town = world.get_region("Fishing Town")
    all_towns = world.get_region("All towns")

    mountain_town.connect(snowy_peaks_tunnel, "Mountain Town to Snowy Peaks tunnel")
    snowy_peaks_tunnel.connect(snowy_peaks_early, "Snowy Peaks tunnel to Snowy Peaks early")
    snowy_peaks_early.connect(snowy_peaks, "Snowy Peaks early to Snowy Peaks")

    mountain_town.connect(fishing_town_tunnel, "Mountain Town to Fishing Town tunnel")
    fishing_town_tunnel.connect(fishing_town_entry, "Fishing Town tunnel to Fishing Town entry")
    fishing_town_entry.connect(fishing_town, "Fishing Town entry to Fishing Town")

    snowy_peaks.connect(all_towns, "Snowy Peaks to All towns")
