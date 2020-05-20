---
title: "Modify the sensor combinations"
chapter: true
weight: 15
description: "Explore the possible sensor combinations in the simulation application."
---

# Modify the sensor combinations

Note that we have already added all the sensor combinations into the simulation application, and thus you only have to specify the sensor that you want to use. 


### Possible sensors

Single camera

Single camera + LIDAR

Stereo camera

Stereo camera + LIDAR

When you specify a new sensor configuration this impacts the state data that will feed into the neural network.

![Image](/images/400workshop/networkinput.png)


![Image](/images/400workshop/inputembedder.png)

### Exercise 7 - Configure the sensor in the action space artifact file

In the action space artifact file there is an entry for sensor.

For the sensor you have the following choices:

```"sensor": ["FRONT_FACING_CAMERA"]```

```"sensor": ["FRONT_FACING_CAMERA", "LIDAR"]```

```"sensor": ["STEREO_CAMERAS"]```

```"sensor": ["STEREO_CAMERAS", "LIDAR"]```



![Image](/images/400workshop/actionspaceexample.png)


 ### Save your action space artifact file and move to the next activity to modify the neural network.

**[Proceed to the next activity](../modifyneuralnetwork/)**
