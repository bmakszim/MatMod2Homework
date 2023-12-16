from agents import RabbitAgent, GrassAgent, WeedAgent
from counters import count_rabbits, count_grasses, count_weeds
from mesa.datacollection import DataCollector
from mesa.model import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation


class RabbitGrassModel(Model):
    def __init__(self, num_agent, height, width,
                 birth_threshold,
                 grass_grow_rate, grass_energy,
                 weed_grow_rate, weed_energy):
        super().__init__()
        self.num_agent = num_agent
        self.birth_threshold = birth_threshold
        self.grass_grow_rate = grass_grow_rate
        self.grass_energy = grass_energy
        self.weed_grow_rate = weed_grow_rate
        self.weed_energy = weed_energy
        self.grid = MultiGrid(height=height,
                              width=width,
                              torus=True)

        self.schedule = RandomActivation(model=self)
        for agent_id in range(0, num_agent):
            a = RabbitAgent(unique_id=self.next_id(),
                            model=self)
            self.schedule.add(agent=a)
            x = self.random.randrange(0, width)
            y = self.random.randrange(0, height)
            self.grid.place_agent(agent=a,
                                  pos=(x, y))

        self.grow_grass_and_weed()

        self.datacollector = DataCollector(
            model_reporters={
                "Rabbits": count_rabbits,
                "Grasses": count_grasses,
                "Weeds": count_weeds
            }
        )
        self.datacollector.collect(model=self)

    def grow_grass_and_weed(self):
        for agent, (x, y) in self.grid.coord_iter():
            if not isinstance(agent, RabbitAgent):
                if self.random.randrange(0, 1000) < self.grass_grow_rate:
                    grass = GrassAgent(unique_id=self.next_id(),
                                       model=self)
                    self.grid.place_agent(grass, (x, y))
                    self.schedule.add(grass)
                if self.random.randrange(0, 1000) < self.weed_grow_rate:
                    weed = WeedAgent(unique_id=self.next_id(),
                                     model=self)
                    self.grid.place_agent(weed, (x, y))
                    self.schedule.add(weed)

    def step(self):
        self.grow_grass_and_weed()
        self.schedule.step()
        self.datacollector.collect(model=self)
