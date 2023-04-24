from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    # o atributo conjunto restrictions é populado como esperado

    first_ingredient = Ingredient("caldo de carne")
    second_ingredient = Ingredient("bacon")
    third_ingredient = Ingredient("manteiga")
    fourth_ingredient = Ingredient("bacon")
    assert Restriction.ANIMAL_DERIVED in first_ingredient.restrictions
    assert Restriction.ANIMAL_DERIVED in second_ingredient.restrictions
    assert Restriction.ANIMAL_MEAT in second_ingredient.restrictions

    # o método mágico __repr__ funcione como esperado

    assert repr(first_ingredient) == "Ingredient('caldo de carne')"
    assert repr(second_ingredient) == "Ingredient('bacon')"

    # o método mágico __eq__ funcione como esperado;

    assert second_ingredient == fourth_ingredient
    assert first_ingredient != third_ingredient

    # o método mágico __hash__ funcione como esperado

    assert hash(second_ingredient) == hash(fourth_ingredient)
    assert hash(first_ingredient) != hash(third_ingredient)

    # validando o nome errado

    assert first_ingredient.name == "caldo de carne"
    assert second_ingredient.name == "bacon"
    assert second_ingredient.name != "manteiga"
