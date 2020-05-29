---
title: "Train the RL Model"
chapter: true
weight: 30
description: "Train it!"
---



# Train the RL model

The training process involves using AWS RoboMaker to emulate driving experiences in the environment, relaying the experiences at fixed intervals to Amazon SageMaker as input to train the deep neural network, and updating the network weights to an S3 location.

## Build and push Docker image

Part of this training process uses a customized Docker image.
The Dockerfile is located in the Amazon SageMaker Notebook Instance filesystem here:

```DeepRacer_400_Workshop/Dockerfile```

[More information on how Amazon SageMaker creates containers for custom training.](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html)

The type of container whether the training is done via CPU or if the training takes advantage of a GPU is set via the **instance_type** parameter.
If you selected a GPU instance type then be aware that training may go faster but the cost for a GPU container is higher than CPU.

Another action is code is copied from the ```DeepRacer_400_Workshop/src``` folder in the Amazon SageMaker Notebook Instance to the Docker container.

---

***NOTE*** 

If you modify files after the Build and Push Docker image step that you want to include in the Amazon SageMaker container you must re-run the step.


---

## Set algorithm metrics for CloudWatch

Next, we define the following algorithm metrics that we want to capture from CloudWatch logs to monitor the training progress. These are algorithm specific parameters and might change for different algorithm. We use Clipped PPO for this example.

## Train the RL model using the Python SDK Script mode

We use Clipped PPO (as provided by Coach) as our reinformcent learning algorithm to train our network. 
To edit the hyperparameters of the Clipped PPO RL agent edit the cell in the Jupyter Notebook.

The areas to edit are highlighted below.

![Image](/images/400workshop/hyperparams.png)


| ![Open SageMaker Notebook](/images/400workshop/aws-sagemaker-notebooks.png) | **Section: Train the RL Model** |
|---|---|

1. Return to the Jupyter Notebook ``400_deepracer_rl.ipynb``

2. Complete the **Section: Train the RL Model** in the notebook.


**[Proceed to the next activity](../startrollouts)**

