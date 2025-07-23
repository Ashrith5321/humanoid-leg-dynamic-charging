#include "rclcpp/rclcpp.hpp"

class DummyNode : public rclcpp::Node
{
public:
  DummyNode() : Node("dummy_node")
  {
    RCLCPP_INFO(this->get_logger(), "Dummy node has started!");
  }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<DummyNode>());
  rclcpp::shutdown();
  return 0;
}
