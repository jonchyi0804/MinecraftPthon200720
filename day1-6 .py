# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:04:51 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()


while True :
    x,y,z, = mc.player.getTilePos()
    mc.postToChat("你現在在x:"+str(x)+"y:"+str(y)+"z:"+str(z))
    