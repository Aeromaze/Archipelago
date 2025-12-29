from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from ..generic.Rules import set_rule

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld


def set_all_rules(world: EasyDeliveryCoWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: EasyDeliveryCoWorld) -> None:
    mountain_town_to_snowy_peaks = world.get_entrance("Mountain Town to Snowy Peaks")
    mountain_town_to_fishing_town = world.get_entrance("Mountain Town to Fishing Town")
    mountain_town_to_all_towns = world.get_entrance("Mountain Town to All towns")

    set_rule(mountain_town_to_snowy_peaks, lambda state: state.has_all(("Lighter", "Snow Tires"), world.player))
    set_rule(mountain_town_to_fishing_town, lambda state: state.has_all(("Lighter", "Snow Tires", "Bumper Bar"), world.player))
    set_rule(mountain_town_to_all_towns, lambda state: state.has_all(("Snow Tires", "Lighter", "Bumper Bar"), world.player))


def set_all_location_rules(world: EasyDeliveryCoWorld) -> None:
    if world.options.snowcats != 0:
        snowcat_tooey = world.get_location("Snowcat Tooey")
        snowcat_gus = world.get_location("Snowcat Gus")
        set_rule(snowcat_tooey, lambda state: (state.has("Snow Tires", world.player)))
        set_rule(snowcat_gus, lambda state: (state.has("Snow Tires", world.player)))


def set_completion_condition(world: EasyDeliveryCoWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(("Snow Tires", "Bumper Bar",
                                                                                       "Ice Chains", "Lighter"), world.player)
