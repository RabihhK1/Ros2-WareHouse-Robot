from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='warehouse_robot',
            executable='deliver_item_server',
            name='item_delivery_server',
        ),
        Node(
            package='warehouse_robot',
            executable='stock_checker_server',
            name='stock_checker_server',
        ),
        Node(
            package='warehouse_robot',
            executable='deliver_item_client',
            name='item_delivery_client',
            parameters=[{
    'item_name': LaunchConfiguration('item_name'),  
    'quantity': LaunchConfiguration('quantity')
}],
        ),
        Node(
            package='warehouse_robot',
            executable='stock_checker_client',
            name='stock_checker_client',
        ),
    ])