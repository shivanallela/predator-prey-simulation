from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from model import PredatorPreyModel
from agent import Prey, Predator

# Portrayal function
def agent_portrayal(agent):
    if isinstance(agent, Prey):
        return {"Shape": "circle", "Filled": "true", "r": 0.5, "Color": "green", "Layer": 0}
    elif isinstance(agent, Predator):
        return {"Shape": "circle", "Filled": "true", "r": 0.5, "Color": "red", "Layer": 1}
    return {}

# Grid visualization
grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)

# Chart visualization
chart = ChartModule(
    [{"Label": "Prey", "Color": "green"},
     {"Label": "Predators", "Color": "red"}],
    data_collector_name='datacollector'
)

server = ModularServer(PredatorPreyModel,
                       [grid, chart],
                       "Predator-Prey Simulation",
                       {"width": 20, "height": 20, "initial_prey": 20, "initial_predators": 5})

server.port = 8521  # Can change if port is busy
server.launch(port=8522)  # pick any number above 1024python "c:\Users\shiva\OneDrive\Documents\projectmesa\predator-prey-simulation\visualization.py"
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

# Example sliders
model_params = {
    "width": 20,
    "height": 20,
    "initial_prey": UserSettableParameter("slider", "Initial Prey", 20, 10, 50, 1),
    "initial_predators": UserSettableParameter("slider", "Initial Predators", 5, 1, 20, 1),
    "prey_reproduce": UserSettableParameter("slider", "Prey Reproduce Probability", 0.2, 0.01, 1.0, 0.01),
    "predator_gain": UserSettableParameter("slider", "Predator Energy Gain", 4, 1, 10, 1),
}