from hub import light_matrix
from hub import port
from app import sound
import motor_pair
import runloop
import motor
import distance_sensor
import color_sensor
import color
import app

async def main():
    # write your code here
    await light_matrix.write("Hi!")

    # Motors connected to the wheels
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    motor.run(motor_pair.PAIR_1,  1000)

    # Motors for arms to collect and retrieve materials, when program starts, arms raise up
    motor_pair.pair(motor_pair.PAIR_2, port.E, port.F)
    motor.run(motor_pair.PAIR_2, 1000)
    findRock()
    pickUp()
    
    #return back to base
    motor.run_for_degrees(motor_pair.PAIR_1, 180, 100) 
    motor.run(motor_pair.PAIR_1, 1000)


def findRock():
    while distance_sensor.distance(port.C) == -1: # returns -1 when it cant read an object
        pass
        if color_sensor.color(port.D) is color.YELLOW or color_sensor.color(port.D) is color.BLACK:
            motor.stop(motor_pair.PAIR_1)
            identifyMineral()

def identifyMineral():
    # play two different sounds to show judges our rover can differentiate between the two mineral colors
    if color_sensor.color(port.D) is color.YELLOW:
        sound.play('Collect', 80, 0, 0) 
    elif color_sensor.color(port.D) is color.BLACK:
        sound.play('Applause 3', 80, 100)
def pickUp():
    # close arms to retrieve rock or other item
    motor.run_for_degrees(motor_pair.PAIR_2, 50, 1000) 







    

    

runloop.run(main())
