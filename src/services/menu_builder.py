import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def ingredient_inventory(self, recipe):
        return all(
            self.inventory.inventory.get(ingredient, 0) >= item
            for ingredient, item in recipe.items()
        )

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        data = pd.DataFrame
        list = []
        for dish in self.menu_data.dishes:
            if restriction not in dish.get_restrictions():
                if self.ingredient_inventory(dish.recipe):
                    list.append(
                        {
                            "dish_name": dish.name,
                            "ingredients": dish.get_ingredients(),
                            "restrictions": dish.get_restrictions(),
                            "price": dish.price,
                        }
                    )
        return data(
            list,
            columns=[
                "dish_name",
                "ingredients",
                "price",
                "restrictions",
            ],
        )
