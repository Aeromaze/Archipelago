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


def has_snow_tires(state: CollectionState, world: "EasyDeliveryCoWorld") -> bool:
    if world.options.car_upgrades == 0:
        if world.options.blocked_tunnels == 0 or world.options.blocked_tunnels == 2:
            return state.has_all(("Lighter", "Snow Tires"), world.player)
        elif world.options.blocked_tunnels == 1:
            return state.has_all(("Lighter", "Snow Tires", "Snowy Peaks Tunnel"), world.player)
        else:
            return state.can_reach_region("Snowy Peaks early", world.player)
    else:
        return state.has("Snow Tires", world.player)


def can_open_ft_gate(state: CollectionState, world: "EasyDeliveryCoWorld") -> bool:
    if world.options.radio_towers == 1 or world.options.radio_towers == 3:
        return state.has("Radio Tower", world.player, 3) and state.has("Bumper Bar", world.player)
    else:
        return state.can_reach_region("Snowy Peaks", world.player) and state.has("Bumper Bar", world.player)


def set_all_entrance_rules(world: EasyDeliveryCoWorld) -> None:
    mountain_town_to_snowy_peaks_tunnel = world.get_entrance("Mountain Town to Snowy Peaks tunnel")
    snowy_peaks_tunnel_to_snowy_peaks_early = world.get_entrance("Snowy Peaks tunnel to Snowy Peaks early")
    snowy_peaks_early_to_snowy_peaks = world.get_entrance("Snowy Peaks early to Snowy Peaks")
    mountain_town_to_fishing_town_tunnel = world.get_entrance("Mountain Town to Fishing Town tunnel")
    fishing_town_entry_to_fishing_town = world.get_entrance("Fishing Town entry to Fishing Town")
    snowy_peaks_to_all_towns = world.get_entrance("Snowy Peaks to All towns")

    set_rule(snowy_peaks_tunnel_to_snowy_peaks_early,
             lambda state: state.has("Snow Tires", world.player))
    set_rule(snowy_peaks_early_to_snowy_peaks,
             lambda state: has_snow_tires(state, world))
    set_rule(fishing_town_entry_to_fishing_town,
             lambda state: can_open_ft_gate(state, world))

    if world.options.blocked_tunnels == 0 or world.options.blocked_tunnels == 2:
        set_rule(mountain_town_to_snowy_peaks_tunnel,
                 lambda state: state.has("Lighter", world.player))
        set_rule(mountain_town_to_fishing_town_tunnel,
                 lambda state: has_snow_tires(state, world))
    elif world.options.blocked_tunnels == 1:
        set_rule(mountain_town_to_snowy_peaks_tunnel,
                 lambda state: state.has_all(("Lighter", "Snowy Peaks Tunnel"), world.player))
        set_rule(mountain_town_to_fishing_town_tunnel,
                 lambda state: state.has("Fishing Town Tunnel", world.player) and has_snow_tires(state, world))

    set_rule(snowy_peaks_to_all_towns,
             lambda state: state.can_reach_region("Fishing Town", world.player))


def set_all_location_rules(world: EasyDeliveryCoWorld) -> None:
    if world.options.snowcats != 0:
        snowcat_tooey = world.get_location("Snowcat Tooey")
        snowcat_gus = world.get_location("Snowcat Gus")
        snowcat_ellie = world.get_location("Snowcat Ellie")
        snowcat_fortino = world.get_location("Snowcat Fortino")
        snowcat_foreman = world.get_location("Snowcat Foreman")
        set_rule(snowcat_tooey,
                 lambda state: has_snow_tires(state, world))
        set_rule(snowcat_gus,
                 lambda state: has_snow_tires(state, world))
        set_rule(snowcat_ellie,
                 lambda state: has_snow_tires(state, world))
        set_rule(snowcat_fortino,
                 lambda state: has_snow_tires(state, world))
        set_rule(snowcat_foreman,
                 lambda state: has_snow_tires(state, world) or state.has("Ice Chains", world.player))

    if world.options.radio_towers == 1 or world.options.radio_towers == 2:
        radio_easton = world.get_location("Easton Radio Tower")
        radio_ft = world.get_location("Fishing Town Radio Tower")
        set_rule(radio_easton,
                 lambda state: (state.has_any(("Lighter", "Snow Tires"), world.player)))
        set_rule(radio_ft,
                 lambda state: (state.has_all(("Ice Chains", "Bumper Bar"), world.player)))


# TODO Consider changing to victory event
def set_completion_condition(world: EasyDeliveryCoWorld) -> None:
    if world.options.car_upgrades == 0:
        if world.options.blocked_tunnels == 0:
            world.multiworld.completion_condition[world.player] = \
                lambda state: (state.can_reach_region("Fishing Town", world.player)
                and state.has_all(("Ice Chains", "Bumper Bar"), world.player))
        else:
            world.multiworld.completion_condition[world.player] = \
                lambda state: (state.can_reach_region("Fishing Town", world.player)
                and state.has_all(("Ice Chains", "Factory Tunnel", "Bumper Bar"), world.player))
    else:
        if world.options.require_handheld_radio == 0:
            if world.options.blocked_tunnels == 0:
                world.multiworld.completion_condition[world.player] = \
                    lambda state: state.has_all(("Ice Chains", "Bumper Bar"), world.player)
            else:
                world.multiworld.completion_condition[world.player] = \
                    lambda state: state.has_all(("Ice Chains", "Bumper Bar", "Factory Tunnel"), world.player)
        else:
            if world.options.blocked_tunnels == 0:
                world.multiworld.completion_condition[world.player] = \
                    lambda state: (state.can_reach_region("Fishing Town", world.player)
                    and state.has_all(("Ice Chains", "Bumper Bar"), world.player))
            else:
                world.multiworld.completion_condition[world.player] = \
                    lambda state: (state.can_reach_region("Fishing Town", world.player)
                    and state.has_all(("Ice Chains", "Bumper Bar", "Factory Tunnel"), world.player))
