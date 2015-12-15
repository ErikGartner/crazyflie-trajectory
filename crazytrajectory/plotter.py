"""
Plot trajectory in a sexy 3D plot
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import numpy as np


class TrajectoryPlotter():

    def __init__(self):
        plt.ion()
        plt.show()

        self.fig = plt.figure()
        self.ax = self.fig.gca(projection='3d')
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')
        plt.suptitle('CrazyTrajectory')
        self.ax.set_zlim3d(0, 10)
        self.ax.set_xlim3d(-10, 10)
        self.ax.set_ylim3d(-10, 10)
        plt.axis(xmin=-10, xmax=10, ymin=-10, ymax=10, zmin=0, zmax=10)

        plt.draw()
        plt.pause(0.001)

    def set_endpoints(self, start, end):
        self.ax.scatter(start['x'], start['y'], start['z'], color='red',
                        marker='o')
        self.ax.text(start['x'], start['y'], start['z'], 'Start position')
        self.ax.scatter(end['x'], end['y'], end['z'], color='g', marker='x')
        self.ax.text(end['x'], end['y'], end['z'], 'Landing zone')
        self.ax.scatter(1, 1, 1, color='g', marker='x') # this actually works
        plt.draw()
        plt.pause(0.001)


    def set_trajectory(self, points):
        print("Plotting trajectory points x:{}, y:{}, z:{}".format(points[0], points[1], points[2]))
        self.ax.scatter(2, 2, 2, color='g', marker='x') # this has no effect for some reason
        # of course what we want to do is self.ax.plot(points[0], points[1], points[2], label='Trajectory')
        # but that does not work either...
        plt.draw()
        plt.pause(0.001)

    def add_copter_point(self, point):
        self.ax.scatter(point['x'], point['y'], point['z'], color='red',
                        marker='*', label='Crazyflie')
        plt.draw()
        plt.pause(0.001)
