# -*- coding: UTF-8 -*-
# Copyright (c) 2014 Daniele Ciriello. All Rights Reserved.

# This file is part of Pydiamond.

# Pydiamond is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation version 2 and no later version.

# Pydiamond is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License version 2 for more details.

# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc. 51 Franklin
# St, Fifth Floor, Boston, MA 02110-1301 USA.


class Pattern():

    def __init__(self):
        pass

    def in_range(self, target, min_, max_):
        return target >= min_ and max_ >= target

    def is_straight_pattern(self, color_map, x, y):
        c = color_map[x][y][2]
        if (x <= 7 and color_map[x + 1][y][2] == c and color_map[x + 2][y][2] == c):
            return True
        if (x >= 2 and color_map[x - 1][y][2] == c and color_map[x - 2][y][2] == c):
            return True
        if (y <= 6 and color_map[x][y + 1][2] == c and color_map[x][y + 2][2] == c):
            return True
        if (y >= 2 and color_map[x][y - 1][2] == c and color_map[x][y - 2][2] == c):
            return True

        return False

    def is_l_pattern(self, color_map, x, y):
        c = color_map[x][y][2]

        if (x <= 8 and y <= 7 and
            ((color_map[x + 1][y][2] == c and color_map[x + 1][y + 1][2] == c) or
             (color_map[x][y + 1][2] == c and color_map[x + 1][y + 1][2] == c))):
            return True
        if (x <= 8 and y >= 1 and
           ((color_map[x + 1][y][2] == c and color_map[x + 1][y - 1][2] == c) or
                (color_map[x][y - 1][2] == c and color_map[x + 1][y - 1][2] == c))):
            return True
        if (x >= 1 and y <= 7 and
           ((color_map[x - 1][y][2] == c and color_map[x - 1][y + 1][2] == c) or
                (color_map[x][y + 1][2] == c and color_map[x - 1][y + 1][2] == c))):
            return True
        if (x >= 1 and y >= 1 and
            ((color_map[x - 1][y][2] == c and color_map[x - 1][y - 1][2] == c) or
             (color_map[x][y - 1][2] == c and color_map[x - 1][y - 1][2] == c))):
            return True

        return False

    def get_next_combo(self, color_map):
        for y in range(8, -1, -1):
            for x in range(10):
                if color_map[x][y][2] is not 'grey' and ((
                    color_map[x][y][2] == 'special') or (
                        self.is_straight_pattern(color_map, x, y)) or(
                        self.is_l_pattern(color_map, x, y))):
                            return color_map[x][y][0], color_map[x][y][1]

        return -1, -1
