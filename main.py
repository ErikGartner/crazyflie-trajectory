#!/usr/bin/env python3
import zmq

context = zmq.Context()

status_con = context.socket(zmq.PULL)
status_con.connect("tcp://127.0.0.1:9001")

controller_con = context.socket(zmq.PUSH)
controller_con.connect("tcp://127.0.0.1:9002")

class CrazyTrajectory(Thread):
    
