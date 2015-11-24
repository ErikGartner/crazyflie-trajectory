#!/usr/bin/env python3
import zmq

context = zmq.Context()

kinect_conn = context.socket(zmq.PULL)
kinect_conn.connect("tcp://127.0.0.1:9999")
