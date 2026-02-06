from dataclasses import dataclass

from Options import Toggle, PerGameCommonOptions, OptionGroup, Choice, DefaultOnToggle


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


class BlindBags(Toggle):
    """
    Enable locations for buying blind bags.
    """
    display_name = "Blind Bags"


class Snowcats(Choice):
    """
    Enable locations for snowcats.
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


class BlockedTunnels(Choice):
    """
    Require an item to travel through a tunnel.
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


@dataclass
class EasyDeliveryCoOptions(PerGameCommonOptions):
    payload_checks: PayloadChecks
    perfect_deliveries: PerfectDeliveries
    blind_bags: BlindBags
    snowcats: Snowcats
    radio_towers: RadioTowers
    car_upgrades: CarUpgrades
    blocked_tunnels: BlockedTunnels
    require_handheld_radio: RequireHandheldRadio


option_groups = [
    OptionGroup(
        "Locations",
        [PayloadChecks, PerfectDeliveries, BlindBags, Snowcats, RadioTowers]
    )
]
