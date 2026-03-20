from model import PredatorPreyModel

# Initialize the model
model = PredatorPreyModel(width=10, height=10, initial_prey=20, initial_predators=5)

# Run for 20 steps
for step in range(20):
    model.step()
    
    # Count agents
    prey_count = sum(1 for agent in model.schedule.agents if type(agent).__name__ == "Prey")
    predator_count = sum(1 for agent in model.schedule.agents if type(agent).__name__ == "Predator")
    
    print(f"Step {step}: {prey_count} prey, {predator_count} predators")