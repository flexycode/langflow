import pytest

from langflow.graph import Graph
from langflow.processing.load import load_flow_from_json


def test_load_flow_from_json():
    """Test loading a flow from a json file"""
    loaded = load_flow_from_json(pytest.BASIC_EXAMPLE_PATH)
    assert loaded is not None
    assert isinstance(loaded, Graph)


def test_load_flow_from_json_with_tweaks():
    """Test loading a flow from a json file and applying tweaks"""
    tweaks = {"dndnode_82": {"model_name": "gpt-3.5-turbo-16k-0613"}}
    loaded = load_flow_from_json(pytest.BASIC_EXAMPLE_PATH, tweaks=tweaks)
    assert loaded is not None
    assert isinstance(loaded, Graph)
