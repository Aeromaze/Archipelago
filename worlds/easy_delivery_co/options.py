from dataclasses import dataclass

from Options import Toggle, PerGameCommonOptions, OptionGroup, Choice


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


@dataclass
class EasyDeliveryCoOptions(PerGameCommonOptions):
    payload_checks: PayloadChecks
    perfect_deliveries: PerfectDeliveries
    blind_bags: BlindBags
    snowcats: Snowcats


option_groups = [
    OptionGroup(
        "Locations",
        [PayloadChecks, PerfectDeliveries, BlindBags, Snowcats]
    )
]
