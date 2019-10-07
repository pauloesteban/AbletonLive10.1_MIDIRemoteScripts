# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/UC33e/config.py
# Compiled at: 2019-04-09 19:23:45
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {'STOP': GENERIC_STOP, 
   'PLAY': GENERIC_PLAY, 'REC': GENERIC_REC, 'LOOP': GENERIC_LOOP, 
   'RWD': GENERIC_RWD, 'FFWD': GENERIC_FFWD}
DEVICE_CONTROLS = (
 (
  GENERIC_ENC1, 0), (GENERIC_ENC2, 1), (GENERIC_ENC3, 2), (GENERIC_ENC4, 3),
 (
  GENERIC_ENC5, 4), (GENERIC_ENC6, 5), (GENERIC_ENC7, 6), (GENERIC_ENC8, 7))
VOLUME_CONTROLS = (
 (
  GENERIC_SLI1, 0), (GENERIC_SLI2, 1), (GENERIC_SLI3, 2),
 (
  GENERIC_SLI4, 3), (GENERIC_SLI5, 4), (GENERIC_SLI6, 5), (GENERIC_SLI7, 6),
 (
  GENERIC_SLI8, 7))
TRACKARM_CONTROLS = (
 GENERIC_BUT1, GENERIC_BUT2, GENERIC_BUT3, GENERIC_BUT4,
 GENERIC_BUT5, GENERIC_BUT6, GENERIC_BUT7, GENERIC_BUT8)
BANK_CONTROLS = {'TOGGLELOCK': GENERIC_BUT9, 
   'BANKDIAL': -1, 
   'NEXTBANK': GENERIC_PAD5, 
   'PREVBANK': GENERIC_PAD1, 'BANK1': -1, 
   'BANK2': -1, 'BANK3': -1, 'BANK4': -1, 'BANK5': -1, 
   'BANK6': -1, 'BANK7': -1, 'BANK8': -1}
CONTROLLER_DESCRIPTIONS = {'INPUTPORT': 'UC-33 USB MIDI Controller (Port 1)', 'OUTPUTPORT': 'UC-33 USB MIDI Controller (Port 1)', 'CHANNEL': 0}
MIXER_OPTIONS = {'NUMSENDS': 2, 
   'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1), 
   'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1), 
   'MASTERVOLUME': 28}