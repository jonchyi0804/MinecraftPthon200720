# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:01:57 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x = 314
y = 123
z = 220

mc.player.setTilePos(x,y,z)