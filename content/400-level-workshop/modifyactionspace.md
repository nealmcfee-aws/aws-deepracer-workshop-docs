---
title: "Modify the action space"
chapter: true
weight: 10
description: "Explore the possible steering angle and speed combinations."
---




# Modify the action space

Configure your vehicle's action space to define by setting the range and granularity for steering angle and speed.

## Steering angle
The steering angle determines the range of steering angles in which the front wheels of your agent can turn. For the agent to be able to make bigger turns, set a higher steering angle. However, too high a steering angle can empower the agent to make unnecessarily excessive turns and can cause zig-zagging.

 
## Speed
The speed determines how fast your agent can drive. For the agent to be able to drive faster, set a higher speed. However, on a given track, you must balance the desire for speed against the concern for keeping the agent on the track while it maneuvers curves at a high speed.


![Image](/images/400workshop/actionspace.png)

### Create action space

Action space and steering angles can be changed by modifying files in the actions folder.

There are several example files included in the actions folder for you to use.

Use the file browser tab in Jupyter Lab to navigate to the following folder.


`DeepRacer_400_Workshop/src/artifacts/actions/`

In the actions folder you will see several example files.

The filename of each file specifies the sensors, the neural network, speed, and steering granularity of the action space.

#### The below example specifies the left camera, a deep neural network, one speed, and 5 steering levels.

`front_deep_single_speed_5steering.json`

#### The below example specifies both cameras, a shallow neural network, one speed, and 5 steering levels.

`stereo_shallow_single_speed_5steering.json`

#### The below example specifies both cameras, lidar, deep neural network, two speeds, and 5 steering levels.

`stereo_lidar_deep_two_speed_5steering.json`

### Create your own action space artifact file by following this json format.

![Image](/images/400workshop/actionspaceexample.png)


### Save your action space artifact file and move to the next activity.






**[Proceed to the next activity](../cyclopstostereo/)**
