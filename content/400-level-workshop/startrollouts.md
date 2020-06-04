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
**robomaker_s3_key** sets the location that the AWS RoboMaker Simulation Application will look for the bundled SimApp. `robomaker/simulation_ws.tar.gz`

**robomaker_source** sets the S3 bucket location to AWS RoboMaker to look for the SimApp bundle.
Additionally the architecture is set for "X86_64" which should not be changed for this workshop.

**simulation_software_suite** sets Gazebo as the simulation engine, and version 7 of Gazebo.

**robot_software_suite** sets ROS and ROS version Kinetic which is the first version of ROS.

**rendering_engine** sets the graphical rendering engine, OGRE stands for Object-Oriented Graphics Rendering Engine

[Additional AWS RoboMaker Simulation FAQs](https://aws.amazon.com/robomaker/faqs/#Simulation)


### Bundle the AWS RoboMaker Simulation Application

The Simulation Application was downloaded and you expanded the SimApp into the `DeepRacer_400_Workshop/build` folder.
If you make changes to any files in the `DeepRacer_400_Workshop/src/markov` folder then you will need to copy those changes to the SimApp so the simulation works with your changes then bundle the SimApp.

If you did not make any changes to files in the `DeepRacer_400_Workshop/src/markov` folder then only bundle the SimApp, copying changes is not required.

### Upload the AWS RoboMaker Simulation Application to an Amazon S3 bucket

After bundling the SimApp locally in your notebook filesystem you need to upload the SimApp to S3.
The location for upload is set by the **robomaker_s3_key** parameter.


### Create ARN for the AWS RoboMaker Simulation Application

Using boto3.client("robomaker"), create the Amazon Resource Name which will return an ARN for use in creating AWS RoboMaker Simulation Jobs.
This ARN is used as a reference to which Simulation Application the rollouts will use. 

### Set the AWS RoboMaker Simulation Job parameters and start the training Simulation Jobs

This task contains multiple steps to set Simulation parameters and start the training Simulation jobs.

#### Set SimApp Parameters ####

Since the Simulation Application contains multiple tracks and multiple race types there is a need to tell the SimApp which to run in the Simulation Job. 

Like the Action Space and Reward Function artifact file templates there are example SimApp configuration files available for you to review.

The files are located in the `DeepRacer_400_Workshop/src/artifacts/yaml` folder.
There are four files:

**Evaluation**
`DeepRacer_400_Workshop/src/artifacts/yaml/evaluation_yaml_template.yaml`

**Head to Head**
`DeepRacer_400_Workshop/src/artifacts/yaml/head2head_yaml_template.yaml`

**Tournament**
`DeepRacer_400_Workshop/src/artifacts/yaml/tournament_yaml_template.yaml`

**Training**
`DeepRacer_400_Workshop/src/artifacts/yaml/training_yaml_template.yaml`

For this section we will focus on **Training**

In the `training_yaml_template.yaml` there are parameters that will set the track and the type of race.

| world_name | image | value
| Bowtie | ![Bowtie](/images/400workshop/Bowtie_track.png) | Bowtie_track
| Canada | ![Bowtie](/images/400workshop/Canada_Training.png) | Canada_Training
| China | ![Bowtie](/images/400workshop/China_track.png) | China_track

#### Set Simulation Job environment variables ####
#### Create the Simulation Jobs ####





### Creating temporary folder top plot metrics

### Plot metrics for training job


| ![Open SageMaker Notebook](/images/400workshop/aws-sagemaker-notebooks.png) | **Section: Start the AWS Robomaker Simulation** |
|---|---|

1. Return to the Jupyter Notebook ``400_deepracer_rl.ipynb``

2. Complete the **Section: Start the AWS Robomaker Simulation** in the notebook.



**[Proceed to the next activity](../evaluation/)**
