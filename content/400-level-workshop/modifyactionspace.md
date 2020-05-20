---
title: "Modify the action space"
chapter: true
weight: 10
description: "Explore the possible steering angle and speed combinations."
---




# Modify the action space

Configure your vehicle's action space to define by setting the range and granularity for steering angle and speed.

## Steering angle
The steering angle granularity determines the number of directions your agent can steer. Increasing this will empower the agent to exercise finer control, but the larger action space will also increase the time it takes to train your model.
 
## Speed
The speed granularity determines the number of speeds in which your agent can drive. Increasing this will empower the agent to exercise finer control, but the larger action space will also increase the time it takes to train your model.

![Image](/images/400workshop/actionspace.png)

### Create action space

Action space and steering angles can be changed by modifying files in the actions folder.

There are several example files included in the actions folder for you to use.


`DeepRacer_400_Workshop/src/artifacts/actions/`


The filename of each file specifies the sensors, the neural network, speed, and steering granularity of the action space.

#### The below example specifies the left camera, a deep neural network, one speed, and 5 steering levels.

`front_deep_single_speed_5steering.json`

#### The below example specifies both cameras, a shallow neural network, one speed, and 5 steering levels.

`stereo_shallow_single_speed_5steering.json`

#### The below example specifies both cameras, lidar, deep neural network, two speeds, and 5 steering levels.

`stereo_lidar_deep_two_speed_5steering.json`

### Create your own action space artifact file by following this json format.

![Image](/images/400workshop/actionspaceexample.png)


### Save your action space artifact file and move to the next activity to modify the sensors.






**[Proceed to the next activity](../cyclopstostereo/)**
