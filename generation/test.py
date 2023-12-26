import names
from models import Person, Region, Land
from db_functions import DBEngine as DBE


def generate_population(population_size):
    population = []
    for i in range(population_size):
        population.append(Person(name=names.get_full_name()))
    return DBE.get_all(Person)


def generate_regions(span):
    regions = []
    for x in range(span):
        for y in range(span):
            regions.append(Region(x_position=x, y_position=y))
    DBE.batch_insert(regions)


def generate_lands(span):
    generate_regions(span)
    lands = []
    map = {}
    for region in DBE.get_all(Region):
        for x in range(span):
            for y in range(span):
                lands.append(Land(x_position=x, y_position=y, region=region.id))
                if region.id not in map.keys():
                    map[region.id] = [(x, y)]
                else:
                    map[region.id].append((x, y))
    print(map)
    DBE.batch_insert(lands)
    return map


map = generate_lands(10)
