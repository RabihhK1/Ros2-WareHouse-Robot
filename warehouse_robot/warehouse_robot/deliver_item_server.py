import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from action_msgs.msg import GoalStatus
from interfaces.action import DeliverItem
import asyncio 
from warehouse_robot.stock_checker_client import StockCheckerClient
import time
class ItemDeliveryServer(Node):
   
    def __init__(self):
        super().__init__('item_delivery_server')
        
        self._action_server = ActionServer(
            self,
            DeliverItem,
            'deliver_item',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
            
            handle_accepted_callback=self.handle_accepted_callback
        )
        self.stock_checker = StockCheckerClient()
        
        self.get_logger().info('Item Delivery Action Server has been started.')

    def goal_callback(self, goal_request):
        
        stock_level = self.stock_checker.send_request(goal_request.item_name)
       
        if stock_level < int(goal_request.quantity):
            self.get_logger().info(f'Not enough qty for {goal_request.item_name}')
            return GoalResponse.REJECT
        
        self.get_logger().info(f'Accepting goal request for {goal_request.quantity} of {goal_request.item_name}')
        return GoalResponse.ACCEPT
    def handle_accepted_callback(self, goal_handle):
        self.get_logger().info('Goal accepted, executing...')
        goal_handle.execute()
    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        quantity=goal_handle.request.quantity
        feedback_msg = DeliverItem.Feedback()
        result_msg = DeliverItem.Result()

        for i in range(quantity):
            if goal_handle.is_cancel_requested:
                self.get_logger().info('Goal preempted')
                goal_handle.canceled()
                result_msg.success = False
                result_msg.message = 'Delivery canceled'
                goal_handle.publish_feedback(feedback_msg)
                return result_msg

            feedback_msg.status = f'Delivering item {i+1}/{quantity}'
            self.get_logger().info(feedback_msg.status)
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.1)  
        goal_handle.succeed()
        result_msg.success = True
        result_msg.message = 'Item delivered successfully'
        return result_msg

def main(args=None):
    rclpy.init(args=args)
    item_delivery_server = ItemDeliveryServer()
    rclpy.spin(item_delivery_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
