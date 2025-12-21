from dataclasses import dataclass

from Options import Toggle, PerGameCommonOptions, OptionGroup


class PayloadChecks(Toggle):
    """
    Enable locations for delivering each type of payload
    """
    display_name = "Payload Checks"


@dataclass
class EasyDeliveryCoOptions(PerGameCommonOptions):
    payload_checks: PayloadChecks


option_groups = [
    OptionGroup(
        "Locations",
        [PayloadChecks]
    )
]
