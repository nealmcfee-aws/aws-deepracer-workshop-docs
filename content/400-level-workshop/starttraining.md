---
title: "Train the RL Model"
chapter: true
weight: 30
description: "Train it!"
---

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



---

**NOTE**

The following hyperparameters are for file references and may cause your code to not work.
Please refrain from modifications unless in advanced scenarios.

![Image](/images/400workshop/hyperparamsdonotedit.png)
 
---

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


# Train the RL model

### Exercise XX - Notebook Imports

### Exercise XX - Initialize basic parameters

### Exercise XX - Setup S3 bucket

### Exercise XX - Build and push Docker image

### Exercise XX - Train the RL model using the Python SDK Script mode

Next, we define the following algorithm metrics that we want to capture from cloudwatch logs to monitor the training progress. These are algorithm specific parameters and might change for different algorithm. We use Clipped PPO for this example.

### Exercise XX - Create the Kinesis video stream (optional)

Blurb about KVS

### Exercise XX - Start the AWS RoboMaker job

Blurb about starting the AWS RoboMaker job

### Exercise XX - Create Simulation Application

Blurb about creating the simapp in AWS RoboMaker

### Exercise XX - Upload your customized simulation application to your s3 bucket

The AWS DeepRacer bundle to be used by the AWS RoboMaker service is under 
```
build/output.tar.gz
```
Next, we need to upload the bundle to our S3 bucket and create an AWS RoboMaker Simulation Application.



### Exercise XX - Create arn for the AWS RoboMaker simulation application

blurb about the ARN



**[Proceed to the next activity](../startrollouts)**
