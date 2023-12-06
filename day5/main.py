#!/usr/bin/env python


# TODO implement method to test if seed number corresponds to
# move input into desired dataset
# soil number inside of maps
# create generator for source/destinations
# output from each map corresponds to the next map
# return lowest location number
class Almanac:
    def __init__(self, order, maps) -> None:
        self.order = order
        self.maps = maps
        self.seeds = self.maps['seeds']
        self.location = ...

    def seed_factors(self):
        self.seeds_2 = []
        seed_combos = [(self.seeds[0], self.seeds[1]), (self.seeds[2], self.seeds[3])]
        for seed in seed_combos:
            seeds = range(int(seed[0]), (int(seed[0])+int(seed[1])))

            self.seeds_2.append([*seeds])

        self.seeds = [] 

        for l in self.seeds_2:
            self.seeds += l

        self.loop_seeds()

    def loop_seeds(self):
        
        lowest_location = ""
        for seed in self.seeds:
            self.location = int(seed)
            print(f"SEED: {seed}")
            self.map()

            if lowest_location == "":
                lowest_location = self.location
            elif self.location < lowest_location:
                lowest_location = self.location 

        print('LOWEST LOCATION: ', lowest_location)

    def map(self):
        for map in self.order:
            # print(map)
            self.location = self.get_next(self.maps[map], self.location)
            # print(self.location)

    def get_next(self, map, source):
        """processes the map"""

        for i in map:
            dest = int(i[0])
            src = int(i[1])
            _range = int(i[2])
            
            dest_range = range(dest, (dest+_range))
            source_range = range(src, (src+_range))
            
            if source in source_range:
                source_index = source_range.index(source)
                dest_location = dest_range[source_index]
                return dest_location

        return source


def load_file(file):
    """
    :returns file data by reading lines
    """

    with open(file) as f:
        data = f.readlines()
    order = []
    blocks = {}
    title = ""
    for line in data:
        if line == "\n":
            continue
        elif "-" in line:
            title = line.split()[0]
            blocks[title] = []
            order.append(title)
        elif "seed" in line:
            name = line.strip(":").split()[0][:5]
            blocks[name] = line.strip().split()[1:]
            continue
        else:
            if title in blocks:
                blocks[title].append(line.strip().split())

    return blocks, order


if __name__ == "__main__":
    blocks, title = load_file("./input.txt")

    a = Almanac(title, blocks)
    a.seed_factors()
    # a.loop_seeds()
