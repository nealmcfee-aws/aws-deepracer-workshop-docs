from rl_coach.architectures.layers import Conv2d, Dense, BatchnormActivationDropout
from rl_coach.architectures.middleware_parameters import FCMiddlewareParameters
from rl_coach.architectures.embedder_parameters import InputEmbedderParameters
from rl_coach.agents.clipped_ppo_agent import ClippedPPOAgentParameters
from rl_coach.base_parameters import VisualizationParameters, PresetValidationParameters
from rl_coach.core_types import TrainingSteps, EnvironmentEpisodes, EnvironmentSteps
from rl_coach.environments.gym_environment import GymVectorEnvironment
from rl_coach.exploration_policies.categorical import CategoricalParameters

from rl_coach.filters.filter import InputFilter
from rl_coach.filters.observation.observation_rgb_to_y_filter import ObservationRGBToYFilter
from rl_coach.filters.observation.observation_stacking_filter import ObservationStackingFilter
from rl_coach.filters.observation.observation_to_uint8_filter import ObservationToUInt8Filter
from rl_coach.filters.observation.observation_clipping_filter import ObservationClippingFilter

from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.graph_managers.graph_manager import ScheduleParameters
from rl_coach.schedules import LinearSchedule

from rl_coach.base_parameters import DistributedCoachSynchronizationType, EmbedderScheme
####################
# Graph Scheduling #
####################

schedule_params = ScheduleParameters()
schedule_params.improve_steps = TrainingSteps(10000000)
schedule_params.steps_between_evaluation_periods = EnvironmentEpisodes(40)
schedule_params.evaluation_steps = EnvironmentEpisodes(5)
schedule_params.heatup_steps = EnvironmentSteps(0)

#########
# Agent #
#########
agent_params = ClippedPPOAgentParameters()
agent_params.network_wrappers['main'].input_embedders_parameters = {
        'STEREO_CAMERAS': InputEmbedderParameters(
            scheme=[
                Conv2d(32, 8, 4),
                Conv2d(32, 4, 2),
                Conv2d(64, 4, 2),
                Conv2d(64, 3, 1),
                Conv2d(64, 2, 1),
                Dense(256)
            ],
            activation_function='relu', dropout_rate=0.3),
        'LIDAR': InputEmbedderParameters(
            scheme=[
                Dense(64),
                Dense(32)
             ],
             activation_function='relu', dropout_rate=0.3)      
        }

agent_params.network_wrappers['main'].middleware_parameters = \
     FCMiddlewareParameters(
         scheme=[
             Dense(256)
         ],
         activation_function='relu', dropout_rate=0.3
     )

agent_params.network_wrappers['main'].learning_rate = 0.0003
#agent_params.network_wrappers['main'].middleware_parameters.activation_function = 'relu'
agent_params.network_wrappers['main'].batch_size = 128
agent_params.network_wrappers['main'].optimizer_epsilon = 1e-5
agent_params.network_wrappers['main'].adam_optimizer_beta2 = 0.999

# agent_params.network_wrappers['main'].learning_rate_decay_steps = 60000
# agent_params.network_wrappers['main'].learning_rate_decay_rate = 0.95
# agent_params.network_wrappers['main'].input_embedders_parameters['observation'].batchnorm = True
# agent_params.network_wrappers['main'].input_embedders_parameters['observation'].dropout_rate = 0.3
# agent_params.network_wrappers['main'].l2_regularization = 2e-5
agent_params.algorithm.beta_entropy = 0.001

agent_params.algorithm.clip_likelihood_ratio_using_epsilon = 0.2
agent_params.algorithm.clipping_decay_schedule = LinearSchedule(1.0, 0, 1000000)
agent_params.algorithm.gae_lambda = 0.95
agent_params.algorithm.discount = 0.999
agent_params.algorithm.optimization_epochs = 3
agent_params.algorithm.estimate_state_value_using_gae = True
agent_params.algorithm.num_steps_between_copying_online_weights_to_target = EnvironmentEpisodes(20)
agent_params.algorithm.num_consecutive_playing_steps = EnvironmentEpisodes(20)
#huber loss
agent_params.network_wrappers['main'].replace_mse_with_huber_loss = True

agent_params.exploration = CategoricalParameters()

agent_params.algorithm.distributed_coach_synchronization_type = DistributedCoachSynchronizationType.SYNC


###############
# Environment #
###############
SilverstoneInputFilter = InputFilter(is_a_reference_filter=True)

# SilverstoneInputFilter.add_observation_filter('left_camera', 'to_grayscale', ObservationRGBToYFilter())
# SilverstoneInputFilter.add_observation_filter('left_camera', 'to_uint8', ObservationToUInt8Filter(0, 255))
# SilverstoneInputFilter.add_observation_filter('left_camera', 'stacking', ObservationStackingFilter(1))
SilverstoneInputFilter.add_observation_filter('STEREO_CAMERAS', 'to_uint8', ObservationToUInt8Filter(0, 255))
SilverstoneInputFilter.add_observation_filter('LIDAR', 'clipping', ObservationClippingFilter(0.1, 0.5))

env_params = GymVectorEnvironment()
env_params.default_input_filter = SilverstoneInputFilter
env_params.level = 'DeepRacerRacetrackCustomActionSpaceEnv-v0'

vis_params = VisualizationParameters()
vis_params.dump_mp4 = False

########
# Test #
########
preset_validation_params = PresetValidationParameters()
preset_validation_params.test = True
preset_validation_params.min_reward_threshold = 400
preset_validation_params.max_episodes_to_achieve_reward = 1000

graph_manager = BasicRLGraphManager(agent_params=agent_params, env_params=env_params,
                                    schedule_params=schedule_params, vis_params=vis_params,
                                    preset_validation_params=preset_validation_params)
