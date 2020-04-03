---
title: "Update the neural network architecture"
chapter: true
weight: 15
description: "We have partnered with Intel and use Coach as reinforcement learning framework. Furthermore, we are using Tensorflow as our deep learning framework.

The neural network architecture typically includes an input embedder, middleware, and an output head, see descriptions here. In this section we are interested in changing the middleware."
---

# Update the neural network architecture

### Exercise 8 - Update Middleware

Coach layer names

![Image](/images/400workshop/coachnames.png)

Add another convolutional layer
Add mode convolutions
Test drop out
To change the neural network architecture, edit the preset file in 
```
src/markov/presets/
```
We provide two example preset files:

The default neural network architecture
 
`src/markov/presets/default.py`

, has an input embedder with a 3 layer Convolutional Neural Network (CNN).

The attention neural network architecture, 

`src/markov/presets/preset_attention_layer.py`

provides an example on how to use custom layers.

Example:
```python
agent_params.network_wrappers['main'].input_embedders_parameters['observation'].scheme = [Conv2d(32, 8, 4),Conv2d(64, 4, 2),Conv2dWithAttention(64, 3, 1, 256)]
```
In this example we have three convolutional layers on top of each other. The first one has 32 convolutional filters, a kernel size of 8x8, and a stride length of 4.

The source code explanation of Conv2d is here

Here are the default Coach layer presets

![Image](/images/400workshop/coachlayerpresets.png)

### Exercise 9 - Configure the RL algorithm hyperparameters

We use Clipped PPO (as provided by Coach) as our reinformcent learning algorithm to train our network. 
To edit the hyperparameters of the Clipped PPO RL agent, edit the preset file in 
```
src/markov/presets/
```
 The configurable hyperparameters include learning_rate, neural network structure, batch_size, discount factor. These really are vital to getting good convergence, or none at all.

### Exercise 10 - Configure the reward function

To customize reward functions, modify reward_function in 
```
src/markov/rewards/ 
```
Note that the parameters exposed to the reward function are coded in the environment file. 
To create new variables for the reward function, edit the environment file

`src/markov/environment/deepracer_racetrack_env.py`

### Exercise 11 - Configure the action space

Action space and steering angles can be changed by modifying 

`src/markov/actions/.json`

The default action space for our RL agent is discrete, therefore, the number of actions correspond to the number of output nodes of the policy network.

## Other interesting manipulations to take note of

### Changing the training algorithm
To change the RL agent algorithm, refer to the DQN example for AWS DeepRacer. There are multiple files that need to be editted including the preset file in 
```
src/markov/presets/
```
### Configure the environment file with custom simulation variables
We use an environment file, 

`src/markov/environment/deepracer_racetrack_env.py` 

which contains "step" and "reset" functions and ability to exchange messages with the Gazebo based AWS RoboMaker simulator. This environment file is shared between Amazon Sagemaker and AWS RoboMaker jobs. 
The environment variable - NODE_TYPE defines which node the code is running on. So, the expressions that have rospy dependencies are executed on RoboMaker only.

How to add noise to observations?
You can add noise to robocar camera observations by using OpenCV or other image editing packages available in Python. Note that these libraries need to be located in or copied to 
```
build/simapp/bundle/usr/local/lib/python3.5/dist-packages 
```
for AWS RoboMaker to import them.

As an example, we provide a modified environment 

`src/markov/environment/deepracer_racetrack_env_cv2.py`

, to use cv2 and add Gaussian noise to robocar observations in 
```python 
def set_next_state()
```
: (see Lines ~241-254)

How to add noise to actions, i.e., steering and speed, for robustness?
Adding noise to your actions also increases the robustness of your model to steady-state or tracking errors of the robocar controllers for steering and speed in the real world. Since we use discrete action, we need to add noise to their associated mappings in 
```python
class DeepRacerRacetrackCustomActionSpaceEnv(DeepRacerRacetrackEnv)
```
: (see Lines ~575-579)

### Exercise 12 - Copy custom files to S3 bucket so that Amazon SageMaker and AWS RoboMaker can pick them up

Very important, remember to copy the edited files from 
```
./src/ 
```
back into S3 where SageMaker and RoboMaker will pick them up..

**[Proceed to the next activity](../starttraining/)**
