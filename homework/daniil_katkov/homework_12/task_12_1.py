from operator import attrgetter


class Flowers:
    def __init__(self, name, freshness, colour, stem_length, lifespan, cost):
        self.name = name
        self.freshness = freshness
        self.colour = colour
        self.stem_length = stem_length
        self.lifespan = lifespan
        self.cost = cost


    def wilt_time(self):
        return f'Время увядания для {self.name} - {self.lifespan}'

    def __str__(self):
        return (f"{self.colour} {self.name} (стебель: {self.stem_length}см,"
                f" цена: ${self.cost}, живёт {self.freshness} дней)")


class Roses(Flowers):
    def __init__(self, freshness, colour, stem_length, cost):
        super().__init__('Роза', freshness, colour, stem_length, 4, cost)


class Peonies(Flowers):
    def __init__(self, freshness, colour, stem_length, cost):
        super().__init__('Пиона', freshness, colour, stem_length, 8, cost)

class Buttercups(Flowers):
    def __init__(self, freshness, colour, stem_length, cost):
        super().__init__('Лютик', freshness, colour, stem_length, 12, cost)

class Bouquets:
    def __init__(self):
        self.flowers = []


    def add_flower(self, flower):
        self.flowers.append(flower)


    def flower_price(self):
        return sum(flower.cost for flower in self.flowers)


    def time_to_finish(self):
        return round((sum(flower.freshness for flower in self.flowers) / len(self.flowers)), 2)


    def sort_by_key(self, key):
        self.flowers.sort(key = attrgetter(key))
        return self.flowers


    def search_by(self, attribute, average_value):
        return [flower for flower in self.flowers if getattr(flower, attribute) >= average_value]


red_rose = Roses(3, 'Красная', 50, 3)
white_rose = Roses(3, 'Белая', 55, 4)
pink_rose = Roses(4, 'Розовая', 40, 5)
peon = Peonies(5, 'Розовая', 45, 2)
buttercup = Buttercups(8, 'Жёлтая', 35, 1)


bouquet = Bouquets()
bouquet.add_flower(red_rose)
bouquet.add_flower(white_rose)
bouquet.add_flower(pink_rose)
bouquet.add_flower(peon)
bouquet.add_flower(buttercup)

sorted_flowers = bouquet.sort_by_key('cost')
for flower in sorted_flowers:
    print(flower)

print(bouquet.flower_price())
print(bouquet.time_to_finish())

for flower in bouquet.search_by('stem_length', 45):
    print(flower)

