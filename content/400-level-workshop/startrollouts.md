---
title: "Create multiple Rollouts"
chapter: true
weight: 35
description: "We create AWS RoboMaker simulation jobs that simulates the environment and shares this data with SageMaker for training. Each roll-out uses a central model to independently collect experience in the form of episodes, where each episode consist of (state, action, next state, reward) tuples"
---

# Create multiple Rollouts 

We create AWS RoboMaker simulation jobs that simulates the environment and shares this data with SageMaker for training. Each roll-out uses a central model to independently collect experience in the form of episodes, where each episode consist of (state, action, next state, reward) tuples

![Image](/images/400workshop/fourrollouts.png)

We use horizontal scaling where the neural network model files are synchronized between the Amazon Sagemaker training job and AWS RoboMaker simulation workers. Model sync behavior is coded in 

`src/markov/training_worker.py`

## Create the Kinesis video stream (optional)

Like the AWS DeepRacer Console Kinesis video streams is used to display the video feed and additional overlay information. If you wish to view the video feed then you can run the 


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


### Exercise ## - Set preset parameter

```python
if graph_manager.agent_params.algorithm.distributed_coach_synchronization_type == 
            DistributedCoachSynchronizationType.SYNC:
    graph_manager.save_checkpoint()
else:
    graph_manager.occasionally_save_checkpoint()
```
To enable sync models to the s3 bucket for multiple rollouts, set the **agent_params.algorithm.distributed_coach_synchronization_type** parameter in

`src/markov/presets/preset.py`
```python
agent_params.algorithm.distributed_coach_synchronization_type = DistributedCoachSynchronizationType.SYNC
```

### Exercise XX - Increase number of workers to 2 or more

Specify the number of roll-out workers using the **num_simulation_workers** parameter.

### Exercise XX - Create links to AWS RoboMaker jobs for visualization

You can visit the RoboMaker console to visualize the simulations or run the following cell to generate the hyperlinks.

### Exercise XX - Run evaluation in parallel

Blurb about running in parallel



**[Proceed to the next activity](../evaluation/)**
