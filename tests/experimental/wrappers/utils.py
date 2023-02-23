"""Utility functions for testing the experimental wrappers."""
import gymnasium as gym
from tests.spaces.utils import TESTING_SPACES, TESTING_SPACES_IDS
from tests.testing_env import GenericTestEnv


SEED = 42
ENV_ID = "CartPole-v1"
DISCRETE_ACTION = 0
NUM_ENVS = 3
NUM_STEPS = 20


def record_obs_reset(self: gym.Env, seed=None, options: dict = None):
    """Records and uses an observation passed through options."""
    return options["obs"], {"obs": options["obs"]}


def record_random_obs_reset(self: gym.Env, seed=None, options=None):
    """Records random observation generated by the environment."""
    obs = self.observation_space.sample()
    return obs, {"obs": obs}


def record_action_step(self: gym.Env, action):
    """Records the actions passed to the environment."""
    return 0, 0, False, False, {"action": action}


def record_random_obs_step(self: gym.Env, action):
    """Records the observation generated by the environment."""
    obs = self.observation_space.sample()
    return obs, 0, False, False, {"obs": obs}


def record_action_as_obs_step(self: gym.Env, action):
    """Uses the action as the observation."""
    return action, 0, False, False, {"obs": action}


def check_obs(
    env: gym.Env,
    wrapped_env: gym.Wrapper,
    transformed_obs,
    original_obs,
    strict: bool = True,
):
    """Checks that the original and transformed observations using the environment and wrapped environment.

    Args:
        env: The base environment
        wrapped_env: The wrapped environment
        transformed_obs: The transformed observation by the wrapped environment
        original_obs: The original observation by the base environment.
        strict: If to check that the observations aren't contained in the other environment.
    """
    assert (
        transformed_obs in wrapped_env.observation_space
    ), f"{transformed_obs}, {wrapped_env.observation_space}"
    assert (
        original_obs in env.observation_space
    ), f"{original_obs}, {env.observation_space}"

    if strict:
        assert (
            transformed_obs not in env.observation_space
        ), f"{transformed_obs}, {env.observation_space}"
        assert (
            original_obs not in wrapped_env.observation_space
        ), f"{original_obs}, {wrapped_env.observation_space}"


TESTING_OBS_ENVS = [GenericTestEnv(observation_space=space) for space in TESTING_SPACES]
TESTING_OBS_ENVS_IDS = TESTING_SPACES_IDS

TESTING_ACTION_ENVS = [GenericTestEnv(action_space=space) for space in TESTING_SPACES]
TESTING_ACTION_ENVS_IDS = TESTING_SPACES_IDS
