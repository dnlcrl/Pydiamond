# -*- coding: UTF-8 -*-
# Copyright (c) 2014 Daniele Ciriello. All Rights Reserved.

# This file is part of diamonddashsolver.

# diamonddashsolver is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation version 2 and no later version.

# diamonddashsolver is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License version 2 for more details.

# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc. 51 Franklin
# St, Fifth Floor, Boston, MA 02110-1301 USA.
import time
from pytomator.pytomator import *
from operator import itemgetter
from pattern import Pattern

class Bot():

    """docstring for Bot"""

    def __init__(self, zero, width, height, diamond_width, diamond_height, sample_distance, sensitivity, counter_threshold):
        self.zero = zero
        self.width = width
        self.height = height
        self.diamond_height = diamond_height
        self.diamond_width = diamond_width
        self.grid_width = width * diamond_width
        self.grid_heigth = height * diamond_height
        self.sample_distance = sample_distance
        self.sample_total_distance = 2 * sample_distance + 1
        self.sample_area = self.sample_total_distance * \
            self.sample_total_distance
        #self.sensitivity = sensitivity
        # [[],[]] #new ColorTypes[width, height]
        self.grid = [
            [[] for i in range(self.height)] for i in range(self.width)]
        # ]new int[width, height]
        self.counter = [[0 for i in range(self.height)] for i in range(self.width)]
        self.counter_threshold = counter_threshold
        self.buffer = []  # new byte[4 * self.gridWidth * self.gridHeight]
        self.board = []  # new byte[4 * self.gridWidth * self.gridHeight]
        self.running = True
        self.fail = 0

    def next(self):
        # screen capture
        #self.board = screenshot(path=None, region=None, box=None )# [
                                # self.zero[0], self.zero[1], self.grid_width, self.grid_heigth])
        self.generate_grid()
        for x in range(self.width):
            for y in range(self.height):
                #if self.grid[x][y][2] is 'special':
                 #   c = [self.grid[x][y][0], self.grid[x][y][1]]
                 #   if (c[0] > self.zero[0] and c[1] > self.zero[1]) and (c[0] > self.zero[0] + self.width and c[1] > self.zero[1] + self.height):
                 #       mouseclick(c[0], c[1])
                  #      time.sleep(0.3)
                  #      return
                try:
                    if self.grid[x][y][2] is 'grey':
                        self.counter[x][y] += 1
                        if self.counter[x][y] == self.counter_threshold:
                            self.grid[x][y][2] = 'special'
                    else:
                        self.counter[x][y] = 0
                except:
                    print 'error at x: ', x, ', y: ', y
        c = Pattern().get_next_combo(self.grid)
        mouseclick(c[0]+self.zero[0], c[1]+self.zero[1])
        time.sleep(0.2)

    def generate_grid(self):
        err = 0
        def my_filter(x, y, t):
            greater_than_x = t[0] > ((x * self.diamond_width))
            greater_than_y = t[1] > ((y * self.diamond_height))
            less_than_next_x = t[0] < (((x + 1) * self.diamond_width))
            less_than_next_y = t[1] < (((y + 1) * self.diamond_height))

            return ((greater_than_x and less_than_next_x) and (greater_than_y and less_than_next_y))

        centers = []
        board = screenshot(path=None, region=None, box=[
                                self.zero[0], self.zero[1], self.grid_width+self.zero[0], self.grid_heigth+self.zero[1]])
        #board = screenshot(path='s.png', region=None, box=[
         #                       self.zero[0], self.zero[1], self.grid_width+self.zero[0], self.grid_heigth+self.zero[1]])
        for i in ['red', 'green', 'blue', 'yellow', 'purple']:
            f = i + '.png'
            matched = match(f, large_image=board, all_matches=True)
            centers = centers + [p + [i] for p in matched]

        for x in range(self.width):
            for y in range(self.height):
                try:
                    self.grid[x][y] = filter(lambda t: my_filter(x, y, t), centers)[0]
                except Exception, e:
                    self.grid[x][y] = [(x*self.diamond_width) + self.diamond_width/2, (y*self.diamond_height) + self.diamond_height/2, 'grey']
                    err += 1
                    if err == 50:
                        time.sleep(1)
                        self.fail += 1
                        if self.fail == 7:
                            print 'quitting...'
                            self.running = False
                            return



