---
title: "Update the neural network architecture"
chapter: true
weight: 20
description: "We have partnered with Intel and use Coach as reinforcement learning framework. Furthermore, we are using Tensorflow as our deep learning framework.

The neural network architecture typically includes an input embedder, middleware, and an output head, see descriptions here. In this section we are interested in changing the middleware."
---

# Update the neural network architecture

We have partnered with Intel and use Coach as reinforcement learning framework. Furthermore, we are using Tensorflow as our deep learning framework. 

The neural network architecture typically includes an input embedder, middleware, and an output head. In this section we are interested in changing the middleware.

### Network Design
Each agent has at least one neural network, used as the function approximator, for choosing the actions. The network is designed in a modular way to allow reusability in different agents. 

It is separated into three main parts:

![Image](/images/400workshop/coachnames.png)

#### CNN image input embedders 
This is the first stage of the network, meant to convert the input into a feature vector representation. It is possible to combine several instances of any of the supported embedders, in order to allow varied combinations of inputs.

The type of Input Embedder that AWS DeepRacer uses is Convolutional neural network.

#### FC middleware
The middleware gets the output of the input embedder, and processes it into a different representation domain, before sending it through the output head. The goal of the middleware is to enable processing the combined outputs of several input embedders, and pass them through some extra processing. This, for instance, might include an LSTM or just a plain simple FC layer.

#### Action output
The output head is used in order to predict the values required from the network. These might include action-values, state-values or a policy. As with the input embedders, it is possible to use several output heads in the same network. For example, the Actor Critic agent combines two heads - a policy head and a state-value head. In addition, the output heads defines the loss function according to the head type.

The default action space for our RL agent is discrete, therefore, the number of actions correspond to the number of output nodes of the policy network.


### Exercise  - Update Middleware

Note that we have already added middleware combinations into the simulation application, and thus you only have to specify the middleware level that you want to use. 

![Image](/images/400workshop/coachlayerpresets.png)



The more information you collect the larger the neural network is.

In the action space artifact file there is an entry for neural_network. 

![Image](/images/400workshop/actionspaceexample.png)

When updating the neural_network entry take into account the different combinations of sensors and network depth outlined below.

Neural Network values available for use in your action space artifact file:

`["DEEP_CONVOLUTIONAL_NETWORK"]`

`["DEEP_CONVOLUTIONAL_NETWORK_SHALLOW"]`

`["DEEP_CONVOLUTIONAL_NETWORK_DEEP"]`


#### Front facing camera

`"sensor": ["FRONT_FACING_CAMERA"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK"`

This will create a network in the format:

Conv2d(32,5,2)
Conv2d(32,3,1)
Conv2d(64,3,2)
Conv2d(64,3,1)
dense_layer(64)

`"sensor": ["FRONT_FACING_CAMERA"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK_SHALLOW"`

This will create a network in the format:

Conv2d(32,8,4)
Conv2d(64,4,2)
Conv2d(64,3,1)

`"sensor": ["FRONT_FACING_CAMERA"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK_DEEP"`

This will create a network in the format:

Conv2d(32,8,4)
Conv2d(32,4,2)
Conv2d(64,4,2)
Conv2d(64,3,1)
dense_layer(512)
dense_layer(512)

#### Front facing camera with Lidar

`"sensor": ["FRONT_FACING_CAMERA", "LIDAR"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK"`

This will create a network in the format:

Conv2d(32,5,2)
Conv2d(32,3,1)
Conv2d(64,3,2)
Conv2d(64,3,1)
dense_layer(64)
dense_layer(256)
dense_layer(256)

`"sensor": ["FRONT_FACING_CAMERA", "LIDAR"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK_SHALLOW"`

This will create a network in the format:

Conv2d(32,8,4)
Conv2d(64,4,2)
Conv2d(64,3,1)
dense_layer(256)
dense_layer(256)

`"sensor": ["FRONT_FACING_CAMERA", "LIDAR"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK_DEEP"`

This will create a network in the format:

Conv2d(32,8,4)
Conv2d(32,4,2)
Conv2d(64,4,2)
Conv2d(64,3,1)
dense_layer(512)
dense_layer(512)
dense_layer(256)
dense_layer(256)

#### Stereo Cameras

`"sensor": ["STEREO_CAMERAS"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK"`

This will create a network in the format:

Conv2d(32,3,1)
Conv2d(64,3,2)
Conv2d(64,3,1)
Conv2d(128,3,2)
Conv2d(128,3,1)

`"sensor": ["STEREO_CAMERAS"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK_SHALLOW"`

This will create a network in the format:

Conv2d(32,8,4)
Conv2d(64,4,2)
Conv2d(64,3,1)


`"sensor": ["STEREO_CAMERAS"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK_DEEP"`

This will create a network in the format:

Conv2d(32,3,1)
Conv2d(64,3,2)
Conv2d(64,3,1)
Conv2d(128,3,2)
Conv2d(128,3,1)

#### Stereo Cameras with Lidar

`"sensor": ["STEREO_CAMERAS", "LIDAR"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK"`

This will create a network in the format:

Conv2d(32,3,1)
Conv2d(64,3,2)
Conv2d(64,3,1)
Conv2d(128,3,2)
Conv2d(128,3,1)
dense_layer(256)
dense_layer(256)

`"sensor": ["STEREO_CAMERAS", "LIDAR"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK_SHALLOW"`

This will create a network in the format:

Conv2d(32,8,4)
Conv2d(64,4,2)
Conv2d(64,3,1)
dense_layer(256)
dense_layer(256)

`"sensor": ["STEREO_CAMERAS", "LIDAR"]`
`"neural_network": "DEEP_CONVOLUTIONAL_NETWORK_DEEP"`

This will create a network in the format:

Conv2d(32,3,1)
Conv2d(64,3,2)
Conv2d(64,3,1)
Conv2d(128,3,2)
Conv2d(128,3,1)
dense_layer(256)
dense_layer(256)


### Save your action space artifact file and move to the next activity.


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
