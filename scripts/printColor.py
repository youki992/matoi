import ctypes

# 【强调】 有蓝色背景色
# 7 = >默认值
# 0 = >黑色
# 1 =蓝
# 2 = >绿色
# 3 = >水
# 4 = >红色
# 5 = >紫色-purple
# 6 = >黄-yellow
# 7 = >白色-white
# 8 = >灰色-grey
# 9 = >淡蓝色-Light blue  【与 蓝色 无异】
# 10 = >【强调】灰-Light grey
# 11 = >【强调】蓝-Light blue
# 12 = >【强调】绿-Light green
# 13 = >【强调】水-Light water
# 14 = >【强调】红-Light red
# 15 = >白-white
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLACK = 0x0
FOREGROUND_BLUE = 0x01  # text color contains blue.
FOREGROUND_GREEN = 0x02  # text color contains green.
FOREGROUND_WATER = 0x03  # text color contains water.
FOREGROUND_RED = 0x04  # text color contains red.
FOREGROUND_PURPLE = 0x05  # text color contains purple.
FOREGROUND_YELLOW = 0x06  # text color contains yellow.
FOREGROUND_WHITE = 0x07  # text color contains white.
FOREGROUND_GREY = 0x08  # text color contains grey.
FOREGROUND_LIGHTGREY = 0x10  # text color contains light grey.
FOREGROUND_LIGHTBLUE = 0x11  # text color contains light blue.
FOREGROUND_LIGHTGREEN = 0x12  # text color contains light green.
FOREGROUND_LIGHTWATER = 0x13  # text color contains light water.
FOREGROUND_LIGHTRED = 0x14  # text color contains light red.
FOREGROUND_WHITE = 0x15  # text color contains white.

BACKGROUND_BLUE = 0x10  # background color contains blue.
BACKGROUND_GREEN = 0x20  # background color contains green.
BACKGROUND_RED = 0x40  # background color contains red.
BACKGROUND_INTENSITY = 0x80  # background color is intensified.
class Colors:
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    def set_cmd_color(self, color, handle=std_out_handle):
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool

    def reset_color(self):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

    def print_blue_text(self, print_text):
        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_GREY)
        print (print_text)
        self.reset_color()

    def print_green_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_GREY)
        print (print_text)
        self.reset_color()

    def print_water_text(self, print_text):
        self.set_cmd_color(FOREGROUND_WATER | FOREGROUND_GREY)
        print (print_text)
        self.reset_color()

    def print_red_text(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_purple_text(self, print_text):
        self.set_cmd_color(FOREGROUND_PURPLE | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_yellow_text(self, print_text):
        self.set_cmd_color(FOREGROUND_YELLOW | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_white_text(self, print_text):
        self.set_cmd_color(FOREGROUND_WHITE | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_grey_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREY | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_lightgrey_text(self, print_text):
        self.set_cmd_color(FOREGROUND_LIGHTGREY | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_lightblue_text(self, print_text):
        self.set_cmd_color(FOREGROUND_LIGHTBLUE | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_lightgreen_text(self, print_text):
        self.set_cmd_color(FOREGROUND_LIGHTGREEN | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_lightwater_text(self, print_text):
        self.set_cmd_color(FOREGROUND_LIGHTWATER | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_lightred_text(self, print_text):
        self.set_cmd_color(FOREGROUND_LIGHTRED | FOREGROUND_GREY)
        print(print_text)
        self.reset_color()

    def print_white_text(self, print_text):
        self.set_cmd_color(FOREGROUND_WHITE | FOREGROUND_GREY)
        print (print_text)
        self.reset_color()

    def print_red_text_with_blue_bg(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREY | BACKGROUND_BLUE | BACKGROUND_INTENSITY)
        print (print_text)
        self.reset_color()