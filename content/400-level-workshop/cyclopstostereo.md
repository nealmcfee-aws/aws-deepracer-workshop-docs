---
title: "Go from single camera, to stereo camera and LIDAR"
chapter: true
weight: 10
description: "Explore the possible sensor combinations in the simulation application."
---

# Modify the sensor combinations

Note that we have already added all the sensor combinations into the simulation application, and thus you only have to specify the preset that you want to use. Similarly, you can go add entirely new sensors into your simulation application, add them to the car model, and then use them during training. You will have to see what makes sense from a reward fucntion point of view.

Possible sensors

Single camera
Stereo camera
Single camera + LIDAR
Stereo Camera + LIDAR
When you specify a new sensor configuration this inpacts the state data that will feed into the neural network.

![Image](/static/images/400workshop/networkinput.png)

In specifying a single image, the process is straight forward, we take 160x120 pixel image and feed that as input.

However, when you add a second sensor you need to decide if you are concatenating the inputs before feeding them into the neural network, or if you are creating a second input (double headed so to speak).

Note that each input has its own embedder pipeline. For example, converting the color image to 8 bit grayscale. You could add more steps into this embedder process.

![Image](/images/400workshop/inputembedder.png)

### To add configure stereo camera and LIDAR



the observations to include the new sensors added in use function in src/markov/environments/deepracer_racetrack_env.py and use the below code segment in class DeepRacerRacetrackEnv(gym.Env) def __init__(self) to define the observation space with dictionary keys corresponding to the different type of sensors:
self.observation_space = spaces.Dict({
      'STEREO_CAMERAS': spaces.Box(low=0, high=255,
                              shape=(TRAINING_IMAGE_SIZE[1], TRAINING_IMAGE_SIZE[0], 2),
                              dtype=np.uint8),
      'LIDAR': spaces.Box(low=0.15, high=1.0, shape=(64,))
})
the input header names for the neural network in src/markov/presets/preset.py and the neural network architecture which are described in the next section.

**[Proceed to next step](../modifyneuralnetwork/)**
