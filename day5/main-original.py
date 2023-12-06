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

    def loop_seeds(self):
        
        lowest_location = ""
        for seed in self.seeds:
            # set self location to seed to start
            self.location = int(seed)
            print(f"SEED: {seed}")
            self.map()
            # print(f"LOCATION: {self.location}")

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
        # print("THIS IS THE SOURCE:", source)

        num_present = False

        for i in map:
            dest = int(i[0])
            src = int(i[1])
            _range = int(i[2])
            
            # steps, num_present = self.number_present(src, _range, source)
            
            dest_range = range(dest, (dest+_range))
            source_range = range(src, (src+_range))
            
            if source in source_range:
                # print(source_range[29])
                # print(dest_range)
                # print(f"INDEX OF SOURCE: {source_range.index(source)}")
                source_index = source_range.index(source)
                # print(f"INDEX OF DEST: {dest_range[source_index]}" )
                dest_location = dest_range[source_index]
                return dest_location

            # if (num_present):
            #     test = self.get_destination(steps, dest)
            #     return test
            # else:
            #     # print('NUM WASN"T PRESENT')
            #     continue

        return source


    def map_sequence(self, start, _range):
        num = int(start)
        while int(num) < int(start)+int(_range):
            yield num
            num += 1
            
    def get_destination(self, steps, start):
        num = int(start)
        count = 0
    
        while count < steps:
            num += 1
            count  +=1
        return num

    def number_present(self, dest, _range, source):
       
        ranges = range(dest, (dest+_range))

        steps = 0
        in_range = self.map_sequence(dest, _range)

        if source in ranges:
            return None, True

        for j in in_range:
            if source == j:
                return steps, True
            steps += 1

        return None, False



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
    a.loop_seeds()
