---
title: "Update the neural network architecture"
chapter: true
weight: 15
description: "We have partnered with Intel and use Coach as reinforcement learning framework. Furthermore, we are using Tensorflow as our deep learning framework.

The neural network architecture typically includes an input embedder, middleware, and an output head, see descriptions here. In this section we are interested in changing the middleware."
---

# Update Middleware

Coach layer names

![Image](/images/400workshop/coachnames.png)

Add another convolutional layer
Add mode convolutions
Test drop out
To change the neural network architecture, edit the preset file in src/markov/presets/. We provide two example preset files:

The default neural network architecture, src/markov/presets/default.py, has an input embedder with a 3 layer Convolutional Neural Network (CNN).
The attention neural network architecture, src/markov/presets/preset_attention_layer.py, provides an example on how to use custom layers.
Example:

agent_params.network_wrappers['main'].input_embedders_parameters['observation'].scheme = [Conv2d(32, 8, 4),Conv2d(64, 4, 2),Conv2dWithAttention(64, 3, 1, 256)]
In this example we have three convolutional layers on top of each other. The first one has 32 convolutional filters, a kernel size of 8x8, and a stride length of 4.

The source code explanation of Conv2d is here

Here are the default Coach layer presets

![Image](/static/images/400workshop/coachlayerpresets.png)

### Configure the RL algorithm hyperparameters

We use Clipped PPO (as provided by Coach) as our reinformcent learning algorithm to train our network. To edit the hyperparameters of the Clipped PPO RL agent, edit the preset file in src/markov/presets/. The configurable hyperparameters include learning_rate, neural network structure, batch_size, discount factor. These really are vital to getting good convergence, or none at all.

### Configure the reward function

To customize reward functions, modify reward_function in src/markov/rewards/. Note that the parameters exposed to the reward function are coded in the environment file. To create new variables for the reward function, edit the environment file, src/markov/environment/deepracer_racetrack_env.py.

### Configure the action space

Action space and steering angles can be changed by modifying src/markov/actions/.json file. The default action space for our RL agent is discrete, therefore, the number of actions correspond to the number of output nodes of the policy network.

### Copy custom files to S3 bucket so that Amazon SageMaker and AWS RoboMaker can pick them up

Very important, remember to copy the edited files from ./src/ back into S3 where SageMaker and RoboMaker will pick them up


**[Proceed to the next activity](../starttraining/)**
