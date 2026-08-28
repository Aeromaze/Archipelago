from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import HasAll, Rule, HasAny, Has, CanReachRegion
from . import locations
from .options import BlockedTunnels, CarUpgrades, RequireHandheldRadio

if TYPE_CHECKING:
    from .world import EasyDeliveryCoWorld


def set_all_rules(world: EasyDeliveryCoWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def has_snow_tires(world: "EasyDeliveryCoWorld"):
    if world.options.car_upgrades == 0:
        if world.options.blocked_tunnels == 1:
            return HasAll("Lighter", "Snow Tires", "Snowy Peaks Tunnel")
        else:
            return HasAll("Lighter", "Snow Tires")
    else:
        return Has("Snow Tires")


def can_open_ft_gate(world: "EasyDeliveryCoWorld"):
    if world.options.radio_towers == 1 or world.options.radio_towers == 3:
        return Has("Radio Tower", count=3) & Has("Bumper Bar")
    else:
        return CanReachRegion("Snowy Peaks") & Has("Bumper Bar")


def set_all_entrance_rules(world: EasyDeliveryCoWorld) -> None:
    mountain_town_to_snowy_peaks_tunnel = world.get_entrance("Mountain Town to Snowy Peaks tunnel")
    snowy_peaks_tunnel_to_snowy_peaks_early = world.get_entrance("Snowy Peaks tunnel to Snowy Peaks early")
    snowy_peaks_early_to_snowy_peaks = world.get_entrance("Snowy Peaks early to Snowy Peaks")
    mountain_town_to_fishing_town_tunnel = world.get_entrance("Mountain Town to Fishing Town tunnel")
    fishing_town_entry_to_fishing_town = world.get_entrance("Fishing Town entry to Fishing Town")
    snowy_peaks_to_all_towns = world.get_entrance("Snowy Peaks to All towns")

    world.set_rule(snowy_peaks_tunnel_to_snowy_peaks_early,
             Has("Snow Tires"))
    world.set_rule(snowy_peaks_early_to_snowy_peaks,
                   has_snow_tires(world))
    world.set_rule(fishing_town_entry_to_fishing_town,
                   can_open_ft_gate(world))

    if world.options.blocked_tunnels == 0 or world.options.blocked_tunnels == 2:
        world.set_rule(mountain_town_to_snowy_peaks_tunnel,
                 Has("Lighter"))
        world.set_rule(mountain_town_to_fishing_town_tunnel,
                       has_snow_tires(world))
    elif world.options.blocked_tunnels == 1:
        world.set_rule(mountain_town_to_snowy_peaks_tunnel,
                 HasAll("Lighter", "Snowy Peaks Tunnel"))
        world.set_rule(mountain_town_to_fishing_town_tunnel,
                       Has("Fishing Town Tunnel") & has_snow_tires(world))

    world.set_rule(snowy_peaks_to_all_towns,
             CanReachRegion("Fishing Town"))


def set_all_location_rules(world: EasyDeliveryCoWorld) -> None:
    if world.options.snowcats != 0:
        snowcat_tooey = world.get_location("Snowcat Tooey")
        snowcat_gus = world.get_location("Snowcat Gus")
        snowcat_ellie = world.get_location("Snowcat Ellie")
        snowcat_fortino = world.get_location("Snowcat Fortino")
        snowcat_fit = world.get_location("Snowcat Fit")
        world.set_rule(snowcat_tooey,
                       has_snow_tires(world))
        world.set_rule(snowcat_gus,
                       has_snow_tires(world))
        world.set_rule(snowcat_ellie,
                       has_snow_tires(world))
        world.set_rule(snowcat_fortino,
                       has_snow_tires(world))
        world.set_rule(snowcat_fit,
                 Has("Ice Chains"))

    if world.options.radio_towers == 1 or world.options.radio_towers == 2:
        radio_easton = world.get_location("Easton Radio Tower")
        radio_ft = world.get_location("Fishing Town Radio Tower")
        world.set_rule(radio_easton,
                 HasAny("Lighter", "Snow Tires"))
        world.set_rule(radio_ft,
                 HasAll("Ice Chains", "Bumper Bar"))

    if world.options.lock_towns == 1:
        if world.options.intercity_deliveries == 2 or world.options.intercity_deliveries == 3:
            has_snowy_peaks: Rule = HasAny("Winton", "Munton", "Lopton")
            has_fishing_town: Rule = HasAny("Clifton", "Smalton", "Damton")
            has_both_cities: Rule = has_snowy_peaks & has_fishing_town
            if world.options.perfect_deliveries == 0 or world.options.perfect_deliveries == 1:
                world.set_rule(world.get_location("Mountain Town to Snowy Peaks Delivery"),
                                has_snowy_peaks)
                world.set_rule(world.get_location("Snowy Peaks to Snowy Peaks Delivery"),
                                has_snowy_peaks)
                world.set_rule(world.get_location("Snowy Peaks to Mountain Town Delivery"),
                                has_snowy_peaks)
                world.set_rule(world.get_location("Mountain Town to Fishing Town Delivery"),
                                has_fishing_town)
                world.set_rule(world.get_location("Fishing Town to Fishing Town Delivery"),
                                has_fishing_town)
                world.set_rule(world.get_location("Fishing Town to Mountain Town Delivery"),
                                has_fishing_town)
                world.set_rule(world.get_location("Snowy Peaks to Fishing Town Delivery"),
                                has_both_cities)
                world.set_rule(world.get_location("Fishing Town to Snowy Peaks Delivery"),
                                has_both_cities)
            if world.options.perfect_deliveries == 1 or world.options.perfect_deliveries == 2:
                world.set_rule(world.get_location("Mountain Town to Snowy Peaks Perfect Delivery"),
                                has_snowy_peaks)
                world.set_rule(world.get_location("Snowy Peaks to Snowy Peaks Perfect Delivery"),
                                has_snowy_peaks)
                world.set_rule(world.get_location("Snowy Peaks to Mountain Town Perfect Delivery"),
                                has_snowy_peaks)
                world.set_rule(world.get_location("Mountain Town to Fishing Town Perfect Delivery"),
                                has_fishing_town)
                world.set_rule(world.get_location("Fishing Town to Fishing Town Perfect Delivery"),
                                has_fishing_town)
                world.set_rule(world.get_location("Fishing Town to Mountain Town Perfect Delivery"),
                                has_fishing_town)
                world.set_rule(world.get_location("Snowy Peaks to Fishing Town Perfect Delivery"),
                                has_both_cities)
                world.set_rule(world.get_location("Fishing Town to Snowy Peaks Perfect Delivery"),
                                has_both_cities)
        if world.options.intercity_deliveries == 1 or world.options.intercity_deliveries == 3:
            for startTown in locations.TOWN_NAME_TO_ID:
                for endTown in locations.TOWN_NAME_TO_ID:
                    has_towns: Rule = HasAll(startTown, endTown)
                    if world.options.perfect_deliveries == 0 or world.options.perfect_deliveries == 1:
                        world.set_rule(world.get_location(startTown + " to " + endTown + " Delivery"),
                                 has_towns)
                    if world.options.perfect_deliveries == 1 or world.options.perfect_deliveries == 2:
                        world.set_rule(world.get_location(startTown + " to " + endTown + " Perfect Delivery"),
                                 has_towns)
        else:
            for startTown in locations.MOUNTAIN_TOWN_NAMES:
                for endTown in locations.MOUNTAIN_TOWN_NAMES:
                    has_towns: Rule = HasAll(startTown, endTown)
                    if world.options.perfect_deliveries == 0 or world.options.perfect_deliveries == 1:
                        world.set_rule(world.get_location(startTown + " to " + endTown + " Delivery"),
                                 has_towns)
                    if world.options.perfect_deliveries == 1 or world.options.perfect_deliveries == 2:
                        world.set_rule(world.get_location(startTown + " to " + endTown + " Perfect Delivery"),
                                 has_towns)
            for startTown in locations.SNOWY_PEAKS_NAMES:
                for endTown in locations.SNOWY_PEAKS_NAMES:
                    has_towns: Rule = HasAll(startTown, endTown)
                    if world.options.perfect_deliveries == 0 or world.options.perfect_deliveries == 1:
                        world.set_rule(world.get_location(startTown + " to " + endTown + " Delivery"),
                                 has_towns)
                    if world.options.perfect_deliveries == 1 or world.options.perfect_deliveries == 2:
                        world.set_rule(world.get_location(startTown + " to " + endTown + " Perfect Delivery"),
                                 has_towns)
            for startTown in locations.FISHING_TOWN_NAMES:
                for endTown in locations.FISHING_TOWN_NAMES:
                    has_towns: Rule = HasAll(startTown, endTown)
                    if world.options.perfect_deliveries == 0 or world.options.perfect_deliveries == 1:
                        world.set_rule(world.get_location(startTown + " to " + endTown + " Delivery"),
                                 has_towns)
                    if world.options.perfect_deliveries == 1 or world.options.perfect_deliveries == 2:
                        world.set_rule(world.get_location(startTown + " to " + endTown + " Perfect Delivery"),
                                 has_towns)

        if world.options.payload_checks == 1:
            has_easy_flowers: Rule = Has("Upton") \
                           | (Has("Winton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Smalton") & CanReachRegion("Fishing Town"))
            has_easy_eats: Rule = Has("Upton") \
                           | (Has("Winton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Smalton") & CanReachRegion("Fishing Town"))
            has_ez_bakery: Rule = Has("Weston") \
                           | (Has("Lopton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Damton") & CanReachRegion("Fishing Town"))
            has_bar: Rule = Has("Weston") \
                           | (HasAny("Munton", "Lopton") & CanReachRegion("Snowy Peaks")) \
                           | (HasAny("Damton","Clifton") & CanReachRegion("Fishing Town"))
            has_easy_depot: Rule = Has("Weston") \
                           | (Has("Lopton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Damton") & CanReachRegion("Fishing Town"))
            has_ez_cafe: Rule = Has("Weston") \
                           | (Has("Lopton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Damton") & CanReachRegion("Fishing Town"))
            has_easy_pizza: Rule = Has("Easton") \
                           | (Has("Lopton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Smalton") & CanReachRegion("Fishing Town"))
            has_pawn_shop: Rule = Has("Easton") \
                           | (Has("Munton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Clifton") & CanReachRegion("Fishing Town"))
            has_ez_auto: Rule = Has("Easton") \
                           | (Has("Munton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Clifton") & CanReachRegion("Fishing Town"))
            has_ez_mart: Rule = Has("Easton") \
                           | (Has("Munton") & CanReachRegion("Snowy Peaks")) \
                           | (Has("Clifton") & CanReachRegion("Fishing Town"))

            world.set_rule(world.get_location("Deliver Big Box"),
                           has_ez_bakery | has_easy_depot | has_ez_cafe | has_pawn_shop | has_ez_auto | has_ez_mart)
            world.set_rule(world.get_location("Deliver Big Box Stack"),
                           has_ez_bakery | has_easy_depot | has_ez_cafe | has_ez_auto | has_ez_mart)
            world.set_rule(world.get_location("Deliver Box Bunch"),
                           has_easy_eats | has_ez_bakery | has_easy_depot | has_ez_cafe | has_pawn_shop | has_ez_auto | has_ez_mart)
            world.set_rule(world.get_location("Deliver Box Stack"),
                           has_easy_eats | has_ez_bakery | has_easy_depot | has_ez_cafe | has_pawn_shop | has_ez_auto | has_ez_mart)
            world.set_rule(world.get_location("Deliver Crate"),
                           has_easy_depot | has_pawn_shop | has_ez_mart)
            world.set_rule(world.get_location("Deliver Crate of Drinks"),
                           has_easy_eats | has_bar | has_easy_depot | has_ez_cafe | has_ez_mart)
            world.set_rule(world.get_location("Deliver Crate Stack"),
                           has_easy_depot | has_pawn_shop | has_ez_mart)
            world.set_rule(world.get_location("Deliver Lots of Crates of Drinks"),
                           has_bar)
            world.set_rule(world.get_location("Deliver Pizza Stack"),
                           has_easy_eats | has_easy_pizza)
            world.set_rule(world.get_location("Deliver Pizza Stack Mega"),
                           has_easy_eats | has_easy_pizza)
            world.set_rule(world.get_location("Deliver Plant Pot"),
                           has_easy_flowers | has_pawn_shop)
            world.set_rule(world.get_location("Deliver Plant Pot Bunch"),
                           has_easy_flowers | has_pawn_shop)
            world.set_rule(world.get_location("Deliver Plant Pot Stack"),
                           has_easy_flowers | has_pawn_shop)
            world.set_rule(world.get_location("Deliver Plant Pot Wide"),
                           has_easy_flowers | has_pawn_shop)
            world.set_rule(world.get_location("Deliver Sack"),
                           has_easy_flowers | has_ez_bakery | has_easy_depot | has_ez_cafe | has_ez_mart)
            world.set_rule(world.get_location("Deliver Sack Stack"),
                           has_easy_flowers | has_ez_bakery | has_easy_depot | has_ez_cafe | has_ez_mart)
            world.set_rule(world.get_location("Deliver Drink"),
                           has_bar)


# TODO Consider changing to victory event
def set_completion_condition(world: EasyDeliveryCoWorld) -> None:
    tunnels_not_blocked = OptionFilter(BlockedTunnels, False)
    upgrades_received_directly = OptionFilter(CarUpgrades, 1)
    handheld_radio_not_required = OptionFilter(RequireHandheldRadio, False)

    world.set_completion_rule(HasAll("Ice Chains", "Bumper Bar")
                              & ((upgrades_received_directly and handheld_radio_not_required) | CanReachRegion("Fishing Town"))
                              & (tunnels_not_blocked | Has("Factory Tunnel")))
