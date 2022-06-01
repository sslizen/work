
# Ждём контроллера дальше понимаем что испарвлять и добавлять
 
import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand # На глаз, опять сыро, ждём контроллера 
 
class MoveItFkDemo:
    def __init__(self):
        # Инициализировать API move_group
        moveit_commander.roscpp_initialize(sys.argv)
 
                 # Под вопросом зависит от контроллера
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
                 # Создаём группу для движения 
        arm = moveit_commander.MoveGroupCommander('arm')
        
                 # Создаём группу для захвата
        gripper = moveit_commander.MoveGroupCommander('gripper')
        
                 # Ошибка манипулятора, допустимая
        arm.set_goal_joint_tolerance(0.001)
        gripper.set_goal_joint_tolerance(0.001)
        
                 # Исходное положение
        arm.set_named_target('arm_init_pose')
        arm.go()
        rospy.sleep(2)
         
                 # Положение захвата
        '''
        gripper.set_joint_value_target([0.01])
        gripper.go()
        rospy.sleep(1)
        '''
                 # Положение руки в радианах ( под вопросом )
        joint_positions = [1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708]
        result=arm.set_joint_value_target(joint_positions)
        rospy.loginfo(str(result))
                 
                 # Управление рукой робота, чтобы завершить движение
        arm.go()
        joint=arm.get_current_joint_values()
        print("final joint=",joint)
        pose=arm.get_current_pose('link7')
        print('pose=',pose)
        rospy.sleep(1)
        
                 # Выход из управления
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)
 
if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
