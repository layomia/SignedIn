import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import numpy as np


#global variable
#Matrix=np.empty(2,2) initialize 2x2 matrix
#np.concantenate(a,b) concantenates a and b row wise
#FrameDataOutputLength=136
#rowLen=136
#isFirst=1
#outputMatrix=np.empty(shape=(0,136) float)

outputMatrix=[]
class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        outputList=[]
        frame = controller.frame()

        # Get hands
        for hand in frame.hands:

            handType = 0 if hand.is_left else 1 #Left = 0


            outputList.append(handType)
            #outputList.append(hand.id)

            # Get fingers
            for finger in hand.fingers:

                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)

                    outputList.append(float(bone.prev_joint[0]))
                    outputList.append(float(bone.prev_joint[1]))
                    outputList.append(float(bone.prev_joint[2]))

                outputList.append(float(finger.bone(3).next_joint[0]))
                outputList.append(float(finger.bone(3).next_joint[1]))
                outputList.append(float(finger.bone(3).next_joint[2]))

                for b in range(0, 4):
                    bone = finger.bone(b)
                    outputList.append(float(bone.direction[0]))
                    outputList.append(float(bone.direction[1]))
                    outputList.append(float(bone.direction[2]))

        print outputList
        outputMatrix.append(outputList)




def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

    for la in range(0,len(outputMatrix)):
            outputMatrix[la].append(3) #replace 3 with identifier!
    actualOutputMatrix=np.matrix(outputMatrix)
    np.save('Training22', actualOutputMatrix)
    #Use pickle and imports if there are compatibility issues


if __name__ == "__main__":
    main()
