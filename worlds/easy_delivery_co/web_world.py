from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld
from worlds.easy_delivery_co.options import option_groups


class EasyDeliveryCoWebWorld(WebWorld):
    game = "Easy Delivery Co."

    theme = "ice"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Easy Deliver Co. for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Aeromaze"]
    )

    tutorials = [setup_en]

    option_groups = option_groups
