from src.models.dish import Dish
from src.models.ingredient import Ingredient

import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        foo = {}
        df = pd.read_csv(source_path)

        for dish, price, ingredient, recipe_amount in df.itertuples(
            index=False
        ):
            food = Dish(dish, price)
            ingredientes = Ingredient(ingredient)
            if food not in foo:
                foo[food] = food

            foo[food].add_ingredient_dependency(ingredientes, recipe_amount)

        self.dishes = set(dishe for dishe in foo)

    def __str__(self) -> str:
        return str(self.dishes)
