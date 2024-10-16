import cv2  # 导入 OpenCV 库
cap = cv2.VideoCapture("1.mp4")  # 打开视频文件

import numpy as np  # 导入 NumPy 库
import time  # 导入时间库
import tkinter as tk  # 导入 Tkinter 库，用于创建 GUI
from tkinter import scrolledtext  # 从 Tkinter 导入滚动文本框

# 定义用于 ASCII 艺术的字符集
chars = ['#', 'S', '0', 'B', '+', '=', 'O', 'o', '8']

display_width = 450  # 设置显示宽度
display_height = 130  # 设置显示高度

def frame_to_ascii(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将帧转换为灰度图像
    small_frame = cv2.resize(gray, (display_width, display_height))  # 将图像调整为指定的显示尺寸
    # 将每个像素值映射到 ASCII 字符
    ascii_frame = ''.join(chars[min(pixel // (256 // len(chars)), len(chars) - 1)] for pixel in small_frame.flatten())
    # 将 ASCII 字符串按行分割
    return '\n'.join([ascii_frame[i:i + display_width] for i in range(0, len(ascii_frame), display_width)])

# 创建主窗口
root = tk.Tk()
root.title("少帅下飞机")  # 设置窗口标题
root.configure(bg='white')  # 设置背景颜色

# 创建可滚动文本框以显示 ASCII 艺术
text_area = scrolledtext.ScrolledText(root, width=display_width, height=display_height, font=("Courier", 4), bg='white', fg='black')
text_area.pack()  # 添加文本框到窗口中

def update_display():
    ret, frame = cap.read()  # 读取视频帧
    if not ret:  # 如果没有读取到帧（视频结束）
        cap.release()  # 释放视频捕捉对象
        return  # 结束函数
    ascii_art = frame_to_ascii(frame)  # 将帧转换为 ASCII 艺术
    text_area.delete(1.0, tk.END)  # 清空文本框
    text_area.insert(tk.END, ascii_art)  # 将 ASCII 艺术插入文本框
    root.after(int(1000 / 30.70), update_display)  # 每隔一定时间更新显示（30.70 FPS）

update_display()  # 开始更新显示
root.mainloop()  # 运行 Tkinter 事件循环
