from dataclasses import dataclass
import random

from Options import Toggle, PerGameCommonOptions, OptionGroup, Choice, DefaultOnToggle, Range, OptionError, TextChoice
from worlds.AutoWorld import World


class PayloadChecks(Toggle):
    """
    Enable locations for delivering each type of payload.
    """
    display_name = "Payload Checks"


class PerfectDeliveries(Choice):
    """
    Enable locations for delivering without any recoveries.
    """
    display_name = "Perfect Deliveries"

    option_off = 0
    option_on = 1
    option_only = 2

    default = option_off


class IntercityDeliveries(Choice):
    """
    Enable locations for intercity deliveries.

    Off - No locations for intercity deliveries
    Town - Adds locations for intercity deliveries between each town (i.e. Winton to Easton Delivery)
    City - Adds locations for intercity deliveries between each city (i.e. Snowy Peaks to Mountain Town Delivery)
    Both - Adds the locations from both options
    """
    display_name = "Intercity Deliveries"

    option_off = 0
    option_town = 1
    option_city = 2
    option_both = 3

    default = option_town


class LockTowns(Toggle):
    """
    Lock deliveries to and from a town behind an item. Starts with a random town in Mountain Town.
    """
    display_name = "Lock Towns"


class BlindBags(Toggle):
    """
    Enable locations for buying blind bags.
    """
    display_name = "Blind Bags"


class Snowcats(Choice):
    """
    Enable locations for snowcats.

    Exclude Easton - Exclude the snowcat in Easton
    """
    display_name = "Snowcats"

    option_off = 0
    option_on = 1
    option_exclude_easton = 2

    default = option_off


class RadioTowers(Choice):
    """
    Enable locations for radio towers.
    Receiving radio towers as items is WIP.
    """
    display_name = "Radio Towers"

    option_off = 0
    option_on = 1
    option_only_checks = 2
    option_only_items = 3

    default = option_off


class CarUpgrades(Choice):
    """
    How car upgrades should work when received.

    Require Buying - You will still have to buy the upgrade after receiving it
    Receive Directly - The upgrade will be installed immediately
    """
    display_name = "Car Upgrades"

    option_require_buying = 0
    option_receive_directly = 1

    default = option_require_buying


class ProgressiveCarUpgrades(Toggle):
    """
    Receive car upgrades in order (Snow Tires, Bumper Bar, Ice Chains)
    """
    display_name = "Progressive Car Upgrades"


class BlockedTunnels(Choice):
    """
    Require an item to travel through a tunnel.

    Factory Only - Only require an item for the tunnel to Factory
    """
    display_name = "Blocked Tunnels"

    option_off = 0
    option_on = 1
    option_factory_only = 2

    default = option_off


class RequireHandheldRadio(DefaultOnToggle):
    """
    Require having the Handheld Radio to enter the factory.
    """
    display_name = "Require Handheld Radio"


class TrapPercentage(Range):
    """
    Replace a percentage of filler with traps.
    """
    display_name = "Trap Percentage"

    range_start = 0
    range_end = 100

    default = 0


class ColorChoice(TextChoice):
    option_golden = 0xFFD65C
    option_fire_red = 0xFF0000
    option_maroon = 0x800000
    option_salmon = 0xFF3A65
    option_orange = 0xD86E0A
    option_lime_green = 0x8DF920
    option_bright_green = 0x0DAF05
    option_forest_green = 0x132818
    option_royal_blue = 0x0036BF
    option_brown = 0xB78726
    option_black = 0x000000
    option_white = 0xFFFFFF
    option_grey = 0x808080
    option_any_color = -1

    @classmethod
    def from_text(cls, text: str) -> Choice:
        text = text.lower()
        if text == "random":
            choice_list = list(cls.name_lookup)
            choice_list.remove(cls.option_any_color)
            return cls(random.choice(choice_list))
        return super().from_text(text)


class RandomizeTrailColor(ColorChoice):
    """
    Randomize the color of the snowtrail when driving.
    The `any_color` option will choose a fully random color
    A custom color entry may be supplied as a 6-character RGB hex color code
    e.g. F542C8
    """
    display_name = "Randomize Trail Color"

    default = ColorChoice.option_white


def resolve_options(world: World):
    if isinstance(world.options.randomize_trail_color.value, str):
        try:
            world.randomize_trail_color = int(world.options.randomize_trail_color.value.strip("#")[:6], 16)
        except ValueError:
            raise OptionError(f"Invalid input for option `randomize_trail_color`:"
                              f"{world.options.randomize_trail_color.value} for "
                              f"{world.player_name}")
    elif world.options.randomize_trail_color.value == ColorChoice.option_any_color:
        world.randomize_trail_color = world.random.randint(0, 0xFFFFFF)
    else:
        world.randomize_trail_color = world.options.randomize_trail_color.value


@dataclass
class EasyDeliveryCoOptions(PerGameCommonOptions):
    payload_checks: PayloadChecks
    perfect_deliveries: PerfectDeliveries
    intercity_deliveries: IntercityDeliveries
    lock_towns: LockTowns
    blind_bags: BlindBags
    snowcats: Snowcats
    radio_towers: RadioTowers
    car_upgrades: CarUpgrades
    progressive_car_upgrades: ProgressiveCarUpgrades
    blocked_tunnels: BlockedTunnels
    require_handheld_radio: RequireHandheldRadio
    trap_percentage: TrapPercentage
    randomize_trail_color: RandomizeTrailColor


option_groups = [
    OptionGroup(
        "Locations",
        [PayloadChecks, PerfectDeliveries, IntercityDeliveries, BlindBags, Snowcats, RadioTowers]
    )
]
