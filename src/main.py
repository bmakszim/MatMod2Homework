from model import RabbitGrassModel
import matplotlib.pyplot as plt


def run_model():
    num_agent = 20
    width = 20
    height = 20
    birth_threshold = 15
    grass_grow_rate = 15
    weed_grow_rate = 0
    grass_energy = 10
    weed_energy = 0

    model = RabbitGrassModel(
        num_agent=num_agent,
        width=width,
        height=height,
        birth_threshold=birth_threshold,
        grass_grow_rate=grass_grow_rate,
        grass_energy=grass_energy,
        weed_grow_rate=weed_grow_rate,
        weed_energy=weed_energy
    )

    timespan = 1000
    for t in range(0, timespan):
        model.step()

    states = model.datacollector.get_model_vars_dataframe()
    states.plot()
    plt.show()


run_model()
