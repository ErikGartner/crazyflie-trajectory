from .trajectory import CrazyTrajectory
from .plotter import TrajectoryPlotter


def start():
    tp = TrajectoryPlotter()
    ct = CrazyTrajectory(tp)
    ct.start()
