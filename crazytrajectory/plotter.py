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
        self.ax.set_zlim3d(-10, 0)

        plt.draw()
        plt.pause(0.001)

    def set_endpoints(self, start, end):
        self.ax.scatter(start['x'], start['y'], start['z'], color='red',
                        marker='o')
        self.ax.text(start['x'], start['y'], start['z'], 'Start position')
        self.ax.scatter(end['x'], end['y'], end['z'], color='g', marker='x')
        self.ax.text(end['x'], end['y'], end['z'], 'Landing zone')

    def add_trajectory(self, points):
        x = []
        y = []
        z = []
        for p in points:
            x.append(p['x'])
            y.append(p['y'])
            z.append(p['z'])
        self.ax.plot(x, y, zs=z, label='Trajectory')

    def add_copter_point(self, point):
        self.ax.scatter(point['x'], point['y'], point['z'], color='red',
                        marker='*', label='Crazyflie')
                        
    def update(self):
        plt.draw()
        plt.pause(0.5)
