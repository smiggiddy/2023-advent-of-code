#!/usr/bin/env python


class Almanac:
    def __init__(self, order, maps) -> None:
        self.order = order
        self.maps = maps
        self.seeds = self.maps["seeds"]
        self.location = ...
        self.lowest_location = ""

    def seed_factors(self):
        self.seeds_2 = []

        factors = self.seeds[1::2]
        seeds = self.seeds[::2]

        for i in range(len(seeds)):
            self.seeds_2.append(range(int(seeds[i]), (int(seeds[i]) + int(factors[i]))))
        
        # print(*self.seeds_2[0])
        self.seeds = self.seeds_2

        self.loop_seeds()

    def loop_seeds(self):
        for seed in self.seeds:
            for s in seed:
                print(s)
                self.location = s
                self.map()

                if self.lowest_location == "":
                    self.lowest_location = self.location
                elif self.location < int(self.lowest_location):
                    self.lowest_location = self.location

        print("LOWEST LOCATION: ", self.lowest_location)

    def map(self):
        for map in self.order:
            self.location = self.get_next(self.maps[map], self.location)

    def get_next(self, map, source):
        """processes the map"""

        for i in map:
            dest = int(i[0])
            src = int(i[1])
            _range = int(i[2])

            dest_range = range(dest, (dest + _range))
            source_range = range(src, (src + _range))

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
    # blocks, title = load_file("./test_input.txt")

    a = Almanac(title, blocks)
    a.seed_factors()
    # a.loop_seeds()
