---
title: "Create multiple Rollouts"
chapter: true
weight: 25
description: "We create AWS RoboMaker simulation jobs that simulates the environment and shares this data with SageMaker for training. Each roll-out uses a central model to independently collect experience in the form of episodes, where each episode consist of (state, action, next state, reward) tuples"
---

# Using multiple rollouts during training 

![Image](/images/400workshop/fourrollouts.png)

### Set preset parameter

````
if graph_manager.agent_params.algorithm.distributed_coach_synchronization_type == 
            DistributedCoachSynchronizationType.SYNC:
    graph_manager.save_checkpoint()
else:
    graph_manager.occasionally_save_checkpoint()
To enable sync models to the s3 bucket for multiple rollouts, set the parameter in src/markov/presets/preset.py

agent_params.algorithm.distributed_coach_synchronization_type = DistributedCoachSynchronizationType.SYNC

````

### Increase number of workers to 2

Specify the number of roll-out workers using the num_simulation_workers parameter.

### Create links to AWS RoboMaker jobs for visualization

You can visit the RoboMaker console to visualize the simulations or run the following cell to generate the hyperlinks.

### Run evaluation in parallel

Blurb about running in parallel



**[Proceed to the next activity](../evaluation/)**
