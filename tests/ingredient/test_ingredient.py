from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Garanta que o nome passado no construtor está correto no atributo name
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"

    # Garanta que o atributo restrictions seja preenchido corretamente
    assert ingredient.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}

    # Garanta que o método __repr__ tenha o comportamento esperado
    ingredient = Ingredient("bacon")
    assert repr(ingredient) == "Ingredient('bacon')"

    # Garanta que o operador de igualdade identifique ingredientes iguais
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("bacon")
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("bacon")

    # Garanta que hashs de ingredientes iguais também sejam iguais
    assert hash(ingredient1) == hash(ingredient2)

    # Garanta que hashs de ingredientes diferentes também sejam diferentes
    assert hash(ingredient1) != hash(ingredient3)
