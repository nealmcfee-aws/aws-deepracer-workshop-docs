---
title: "Create multiple Rollouts"
chapter: true
weight: 35
description: "We create AWS RoboMaker simulation jobs that simulates the environment and shares this data with SageMaker for training. Each roll-out uses a central model to independently collect experience in the form of episodes, where each episode consist of (state, action, next state, reward) tuples"
---

# Create multiple Rollouts 

We create AWS RoboMaker simulation jobs that simulates the environment and shares this data with SageMaker for training. Each roll-out uses a central model to independently collect experience in the form of episodes, where each episode consist of (state, action, next state, reward) tuples

![Image](/images/400workshop/fourrollouts.png)

We use horizontal scaling where the neural network model files are synchronized between the Amazon Sagemaker training job and AWS RoboMaker simulation workers.

### Create the Kinesis video stream (optional)

Like the AWS DeepRacer Console Kinesis video streams is used to display the video feed and additional overlay information. If you wish to view the video feed then you can access the media playback in AWS Console.
Performing this step is optional, but it is a great way to view all of your rollouts and their progress.
If you set multiple rollouts with a value over 1 for the **num_simulation_workers** you will see Kinesis Video Streams cycle through each rollout in the media playback.

[Kinesis Video Streams](https://console.aws.amazon.com/kinesisvideo/home?region=us-east-1#/streams)


![Image](/images/400workshop/kvstraining.png)

You should see a near real-time media playback of your agents traversing the track in training and evaluating phases.

### Create the AWS RoboMaker Simulation Application

AWS DeepRacer uses AWS RoboMaker as the simulation engine to train your model using a world created in Gazebo.
To create this simulation we need to configure AWS RoboMaker by first creating an AWS RoboMaker Simulation Application.
More information on AWS RoboMaker and [Managing Simulation Applications](https://docs.aws.amazon.com/robomaker/latest/dg/managing-simulation-applications.html)

```
robomaker_s3_key = 'robomaker/simulation_ws.tar.gz'
robomaker_source = {'s3Bucket': s3_bucket,
                    's3Key': robomaker_s3_key,
                    'architecture': "X86_64"}
simulation_software_suite={'name': 'Gazebo',
                           'version': '7'}
robot_software_suite={'name': 'ROS',
                      'version': 'Kinetic'}
rendering_engine={'name': 'OGRE',
                  'version': '1.x'}

```
The parameters above outline that we are creating our own AWS RoboMaker Simulation Application using a SimApp bundle located at `robomaker/simulation_ws.tar.gz`

**robomaker_source** sets the S3 bucket location to AWS RoboMaker to look for the SimApp bundle.
Additionally the architecture is set for "X86_64" which should not be changed for this workshop.

**simulation_software_suite** sets Gazebo as the simulation engine, and version 7 of Gazebo.

**robot_software_suite** sets ROS and ROS version Kinetic which is the first version of ROS.

**rendering_engine** sets the graphical rendering engine, OGRE stands for Object-Oriented Graphics Rendering Engine

[Additional AWS RoboMaker Simulation FAQs](https://aws.amazon.com/robomaker/faqs/#Simulation)


### Bundle the AWS RoboMaker Simulation Application

The Simulation Application was downloaded and you expanded the SimApp into the `DeepRacer_400_Workshop/build` folder.


### Upload the AWS RoboMaker Simulation Application to an Amazon S3 bucket




### Create ARN for the AWS RoboMaker Simulation Application


### Set the AWS RoboMaker Simulation Job parameters and start the training Simulation Jobs


### Creating temporary folder top plot metrics

### Plot metrics for training job


| ![Open SageMaker Notebook](/images/400workshop/aws-sagemaker-notebooks.png) | **Section: Start the AWS Robomaker Simulation** |
|---|---|

1. Return to the Jupyter Notebook ``400_deepracer_rl.ipynb``

2. Complete the **Section: Start the AWS Robomaker Simulation** in the notebook.



**[Proceed to the next activity](../evaluation/)**
