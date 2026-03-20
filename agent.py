from mesa import Agent
import random

class Prey(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Move randomly
        self.random_move()
        # Possibly reproduce
        if random.random() < 0.05:
            self.model.add_prey()

    def random_move(self):
        possible_steps = [-1, 0, 1]
        new_x = (self.pos[0] + random.choice(possible_steps)) % self.model.grid.width
        new_y = (self.pos[1] + random.choice(possible_steps)) % self.model.grid.height
        self.model.grid.move_agent(self, (new_x, new_y))


class Predator(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = 10

    def step(self):
        self.random_move()
        self.energy -= 1
        # Eat prey if any on same cell
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        prey_here = [a for a in cellmates if isinstance(a, Prey)]
        if prey_here:
            prey = random.choice(prey_here)
            self.model.grid.remove_agent(prey)
            self.model.schedule.remove(prey)
            self.energy += 5
        # Reproduce if energy enough
        if self.energy > 20:
            self.model.add_predator()
            self.energy /= 2
        # Die if no energy
        if self.energy <= 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)

    def random_move(self):
        possible_steps = [-1, 0, 1]
        new_x = (self.pos[0] + random.choice(possible_steps)) % self.model.grid.width
        new_y = (self.pos[1] + random.choice(possible_steps)) % self.model.grid.height
        self.model.grid.move_agent(self, (new_x, new_y))