---
title: "Create a reward function"
chapter: true
weight: 20
description: "The reward function describes immediate feedback (as a score for reward or penalty) when the vehicle takes an action to move from a given position on the track to a new position. Its purpose is to encourage the vehicle to make moves along the track to reach its destination quickly. The model training process will attempt to find a policy which maximizes the average total reward the vehicle experiences."
---

# Create a reward function

In general, you design your reward function to act like an incentive plan. You can customize your reward function with relevant input parameters passed into the reward function. 

### Reward function files

`DeepRacer_400_Workshop/src/artifacts/rewards/`

![Image](/images/400workshop/rewardfunctionfiles.png)

There are several example reward functions for you to modify.
The file name indicates the reward function code.



### Reward function input parameters

[reward function input parameter list](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html)

### Create the reward function


If you wish to create your own reward function there is a pattern to the function that you must use.

```python
def reward_function(params) :
    
    reward = ...

    return float(reward)
```
The reward function input parameters (params) are passed in as a dictionary object, specifying a given state (params["x"], params["y"], params["all_wheels_on_track"], params["distance_from_center"], etc.) the agent is in and a given action (params["speed"] and params["steering"]) the agent takes. You manipulate one or more of the input parameters to create a customized reward function most appropriate for your solution.

#### A list of parameters and their definition is located [here](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html?icmpid=docs_deepracer_console)

---

**NOTE**

Since you are using a Jupyter Notebook in an Amazon SageMaker Notebook Instance you can import modules to create robust reward functions.

---

### Save your reward function artifact file and move to the next activity.


### move to jupyter notebook and do the save into s3


**[Proceed to the next activity](../starttraining/)**
