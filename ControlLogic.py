# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:12:28 2023


@author: louis
"""

import numpy as np


def toControl(opcodeFile, destFile):
    dest = open(destFile, 'w')
    source = open(opcodeFile)

    sources = source.readlines()

    controls = []
    opcodes = []

    for line in sources:
        x = line.split()
        a = int(x[0], 16)
        controls.append((a, int(x[1], 2)))
        opcodes.append(a)

    outputs = np.zeros(max(opcodes))

    out = []

    out.append("v2.0 raw\n0\n")

    for control in controls:
        outputs[control[0] - 1] = control[1]

    for output in outputs:
        x = hex(int(output))
        out.append(x[2:] + "\n")

    dest.writelines(out)

    dest.close()
    source.close()

    return out


sourceFile = input("Enter source file .txt :")

targetFile = input("Enter target file name .txt :")

toControl(sourceFile, targetFile)
