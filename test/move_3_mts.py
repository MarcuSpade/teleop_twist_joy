#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

def move_robot():
    # Inicializa o nó ROS
    rospy.init_node('move_robot_node', anonymous=True)
    
    # Crie um publisher para publicar comandos de velocidade no tópico "/cmd_vel"
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    # Crie um objeto Twist para enviar comandos de velocidade
    cmd_vel = Twist()
    
    # Defina a velocidade linear (metros por segundo) e a velocidade angular (radianos por segundo)
    cmd_vel.linear.x = -0.2  # Exemplo de velocidade linear
    cmd_vel.angular.z = 0.0  # Exemplo de velocidade angular
    
    # Configure a taxa de publicação (por exemplo, 10 Hz)
    rate = rospy.Rate(10)
    
    # Tempo necessário para percorrer 3 metros a 0.2 m/s
    time_to_travel_3_meters = 15.0  # 3 / 0.2 = 15 segundos
    
    # Tempo inicial
    start_time = rospy.get_time()
    
    while not rospy.is_shutdown():
        # Publica comandos de velocidade
        cmd_vel_pub.publish(cmd_vel)
        
        # Verifique se o robô alcançou a distância desejada
        if (rospy.get_time() - start_time) >= time_to_travel_3_meters:
            # Pare o robô
            cmd_vel.linear.x = 0.0
            cmd_vel.angular.z = 0.0
            cmd_vel_pub.publish(cmd_vel)
            rospy.loginfo("Robô chegou a 3 metros.")
            break
        
        # Espere até a próxima iteração
        rate.sleep()

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
