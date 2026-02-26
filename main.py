import numpy as np
import matplotlib.pyplot as plt
import argparse

# True state of the world: 1 = Good, 0 = Bad
TRUE_STATE = 1

# Prior belief P(Good)
prior = 0.5

# Signal accuracy: P(signal = TRUE_STATE)
parser = argparse.ArgumentParser(description="Bayesian belief update simulator")
parser.add_argument("--accuracy", type=float, default=0.75, help="Signal accuracy between 0 and 1")
args = parser.parse_args()

signal_accuracy = args.accuracy

# Number of rounds
rounds = 30

beliefs = [prior]

def bayes_update(prior, signal, accuracy):
    """
    prior: P(Good)
    signal: 1 or 0
    accuracy: P(signal is correct)
    """
    if signal == 1:
        likelihood_good = accuracy
        likelihood_bad = 1 - accuracy
    else:
        likelihood_good = 1 - accuracy
        likelihood_bad = accuracy

    numerator = likelihood_good * prior
    denominator = numerator + likelihood_bad * (1 - prior)

    return numerator / denominator

for t in range(rounds):
    # Sender sends a noisy signal about the true state
    if np.random.rand() < signal_accuracy:
        signal = TRUE_STATE
    else:
        signal = 1 - TRUE_STATE

    prior = bayes_update(prior, signal, signal_accuracy)
    beliefs.append(prior)

# Plot belief over time
accuracies = [0.6, 0.75, 0.9]

plt.figure()

for acc in accuracies:
    prior = 0.5
    beliefs = [prior]
    for _ in range(rounds):
        signal = TRUE_STATE if np.random.rand() < acc else 1 - TRUE_STATE
        prior = bayes_update(prior, signal, acc)
        beliefs.append(prior)
    plt.plot(beliefs, label=f"accuracy={acc}")

plt.xlabel("Time Step")
plt.ylabel("Belief that State = Good")
plt.title("Belief Update Under Different Signal Noise Levels")
plt.legend()
plt.show()