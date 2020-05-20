---
title: "Create multiple Rollouts"
chapter: true
weight: 30
description: "We create AWS RoboMaker simulation jobs that simulates the environment and shares this data with SageMaker for training. Each roll-out uses a central model to independently collect experience in the form of episodes, where each episode consist of (state, action, next state, reward) tuples"
---

# Create multiple Rollouts 

We create AWS RoboMaker simulation jobs that simulates the environment and shares this data with SageMaker for training. Each roll-out uses a central model to independently collect experience in the form of episodes, where each episode consist of (state, action, next state, reward) tuples

![Image](/images/400workshop/fourrollouts.png)

We use horizontal scaling where the neural network model files are synchronized between the Amazon Sagemaker training job and AWS RoboMaker simulation workers. Model sync behavior is coded in 

`src/markov/training_worker.py`

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
