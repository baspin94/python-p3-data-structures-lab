""" import ipdb """

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food.get("name") for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spicy_foods = [food for food in spicy_foods if food.get("heat_level") > 5]
    return spicy_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name")
        cuisine = food.get("cuisine")
        heat = food.get("heat_level") * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    foods_to_print = get_spiciest_foods(spicy_foods)
    print_spicy_foods(foods_to_print)

def get_average_heat_level(spicy_foods):
    heat = [food.get("heat_level") for food in spicy_foods]
    total_heat = sum(heat)
    avg_heat = total_heat/len(heat)
    return avg_heat

spicy_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

""" ipdb.set_trace() """