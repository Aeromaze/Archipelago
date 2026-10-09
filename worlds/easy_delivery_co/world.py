from typing import Mapping, Any, Optional

from Options import Option
from worlds.AutoWorld import World
from . import items, locations, options, regions, rules, web_world
from .options import resolve_options


class EasyDeliveryCoWorld(World):
    """
    Easy Delivery Co. is a game about delivering packages.
    """

    game = "Easy Delivery Co."

    web = web_world.EasyDeliveryCoWebWorld()

    options_dataclass = options.EasyDeliveryCoOptions
    options: options.EasyDeliveryCoOptions
    item_name_groups = items.item_name_groups

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Mountain Town"

    randomize_trail_color: int

    # Universal Tracker
    ut_can_gen_without_yaml = True
    generating_in_ut = False

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.EasyDeliveryCoItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            for key, value in slot_data.items():
                opt: Optional[Option] = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

        resolve_options(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data: dict[str, Any] = {
            "payload_checks": self.options.payload_checks.value,
            "perfect_deliveries": self.options.perfect_deliveries.value,
            "intercity_deliveries": self.options.intercity_deliveries.value,
            "lock_towns": self.options.lock_towns.value,
            "blind_bags": self.options.blind_bags.value,
            "snowcats": self.options.snowcats.value,
            "blocked_tunnels": self.options.blocked_tunnels.value,
            "require_handheld_radio": self.options.require_handheld_radio.value,
            "radio_towers": self.options.radio_towers.value,
            "vending_machines": self.options.vending_machines.value,
            "trash_bins": self.options.trash_bins.value,
            "car_upgrades": self.options.car_upgrades.value,
            "progressive_car_upgrades": self.options.progressive_car_upgrades.value,
            "randomize_trail_color": self.randomize_trail_color,
        }
        return slot_data

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data
