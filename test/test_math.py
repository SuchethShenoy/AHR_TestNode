import pytest
import rclpy

class TestNode:
    def setup_method(self):
        rclpy.init()
        self.node = rclpy.create_node('test_node')

    def test_my_node(self):
        # Test your node here
        assert 2 + 2 == 4

    def teardown_method(self):
        self.node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    pytest.main()