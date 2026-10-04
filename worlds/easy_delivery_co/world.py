from typing import Mapping, Any, Optional

from Options import Option
from worlds.AutoWorld import World
from . import items, locations, options, regions, rules, web_world


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

            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt: Optional[Option] = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
            "options": self.options.as_dict("payload_checks", "perfect_deliveries",
                       "intercity_deliveries", "lock_towns", "blind_bags", "snowcats", "blocked_tunnels",
                       "require_handheld_radio", "radio_towers", "car_upgrades", "progressive_car_upgrades",
                       "randomize_trail_color"),
        }
        return slot_data

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data
