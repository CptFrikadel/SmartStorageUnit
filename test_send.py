#! /usr/bin/python3

from oocsi import OOCSI
import sys

if len(sys.argv) < 4:
    print("Usage:", sys.argv[0], "<channel> <message key> <message value>")
    exit()

oocsi_inst = OOCSI('Testsenderinator', 'oocsi.id.tue.nl')

message = {sys.argv[2] : sys.argv[3]}
#message['weight'] = 666

oocsi_inst.send(sys.argv[1], message)
oocsi_inst.stop()
