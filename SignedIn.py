import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#import numpy
from numpy import *

Theta1 = load('Theta1.npy')
Theta2 = load('Theta2.npy')

#global count
class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    count = 0
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures


    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        global count
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

#print outputList
        if not outputList:
            count = 0
        else:
            count = count + 1

        if count == 20:
            count = 0

# print "No more input needed"
            #controller.disconnect()
            
            outputList = array([outputList])
            actualOutputMatrix= matrix(outputList)
            print predict_value (Theta1, Theta2, actualOutputMatrix)

            time.sleep(5)


        #print len(outputList)

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller

    controller.add_listener(listener)

    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
    # Remove the sample listener when done
        controller.remove_listener(listener)

def sigmoid(value):
    return 1/(1+exp(-1*value))

def predict_value(Theta1, Theta2, X):
    m = X.shape[0]
    h1 = sigmoid(X.dot(Theta1.T))
    h1 = hstack((ones((m,1)),h1))
    h2 = sigmoid(h1.dot(Theta2.T))
    p = argmax(h2,axis=1)
    return p

# frame should be numpy array without the 1 in the first position,which signifies right hand,
# and without the label value at the last index

#from scipy.special import expit as sigmoid

if __name__ == "__main__":
    main()
