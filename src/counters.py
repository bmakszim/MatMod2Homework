from agents import RabbitAgent, GrassAgent, WeedAgent


def count_rabbits(model):
    result = 0
    for a in model.schedule.agents:
        if isinstance(a, RabbitAgent):
            result += 1
    return result


def count_grasses(model):
    result = 0
    for a in model.schedule.agents:
        if isinstance(a, GrassAgent):
            result += 1
    return result


def count_weeds(model):
    result = 0
    for a in model.schedule.agents:
        if isinstance(a, WeedAgent):
            result += 1
    return result
