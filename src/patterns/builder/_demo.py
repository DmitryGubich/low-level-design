from patterns.builder.menu import VeganMealBuilder, HealthyMealBuilder

if __name__ == "__main__":
    vegan_builder = VeganMealBuilder()
    (vegan_builder.add_starter().add_main_course().add_dessert().add_drink())
    vegan_meal = vegan_builder.build()

    print("Vegan Meal constructed: ")
    print(f"Starter: {vegan_meal.starter.name}")
    print(f"Main: {vegan_meal.main.name}")
    print(f"Dessert: {vegan_meal.dessert.name}")
    print(f"Drink: {vegan_meal.drink.name}\n")

    ##########################################################################

    healthy_builder = HealthyMealBuilder()
    healthy_builder.add_starter().add_main_course().add_dessert().add_drink()
    healthy_meal = healthy_builder.build()

    print("Healthy Meal constructed: ")
    print(f"Starter: {healthy_meal.starter.name}")
    print(f"Main: {healthy_meal.main.name}")
    print(f"Dessert: {healthy_meal.dessert.name}")
    print(f"Drink: {healthy_meal.drink.name}")
