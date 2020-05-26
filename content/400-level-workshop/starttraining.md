---
title: "Train the RL Model"
chapter: true
weight: 30
description: "Train it!"
---

### Exercise 9 - Configure the RL algorithm hyperparameters  --- MOVE THIS TO TRAIN RL MODEL

We use Clipped PPO (as provided by Coach) as our reinformcent learning algorithm to train our network. 
To edit the hyperparameters of the Clipped PPO RL agent edit the cell in the Jupyter Notebook.

The hyperparameters that you can modify are 

![Image](/images/400workshop/hyperparams.png)


---

**NOTE**

The following hyperparameters are for file references and may cause your code to not work.
Please refrain from modifications unless in advanced scenarios.
 
---
![Image](/images/400workshop/hyperparamsdonotedit.png)


# Train the RL model



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

