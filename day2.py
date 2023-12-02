import re
from utils import read_file

class CubeSetData:
    def __init__(self, cube_data: dict[str, int]):
        self.cube_data = cube_data

    def __str__(self):
        return f'{self.cube_data}'

class CubeGameData:
    def __init__(self, game: int, cube_datasets: list[CubeSetData]):
        self.game = game
        self.cube_datasets = cube_datasets

    def __str__(self):
        data = []
        for cube_data in self.cube_datasets: 
            data.append(cube_data.__str__())
        return f'Game: {self.game}, cube_datasets: {", ".join(data)}'

class Day2:

    def __init__(self, possible_cube: dict[str, int]):
        self.possible_cube = possible_cube

    def format_data(self, input: str) -> CubeGameData:
        game = re.search(r'Game (\d+):', input).group(1)
        remove_game = input.split(':')[1]

        all_sets = remove_game.split(';')

        game_data = CubeGameData(game, [])

        for set in all_sets:
            all_cubes = set.split(',')
            set_dict = {}
            for cube in all_cubes:
                if cube.find('red') != -1:
                    red_count = cube.replace('red', '').strip()
                    set_dict['red'] = int(red_count)
                elif cube.find('green') != -1:
                    green_count = cube.replace('green', '').strip()
                    set_dict['green'] = int(green_count)
                elif cube.find('blue') != -1:
                    blue_count = cube.replace('blue', '').strip()
                    set_dict['blue'] = int(blue_count)
            game_data.cube_datasets.append(CubeSetData(set_dict))
        return game_data
    
    # return 0 if invalid cube
    # return game_id if valid cube
    def valid_cube_in_game(self, cube_data: CubeGameData) -> int:
        for cube_set in cube_data.cube_datasets:
            for cube in cube_set.cube_data:
                if cube_set.cube_data[cube] > self.possible_cube[cube]:
                    return 0
        return cube_data.game
    
    def find_fewest_cubes(self, cube_data: CubeGameData) -> int:
        min_red = 0
        min_blue = 0
        min_green = 0

        for cube_set in cube_data.cube_datasets:
            min_red = max(min_red, cube_set.cube_data.get('red', 0))
            min_blue = max(min_blue, cube_set.cube_data.get('blue', 0))
            min_green = max(min_green, cube_set.cube_data.get('green', 0))
        
        return min_red * min_blue * min_green
            
    

    def determine_cube(self, lines: list[str]):

        sum_part_1 = 0
        sum_part_2 = 0
        
        for line in lines:
            formatted_data = self.format_data(line)
            sum_part_1 += int(self.valid_cube_in_game(formatted_data))

            sum_part_2 += int(self.find_fewest_cubes(formatted_data))

        return (sum_part_1, sum_part_2)





day2 = Day2({'red': 12, 'green': 13, 'blue': 14})

inputs = read_file('input_data/day_2.txt')

print(day2.determine_cube(inputs))

