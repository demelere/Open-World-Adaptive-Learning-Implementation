from envs.articulated_object_env import ArticulatedObjectEnv
from learning.imitation_learning import ImitationLearning
from learning.reinforcement_learning import ReinforcementLearning
from utils.data_loader import load_expert_demonstrations

def main():
    # Initialize the environment
    env = ArticulatedObjectEnv()

    # Load expert demonstrations
    expert_demos = load_expert_demonstrations('path/to/demos')

    # Initialize the imitation learning module
    imitation_learner = ImitationLearning(env, expert_demos)
    
    # Train the model with imitation learning
    imitation_learner.train()

    # After imitation learning, initialize the reinforcement learning module
    rl_learner = ReinforcementLearning(env)

    # Train the model with online reinforcement learning
    rl_learner.train()

    # Optionally, evaluate the model's performance

if __name__ == "__main__":
    main()
