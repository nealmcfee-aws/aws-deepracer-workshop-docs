---
title: "Customizing the simulation track and objects"
chapter: true
weight: 5
description: "You may be interested in changing tracks (adding a new track, or editing an existing one), adding objects to your track, or adding bot cars to train against."
---
## Exercise X
### Move the sim app to the working folder

<script src="https://gist.github.com/nealmcfee-aws/ec7dc385a61c6094fa0fd90b195e8c53.js"></script>

### Adding new tracks to your simulation application

![Image](/images/400workshop/Changetracks.png)

Racing tracks with various shapes and textures are included among the 3D assets build/simapp/bundle/opt/install/deepracer_simulation_environment/share/deepracer_simulation_environment.

To add a new track, you need to provide the following files:

3D assets
 meshes/mytrack/mytrack.dae and textures meshes/mytrack/textures. Note that AWS RoboMaker currently uses Gazebo to create the simulation environment, so everything needs to be compatible with Gazebo. For the already existing tracks, we provide Blender files for modifications as needed.

models/mytrack/mytrack.sdf and models/mytrack/model.

config, which point to the meshes and allows us to construct a completed model of the meshes where we specify which meshes should be visual and which should provide collision to our car
worlds/myworld.world, which takes our track model and wraps it in a world file, complete with sky and orientation.
routes/mytrack.npy, contains the waypoints of our track, outside border, center, and inside border, which our simulation will use to determine things such as is the agent on the track, and how much prrogress has been made etc.

### Adding new objects (excluding bot car) on the track

To add objects, you can use the following files:

models/racecar_box/model.sdf and models/racecar_box/model.config, contain model of a box object. Any other Gazebo compatiable object can be added by creating a folder with these files under models folder.
worlds/myworld_with_objects.world, which takes our prior track assets and our new object models. Any number of objects can be added by including the following lines in the world file:
````
  <include>
    <pose>0 0 0 0 0 0</pose>
    <static>true</static>
    <uri>model://models/racecar_box</uri>
    <name>box1</name>
  </include>
````
To replace any object during training, make a note of the object name, e.g., box1, and in your environment file, import rospy library and set_model_state function.

### Adding new bot cars

A bot car is simply another robocar without the neural network, hence, uses the same assets as the robocar in build/simapp/bundle/opt/install/deepracer_simulation_environment/share/deepracer_simulation_environment. The bot car uses the same functionality such as reset in build/simapp/bundle/opt/install/deepracer_simulation_environment/lib/deepracer_simulation_environment/car_node.py

To add, remove, or modify the speed and lane changing behavior bot cars, use function in src/markov/environments/deepracer_racetrack_env.py:

class BotCarController defines the functionality for the bot car behavior, including which segments on the track to spawn the bot car. Note that learning passing around corners is difficult due to partial observability, hence, initially, you can train a model to pass only on the straight segments to reduce the training time.
class DeepRacerRacetrackEnv(gym.Env) def __init__(self) is used to set the number of bot cars, their speed, and lane changning frequency.

### Adding and configuring new sensors

A new sensor such as camera or LIDAR with existing ROS plug-in can be added in directly in the Gazebo car asset files located in build/simapp/bundle/opt/install/deepracer_simulation_environment/share/deepracer_simulation_environment/urdf/

To add another camera:

racecar.gazebo in the original time-trial already includes a camera, to add another camerara you can replicate that code snippet with a new name. Alternatively, you can add a less to the existing camera.

racecar.xacro contains the parameters to set the location of the cameras, see _leftcam and _rightcam.

macro.xacro contains the joints that the sensors are attached to including cameras and lenses for the cameras. The angle of the camera lenses are adjusted in this file.

To add a LIDAR:

racecar.gazebo uses a LIDAR plugin compatible with the LIDAR on the device, similar to the camera module. There are two parameters that can be customized for the LIDAR, scan and range. These parameters determine the angle bracket and range to detect light reflections. The default settings below are for +/- 1.0472 radians (60 degrees) for the scanning angle and is between 0.15 and 0.5 meters for the observability range.
````
<scan>
<horizontal>
  <samples>64</samples>
  <resolution>1</resolution>
  <min_angle>-1.0472</min_angle>
  <max_angle>1.0472</max_angle>
</horizontal>
</scan>
<range>
<min>0.15</min>
<max>0.5</max>
<resolution>0.01</resolution>
</range>
````
racecar.xacro contains the parameters to set the location of the LIDAR, similar to the camera.

macro.xacro contains the joints that the sensors are attached to and its angle.

### Preparing the AWS RoboMaker Bundle

After making changes to the simulation application assets, re-bundle it using the Python file sim_app_bundler.py. We will upload the tar.gz file to the AWS RoboMaker arn later in the notebook.

**[Proceed to the next activity](../cyclopstostereo/)**
