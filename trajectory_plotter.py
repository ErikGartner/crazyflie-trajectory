"""
    Plot trajectory in a sexy 3D plot
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import numpy as np

class TrajectoryPlotter():

    def __init__(self, start, end):
        plt.ion()
        plt.show()

        print("start and end points set")
        self.fig = plt.figure()
        self.ax = self.fig.gca(projection='3d')
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')
        self.ax.scatter(start[0], start[1], start[2], color='red', marker='o')
        self.ax.text(start[0], start[1], start[2], 'Start position')
        self.ax.scatter(end[0], end[1], end[2], color='g', marker='x')
        self.ax.text(end[0], end[1], end[2], 'Landing zone')
        plt.suptitle('CrazyTrajectory')
        self.ax.set_zlim3d(0, 10)
        
        plt.draw()
        plt.pause(0.001)

    def add_trajectory(self, points):
        print("trajectory added")
        self.ax.plot(points[0], points[1], points[2], label='Trajectory')
        plt.draw()
        plt.pause(0.001)

    def add_copter_point(self, x, y, z):
        print("copter point added")
        self.ax.scatter(x, y, z, color='red', marker='*', label='Crazyflie')
        plt.draw()
        plt.pause(0.001)

if __name__ == '__main__':
    trap = TrajectoryPlotter([0,0,0], [4,5,0])
    time.sleep(10)
    trap.add_trajectory([[0,2,4],[0,2,5],[0,5,0]])
    for i in range(0,10):
        time.sleep(1)
        trap.add_copter_point(i,i,i%5)
    plt.ioff()
    plt.show()
