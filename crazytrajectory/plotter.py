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

        self.fig = plt.figure()
        self.ax = self.fig.gca(projection='3d')
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_zlabel('Z axis')
        self.ax.scatter(start['x'], start['y'], start['z'], color='red',
                        marker='o')
        self.ax.text(start['x'], start['y'], start['z'], 'Start position')
        self.ax.scatter(end['x'], end['y'], end['z'], color='g', marker='x')
        self.ax.text(end['x'], end['y'], end['z'], 'Landing zone')
        plt.suptitle('CrazyTrajectory')
        self.ax.set_zlim3d(0, 10)

        plt.draw()
        plt.pause(0.001)

    def add_trajectory(self, points):
        self.ax.plot(points['x'], points['y'], points['z'], label='Trajectory')
        plt.draw()
        plt.pause(0.001)

    def add_copter_point(self, point):
        self.ax.scatter(point['x'], point['y'], point['z'], color='red',
                        marker='*', label='Crazyflie')
        plt.draw()
        plt.pause(0.001)

if __name__ == '__main__':
    trap = TrajectoryPlotter({'x': 0, 'y': 0, 'z': 0}, {'x': 4, 'y': 5, 'z': 0})
    time.sleep(10)
    # trap.add_trajectory([[0, 2, 4], [0, 2, 5], [0, 5, 0]])
    for i in range(0, 10):
        time.sleep(1)
        trap.add_copter_point({'x': i, 'y': i, 'z': i % 5})
    plt.ioff()
    plt.show()
