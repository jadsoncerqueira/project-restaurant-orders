from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    first_dish = Dish("lasanha presunto", 25.90)
    second_dish = Dish("lasanha berinjela", 27.00)
    third_dish = Dish("lasanha berinjela", 27.00)
    first_ingredient = Ingredient("manteiga")
    second_ingredient = Ingredient("bacon")
    first_dish.add_ingredient_dependency(first_ingredient, 1)
    second_dish.add_ingredient_dependency(second_ingredient, 2)

    # a classe pode ser instanciada corretamente

    assert first_dish.name == "lasanha presunto"
    assert first_dish.price == 25.90
    assert second_dish.name == "lasanha berinjela"
    assert second_dish.price == 27.00

    # os métodos da classe, inclusive os métodos mágicos, funcionem

    # __repr__
    assert repr(first_dish) == "Dish('lasanha presunto', R$25.90)"
    assert repr(second_dish) == "Dish('lasanha berinjela', R$27.00)"

    # __eq__
    assert first_dish != second_dish
    assert second_dish == third_dish

    # __hash__
    assert hash(first_dish) != hash(second_dish)
    assert hash(second_dish) == hash(third_dish)

    # add_ingredient_dependency
    assert first_dish.recipe == {first_ingredient: 1}
    assert second_dish.recipe == {second_ingredient: 2}

    # get_restrictions
    assert first_dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
    }

    # get_ingredients
    assert first_dish.get_ingredients() == {first_ingredient}
    assert second_dish.get_ingredients() == {second_ingredient}

    # são levantados erros ao criar pratos inválidos

    with pytest.raises(ValueError):
        Dish("lasanha presuto", -5.0)

    with pytest.raises(TypeError):
        Dish("Lasanha", "50.0")
