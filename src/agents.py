from mesa.agent import Agent


class RabbitAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id=unique_id,
                         model=model)
        self.energy = self.model.random.randrange(0, 20)
        self.model = model

    def step(self):
        self.move()
        self.eat_grass_and_weed()
        self.reproduce()
        self.die()

    def move(self):
        pos_candidates = self.model.grid.get_neighborhood(pos=self.pos,
                                                          moore=False,
                                                          include_center=False)
        new_pos = self.model.random.choice(pos_candidates)
        self.model.grid.move_agent(agent=self,
                                   pos=new_pos)
        self.energy -= 1

    def eat_grass_and_weed(self):
        cell_list_content = self.model.grid.get_cell_list_contents([self.pos])
        if len(cell_list_content) > 1:
            for other_agent in cell_list_content:
                if isinstance(other_agent, GrassAgent):
                    self.energy += self.model.grass_energy
                    self.model.grid.remove_agent(other_agent)
                    self.model.schedule.remove(other_agent)
                if isinstance(other_agent, WeedAgent):
                    self.energy += self.model.weed_energy
                    self.model.grid.remove_agent(other_agent)
                    self.model.schedule.remove(other_agent)


    def reproduce(self):
        if self.energy > self.model.birth_threshold:
            self.energy = self.energy / 2
            rabbit = RabbitAgent(
                self.model.next_id(),
                self.model)
            self.model.grid.place_agent(rabbit, self.pos)
            self.model.schedule.add(rabbit)
            self.move()

    def die(self):
        if self.energy < 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)


class GrassAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id=unique_id,
                         model=model)


class WeedAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id=unique_id,
                         model=model)
