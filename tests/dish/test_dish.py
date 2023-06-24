import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    # Garante que o nome passado no construtor está correto no atributo name
    # Garante que o operador de igualdade identifique
    # pratos iguais e diferentes
    dish = Dish('sururu', 25)
    dish2 = Dish("Hambúrguer", 19.99)
    dish3 = Dish("Hambúrguer", 19.99)
    assert dish2 == dish3
    assert dish != dish2
    assert dish.name == 'sururu'
    assert dish.price == 25

    # Garante que o método __repr__ tenha o comportamento esperado
    dish = Dish('sururu', 25)
    assert repr(dish) == "Dish('sururu', R$25.00)"

    # Garante que hashs de pratos diferentes também sejam diferentes
    dish1 = Dish("Risoto", 34.99)
    dish2 = Dish("Risoto", 34.99)
    dish3 = Dish("Salada", 15.99)
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    # Garante que o método add_ingredient_dependency tenha
    # o comportamento esperado
    dish = Dish("Sushi", 42.99)
    ingredient1 = Ingredient("arroz")
    ingredient2 = Ingredient("peixe")
    dish.add_ingredient_dependency(ingredient1, 200)
    dish.add_ingredient_dependency(ingredient2, 150)
    ingredients = dish.get_ingredients()
    assert ingredients == {ingredient1, ingredient2}
    assert dish.recipe == {ingredient1: 200, ingredient2: 150}

    # Garante que o método get_restrictions tenha o comportamento esperado
    dish = Dish("Bolo de Chocolate", 19.99)
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("leite")
    ingredient3 = Ingredient("ovos")
    dish.add_ingredient_dependency(ingredient1, 250)
    dish.add_ingredient_dependency(ingredient2, 500)
    dish.add_ingredient_dependency(ingredient3, 4)
    restrictions = dish.get_restrictions()
    expected_restrictions = {Restriction.GLUTEN}
    assert restrictions == expected_restrictions

    # Garante que o construtor emite TypeError e ValueError quando deveria
    with pytest.raises(TypeError):
        Dish("Macarrão", "invalid")
    with pytest.raises(ValueError):
        Dish("Sopa", 0)
