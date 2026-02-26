# Bayesian Update Simulator
This project simulates how beliefs change over time using Bayes' Rule when a receiver gets noisy signals from a sender.

## What this shows
- Bayesian belief updates
- Effect of noisy information on belief
- Convergence of belief with repeated signals

## How it works
There is a hidden true state (Good or Bad).  
The sender sends a noisy signal about the true state.  
The receiver updates belief using Bayes’ Rule after every signal.

## How to run
1. Install dependencies:
   pip install -r requirements.txt

2. Run:
   python main.py

You will see a plot showing how belief changes over time.

3. Run with custom signal accuracy:
   python main.py --accuracy 0.9

### Experiments
I ran the simulator with different signal accuracies (0.6, 0.75, 0.9).
Observation: higher signal accuracy leads to faster convergence of beliefs.
This demonstrates how information quality affects persuasion outcomes.

## Why this project
This is a small toy model inspired by Bayesian persuasion and decision-making under uncertainty.