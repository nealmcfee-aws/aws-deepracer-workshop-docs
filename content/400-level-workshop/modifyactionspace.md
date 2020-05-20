---
title: "Modify the action space"
chapter: true
weight: 10
description: "Explore the possible angle and speed combinations."
---

# Modify the action space

Action space and steering angles can be changed by modifying files in the actions folder.

There are several example files included in the actions folder for you to use.

`DeepRacer_400_Workshop/src/artifacts/actions/`

There are several example files that match a pattern.

The filename specifies the sensors, the neural network, speed, and steering granularity of the action space.

This example specifies the left camera, a deep neural network, one speed, and 5 steering levels.

`front_deep_single_speed_5steering.json`

This example specifies both cameras, a shallow neural network, one speed, and 5 steering levels.

`stereo_shallow_single_speed_5steering.json`

This example specifies both cameras, lidar, deep neural network, two speeds, and 5 steering levels.

`stereo_lidar_deep_two_speed_5steering.json`

You are able to create your own action space artifact file by following this json format.

![Image](/images/400workshop/actionspaceexample.png)


Step -- Create action space






**[Proceed to the next activity](../cyclopstostereo/)**
