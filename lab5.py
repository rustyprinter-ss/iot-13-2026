class Fish:
    def __init__(self, name="Невідомо", age=0, species="Невідомо", size=0.0,
                 preferred_food="Невідомо", is_aggressive=False,
                 needed_space=0.0):
        self.__name = name
        self.__age = age
        self.__species = species
        self.__size = size
        self.__preferred_food = preferred_food
        self.__is_aggressive = is_aggressive
        self.__needed_space = needed_space

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def get_size(self):
        return self.__size

    def get_preferred_food(self):
        return self.__preferred_food

    def is_aggressive(self):
        return self.__is_aggressive

    def get_needed_space(self):
        return self.__needed_space

    def __str__(self):
        if self.__is_aggressive:
            temper = "агресивна"
        else:
            temper = "мирна"
        text = f"{self.__name} ({self.__species}), вік {self.__age} р., "
        text += f"розмір {self.__size} см, їсть: {self.__preferred_food}, "
        text += f"{temper}, потрібно місця: {self.__needed_space} м³"
        return text

    def __repr__(self):
        return (f"Fish({self.__name!r}, {self.__age}, {self.__species!r}, "
                f"{self.__size}, {self.__preferred_food!r}, "
                f"{self.__is_aggressive}, {self.__needed_space})")

    def __del__(self):
        print("Рибку видалено:", self.__name)


class Aquarium:
    def __init__(self, total_volume=0.0):
        self.__total_volume = total_volume
        self.__free_space = total_volume
        self.__fishes = []

    def get_total_volume(self):
        return self.__total_volume

    def get_free_space(self):
        return self.__free_space

    def get_fishes(self):
        return self.__fishes

    def add_fish(self, fish):
        if len(self.__fishes) > 0:
            first_fish = self.__fishes[0]
            if fish.is_aggressive() != first_fish.is_aggressive():
                print("Не можна додати", fish.get_name(), "- різний характер")
                return False
        if fish.get_needed_space() > self.__free_space:
            print("Не можна додати", fish.get_name(), "- немає місця")
            return False
        self.__fishes.append(fish)
        self.__free_space -= fish.get_needed_space()
        print("Додано:", fish.get_name())
        return True

    def get_largest_fishes(self):
        fishes = list(self.__fishes)
        for i in range(len(fishes)):
            for j in range(i + 1, len(fishes)):
                if fishes[j].get_size() > fishes[i].get_size():
                    fishes[i], fishes[j] = fishes[j], fishes[i]
        return fishes[:3]

    def print_largest_fishes(self): 
        print("Три найбільші рибки:")
        for fish in self.get_largest_fishes():
            print("  ", fish.get_name(), "-", fish.get_size(), "см")

    def __str__(self):
        return (f"Акваріум: об'єм {self.__total_volume} м³, "
                f"вільно {self.__free_space:.2f} м³, "
                f"рибок: {len(self.__fishes)}")

    def __repr__(self):
        return f"Aquarium({self.__total_volume})"

    def __del__(self):
        print("Акваріум видалено, об'єм:", self.__total_volume)


def print_aquarium(aquarium):
    print(aquarium)
    for fish in aquarium.get_fishes():
        print("  -", fish)
    aquarium.print_largest_fishes()
    print()


def main():
    goldfish = Fish("Золота рибка", 3, "Goldfish", 15.0, "пластівці",
                    False, 0.08)
    neon = Fish("Неон", 1, "Neon tetra", 4.0, "дафнії", False, 0.01)
    angel = Fish("Скалярія", 2, "Angelfish", 12.0, "мотиль", False, 0.06)
    guppy = Fish("Гуппі", 1, "Guppy", 5.0, "пластівці", False, 0.01)
    koi = Fish("Короп кої", 5, "Koi", 40.0, "гранули", False, 0.25)

    piranha = Fish("Піранья", 4, "Red-bellied piranha", 25.0, "м'ясо",
                   True, 0.10)
    oscar = Fish("Оскар", 3, "Astronotus ocellatus", 30.0, "креветки",
                 True, 0.12)
    betta = Fish("Півник", 1, "Betta splendens", 7.0, "личинки комарів",
                 True, 0.03)
    devil = Fish("Червоний диявол", 4, "Amphilophus labiatus", 28.0,
                 "креветки", True, 0.09)

    print("Рибка за замовчуванням:", Fish())
    print()

    print("Акваріум 1 (мирні рибки)")
    aquarium1 = Aquarium(0.3)
    aquarium1.add_fish(goldfish)
    aquarium1.add_fish(neon)
    aquarium1.add_fish(angel)
    aquarium1.add_fish(guppy)
    aquarium1.add_fish(koi)
    aquarium1.add_fish(piranha)
    print()
    print_aquarium(aquarium1)

    print("Акваріум 2 (агресивні рибки)")
    aquarium2 = Aquarium(0.27)
    aquarium2.add_fish(piranha)
    aquarium2.add_fish(oscar)
    aquarium2.add_fish(betta)
    aquarium2.add_fish(devil)
    aquarium2.add_fish(neon)
    print()
    print_aquarium(aquarium2)

    print("Кінець main")


if __name__ == "__main__":
    main()
