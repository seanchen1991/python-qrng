#!/bin/env python

from interface import QuantumDevice
from simulator import SingleQubitSimulator

def qrng(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()

if __name__ == "__main__":
    qsim = SingleQubitSimulator()

    for _ in range(10):
        random_sample = qrng(qsim)
        print(f"QRNG returned {random_sample}")