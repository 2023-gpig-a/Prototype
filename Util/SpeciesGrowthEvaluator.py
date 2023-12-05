import random

import numpy as np
import matplotlib.pyplot as plt


class SpeciesGrowthEvaluator:
    def __init__(self):
        self.maps = []
        self.species_data = {}
    def add(self, other: np.ndarray) -> None:
        if len(self.maps) != 0 and other.size != self.maps[0].size:
            raise ValueError(f"Invalid size of map added, other:{other.size} != {self.maps[0].size}")

        self.maps.append(other)

    def __str__(self) -> str:
        return self.maps.__str__()

    def display_maps(self) -> None:
        figure = plt.figure(figsize=(5, 2))
        figure.suptitle("Graph Showing Species Presence Variation Over Time")
        for i in range(len(self.maps)):
            ax = figure.add_subplot(1, len(self.maps), i+1)
            ax.set_title(f"t={i}")
            plt.axis("off")
            plt.imshow(self.maps[i])
        plt.tight_layout()
        plt.show()

    def evaluate(self):
        unique_species = np.unique(self.maps).tolist()
        for species in unique_species:

            # set up species data
            self.species_data[species] = {
                "count": []
            }

            for i in range(len(self.maps)):
                # count the number of each species at each time stamp
                count_of_species = np.count_nonzero(self.maps[i] == species)
                self.species_data[species]["count"].append(count_of_species)
                print(f"at time t={i}, count of {species} = {count_of_species}")

        # show the growth of each species over time
        figure = plt.figure(figsize=(5, 2*len(unique_species)))
        figure.suptitle("Graph Showing Species Growth With Respect To Time")
        for i, species in enumerate(unique_species):
            ax = figure.add_subplot(len(unique_species), 1, i+1)
            ax.set_title(f"Species: {species}")
            plt.ylabel("Count")
            plt.xlabel("Time")
            plt.plot(range(len(self.maps)), self.species_data[species]["count"])
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":

    # Function to simulate the spread of growth of a plant
    def spread_value(arr: np.ndarray, target: int, grow_chance: float) -> np.ndarray:
        out = arr.copy()
        for i, row in enumerate(arr):
            for j, val in enumerate(row):
                if val == target:
                    if i > 0 and random.random() < grow_chance:
                        out[i-1][j] = val
                    if i < len(arr)-1 and random.random() < grow_chance:
                        out[i+1][j] = val
                    if j > 0 and random.random() < grow_chance:
                        out[i][j-1] = val
                    if j < len(arr[0])-1 and random.random() < grow_chance:
                        out[i][j+1] = val
        return out


    evaluator = SpeciesGrowthEvaluator()
    test_map = np.random.randint(low=0, high=3, size=(50, 50))
    for _ in range(4):
        evaluator.add(test_map)
        test_map = spread_value(test_map, 2, 0.2)

    evaluator.display_maps()
    evaluator.evaluate()

