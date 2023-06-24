import csv

from typing import Dict, Set
from models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self._read_menu_data(source_path)

    def _read_menu_data(self, source_path: str) -> None:
        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            dish_data: Dict[str, Dict[str, str]] = {}

            for row in reader:
                dish_name = row['dish']
                ing_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                if dish_name not in dish_data:
                    dish_data[dish_name] = {
                        'price': float(row['price']),
                        'recipe': {ing_name: recipe_amount}
                    }
                else:
                    dish_data[dish_name]['recipe'][ing_name] = recipe_amount

            for dish_name, dish_info in dish_data.items():
                dish = Dish(dish_name, dish_info['price'])
                for ing_name, recipe_amount in dish_info['recipe'].items():
                    ingredient = Ingredient(ing_name)
                    dish.add_ingredient_dependency(ingredient, recipe_amount)
                self.dishes.add(dish)
