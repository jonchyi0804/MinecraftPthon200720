# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:30:49 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
i=0
while i<=150 :
    i=i + 1
    mc.setBlock(x,y+i,z,57)
    