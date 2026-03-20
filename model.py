from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from agent import Prey, Predator
import random

class PredatorPreyModel(Model):
    def __init__(self, width=20, height=20, initial_prey=20, initial_predators=5):
        super().__init__()
        self.width = width
        self.height = height
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, torus=True)

        # Create prey
        for i in range(initial_prey):
            prey = Prey(self.next_id(), self)
            self.schedule.add(prey)
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            self.grid.place_agent(prey, (x, y))

        # Create predators
        for i in range(initial_predators):
            predator = Predator(self.next_id(), self)
            self.schedule.add(predator)
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            self.grid.place_agent(predator, (x, y))

        # Data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Prey": lambda m: m.count_prey(),
                "Predators": lambda m: m.count_predators()
            }
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def add_prey(self):
        prey = Prey(self.next_id(), self)
        self.schedule.add(prey)
        x = random.randrange(self.width)
        y = random.randrange(self.height)
        self.grid.place_agent(prey, (x, y))

    def add_predator(self):
        predator = Predator(self.next_id(), self)
        self.schedule.add(predator)
        x = random.randrange(self.width)
        y = random.randrange(self.height)
        self.grid.place_agent(predator, (x, y))

    # Helper methods for DataCollector
    def count_prey(self):
        return sum(1 for a in self.schedule.agents if isinstance(a, Prey))

    def count_predators(self):
        return sum(1 for a in self.schedule.agents if isinstance(a, Predator))