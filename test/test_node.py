import time
import unittest

import launch
import launch.actions
import launch_ros.actions
import launch_testing.actions
import launch_testing.markers
import pytest
import rclpy
from rclpy.node import Node


@pytest.mark.launch_test
@launch_testing.markers.keep_alive
def generate_test_description():
    return launch.LaunchDescription([
        launch.actions.TimerAction(
            period=5.0,
            actions=[
                launch_ros.actions.Node(
                    executable='start_simulator.py',
                    package='nimbro_webots_sim',
                    name='demo_node_1'
                ),
            ]),
        launch_testing.actions.ReadyToTest()
    ])


class TestFixture(unittest.TestCase):

    def test_node_start(self, proc_output):
        rclpy.init()
        node = Node('test_node')
        assert wait_for_node(node, 'demo_node_1', 20.0), 'Node not found !'
        rclpy.shutdown()
        # self.__ros_node.destroy_node()
        # rclpy.shutdown(context=self.__ros_context)

    def shutdown(self):
        self.__ros_node.destroy_node()
        rclpy.shutdown(context=self.__ros_context)


def wait_for_node(dummy_node, node_name, timeout=20.0):
    start = time.time()
    flag = False
    print('Waiting for node...')
    while time.time() - start < timeout and not flag:
        flag = node_name in dummy_node.get_node_names()
        time.sleep(0.1)

    return flag