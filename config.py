# -*- coding: UTF-8 -*-

import os
import logging
import yaml

logger = logging.getLogger(__name__)

CONFIGS_DIR_NAME = 'config'
COMMON_CONFIG_NAME = 'common.yml'


def get_common_configs():
    """Return configuration as dict from common file."""

    config_path = os.path.join(os.path.dirname(__file__), CONFIGS_DIR_NAME, COMMON_CONFIG_NAME)
    return yaml.load(open(config_path))
