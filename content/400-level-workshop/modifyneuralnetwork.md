---
title: "Update the neural network architecture"
chapter: true
weight: 15
description: "We have partnered with Intel and use Coach as reinforcement learning framework. Furthermore, we are using Tensorflow as our deep learning framework.

The neural network architecture typically includes an input embedder, middleware, and an output head, see descriptions here. In this section we are interested in changing the middleware."
---

# Update the neural network architecture

### Exercise  - Update Middleware

Coach layer names

![Image](/images/400workshop/coachnames.png)



Here are the default Coach layer presets

![Image](/images/400workshop/coachlayerpresets.png)

### Exercise  - Configure the action space, Sensors, and Neural Network

Action space and steering angles can be changed by modifying files in the actions folder.

There are several example files included in the actions folder for you to use.

`DeepRacer_400_Workshop/src/artifacts/actions/`

There are several example files that match a pattern.

The filename specifies the sensors, the neural network, speed, and steering granularity of the action space.

This example specifies the left camera, a deep neural network, one speed, and 5 steering levels.

`front_deep_single_speed_5steering.json`

This example specifies both cameras, a shallow neural network, one speed, and 5 steering levels.

`stereo_shallow_single_speed_5steering.json`

This example specifies both cameras, lidar, deep neural network, two speeds, and 5 steering levels.

`stereo_lidar_deep_two_speed_5steering.json`

You are able to create your own action space artifact file by following this json format.

![Image](/images/400workshop/actionspaceexample.png)


Step -- Create action space


Step -- Sensors

Sensor values available:

["FRONT_FACING_CAMERA"]
["STEREO_CAMERAS"]
["FRONT_FACING_CAMERA, LIDAR"]
["STEREO_CAMERAS", "LIDAR"]


Step -- Neural Network

Neural Network values available:

["DEEP_CONVOLUTIONAL_NETWORK_SHALLOW"]
["DEEP_CONVOLUTIONAL_NETWORK"]

The default action space for our RL agent is discrete, therefore, the number of actions correspond to the number of output nodes of the policy network.


### Exercise 9 - Configure the RL algorithm hyperparameters  --- MOVE THIS TO TRAIN RL MODEL

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
