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

from bot import Bot
from pytomator.pytomator import *

GRID_WIDTH = 10
GRID_HEIGHT = 9
SENSITIVITY = 0.5
COUNTER_THRESHOLD = 3


def game_box():
    pass


def main():

    # run this from the home
    # https://www.facebook.com/appcenter/diamonddash?
    # fb_source=appcenter_getting_started&fbsid=114
    # with firefox at default zoom (cmd+0 -> default zoom)
    play_button = match('imgs/play.png')
    if play_button:
        #bottom_right = [play_button[0] - 61, play_button[1] + 102]
        #top_left = [play_button[0] - 463, play_button[1] - 258]
        mouseclick(play_button[0], play_button[1])
        mouseclick(play_button[0], play_button[1])
        time.sleep(3)
        play_button = match('imgs/play2.png')
        if play_button:
            mouseclick(play_button[0], play_button[1])

    bottom_right = [486, 686]
    top_left = [86, 326]
    # the game has started
    time.sleep(4)
    print 'start'
    # get top left point and bottom right
    diamond_width = (bottom_right[0] - top_left[0]) / (GRID_WIDTH)
    diamond_height = (bottom_right[1] - top_left[1]) / (GRID_HEIGHT)

    b = Bot(
        #[top_left[0] - diamond_width / 2, top_left[1] - diamond_height / 2],
        [top_left[0], top_left[1]],
        GRID_WIDTH, GRID_HEIGHT, diamond_width, diamond_height,
        SENSITIVITY, COUNTER_THRESHOLD)
    while b.running:
        b.next()


if __name__ == '__main__':
    main()
