# -*- coding: utf-8 -*-
# @Time    : 2021-01-23 22:31
# @Author  : XU
# @File    : settings.py
# @Software: PyCharm


class Settings:

    def __init__(self):
        """初始化游戏的静态值"""
        self.game_title = "Alien Invasion"
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allow = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏加速偏移量
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """初始化随着游戏进程而变化的值"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)

