from utils import read_whole_file_as_string
import sys
from functools import reduce

class Day5:
    def __init__(self, input: str):
        self.seed_to_soid = {}
        self.soid_to_fertilizer = {}
        self.fertilizer_to_water = {}
        self.water_to_light = {}
        self.light_to_temperature = {}
        self.temperature_to_humidity = {}
        self.humidity_to_location = {}
        # self.max_seed = None

        self.inputs = input.split('\n\n')
        self.seeds = self.inputs[0].split(':')[-1].strip().split(' ')

        self.visited_soil = {}
        self.visited_fertilizer = {}
        self.visited_water = {}
        self.visited_light = {}
        self.visited_temperature = {}
        self.visited_humidity = {}

        # self.seed_to_soid = self.generate_source_destination(inputs[1])
        # self.max_seed = max(self.seed_to_soid.keys())
        # self.soid_to_fertilizer = self.generate_source_destination(inputs[2])
        # self.fertilizer_to_water = self.generate_source_destination(inputs[3])
        # self.water_to_light = self.generate_source_destination(inputs[4])
        # self.light_to_temperature = self.generate_source_destination(inputs[5])
        # self.temperature_to_humidity = self.generate_source_destination(inputs[6])
        # self.humidity_to_location = self.generate_source_destination(inputs[7])

    # def generate_source_destination(self, input: str):
    #     print(f'generate data for: {input.split(":")[0]}')
    #     inputs = input.split('\n')[1:]

    #     source_destination = {}
        
    #     for input in inputs:
    #         start_destination, start_source, path_range = input.split(' ')
    #         print(f'generate for input {start_source} to {int(start_source) + int(path_range)}')
    #         for i in range(0, int(path_range)):
    #             source_destination[int(start_source) + i] = int(start_destination) + i

    #     # generate missing mappings
    #     min_source = min(source_destination.keys())
    #     for i in range(0, min_source):
    #         source_destination[i] = i

    #     max_source = self.max_seed if self.max_seed else max(source_destination.keys())
        
    #     for i in range(max(source_destination.keys()) + 1, max_source + 1):
    #         source_destination[i] = i

    #     return source_destination
    
    def find_target(self, input: str, seed: int):

        mappings = input.split('\n')[1:]
        
        in_range = None

        for mapping in mappings:
            start_destination, start_source, path_range = mapping.split(' ')
            if seed >= int(start_source) and seed <= int(start_source) + int(path_range) - 1:
                in_range = [int(start_source), int(start_destination)]
                break

        if in_range:
            return seed - in_range[0] + in_range[1]
        else:
            return seed
        
    def find_location(self, seed: int):
        
        seed_int = seed if isinstance(seed, int) else int(seed)

        soid = self.find_target(self.inputs[1], seed_int)
        fertilizer = self.find_target(self.inputs[2], soid)
        water = self.find_target(self.inputs[3], fertilizer)
        light = self.find_target(self.inputs[4], water)
        temperature = self.find_target(self.inputs[5], light)
        humidity = self.find_target(self.inputs[6], temperature)
        location = self.find_target(self.inputs[7], humidity)

        return location

    
    def part_1(self, seeds: list[int]):
        min_location = sys.maxsize
        
        seed_momorize = {}
        # print(seeds)
        i = 0
        for seed in seeds:
            if i % 100000 == 0:
                print(f'processing seed: {i} - {seed}')
            i += 1
            # does not work with real input: it take too much time to generate the mappings
            # soid = self.seed_to_soid[int(seed)]
            # fertilizer = self.soid_to_fertilizer[soid]
            # water = self.fertilizer_to_water[fertilizer]
            # light = self.water_to_light[water]
            # temperature = self.light_to_temperature[light]
            # humidity = self.temperature_to_humidity[temperature]
            # location = self.humidity_to_location[humidity]
            # all_locations.append(location)

            if seed in seed_momorize:
                continue
            else:
                location = self.find_location(seed)
                seed_momorize[seed] = location
                min_location = min(location, min_location)

        return min_location
    
    def solution(self):

        part_1 = self.part_1(self.seeds)

        part_2 = sys.maxsize

        i = 0
        while i < len(self.seeds):
            print(f'start processing {i}, {i+1}')
            start = int(self.seeds[i])
            end = int(self.seeds[i + 1])
            generated_seeds = [i for i in range(start, start + end)]
            part_2 = min(part_2, self.part_1(generated_seeds))
            i += 2

        return [part_1, part_2]



input_day5 = read_whole_file_as_string('input_data/day_5.txt')

day5 = Day5(input_day5)
print(day5.solution())