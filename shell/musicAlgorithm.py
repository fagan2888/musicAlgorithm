
# created by Zhao Liyuan(Chinese name) / Leon(English name)

# this file using python to realize MUSIC algrithm

# MUSIC algorithm can help us to find out the direction of signal

# it is an algorithm based on linear algebra

import numpy as np
import pandas as pd
from datetime import datetime
from time import strftime
from ipdb import set_trace
#import optparse import OptionParser


class music:

    def __init__(self, detector, noise):
        self.detector = detector
        self.noise = noise

    def algrithm(self):
        # load noise and outputs from detectors
        detector = self.detector
        noise = self.noise
        detectorMatrix = np.dot(detector, detector.H)
        noiseMatrix = np.dot(noise, np.ones((1,len(noise))))
        signalMatrix = detectorMatrix - noiseMatrix
        
        # doing matirx decomposition on signalMatrix
        alpha = np.linalg.eig(signalMatrix)[1]

        # doing matrix decomposition on noiseMatrix
        noiseVector = np.linalg.eig(noiseMatrix)[1]

        # calculate direction
        direction = 1 / np.dot(np.dot(np.dot(alpha.H, noiseVector), noiseVector.H), alpha)        
        
        print(direction)
        return direction

if __name__ == '__main__':
#    optParser = OptionParser()
    detector = np.matrix([[1],[2],[3],[4],[5],[6]]) 
    noise = np.matrix([[0.1],[0.1],[0.1],[0.1],[0.1],[0.1]])
    # six detectors in all
#    optParser.add_option('-d', '--detector', help = 'signals got from detectors', type = , dest = 'detector', defalut = )
#    options,args = optParser.parse_args()
#    detector = options.detector
    music = music(detector, noise)
    music.algrithm()

