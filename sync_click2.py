import sys
import pyautogui
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QListWidget, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt
import threading
import keyboard  # 按键检测库

class ClickAreaSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.click_positions = []  # 存储点击位置
        self.running = False  # 控制点击线程

    def initUI(self):
        self.setWindowTitle("同步点击工具")
        self.setGeometry(100, 100, 400, 300)

        # 创建按钮和列表
        self.add_position_btn = QPushButton("添加点击区域")
        self.start_click_btn = QPushButton("开始点击")
        self.clear_positions_btn = QPushButton("清空所有区域")
        self.positions_list = QListWidget()
        self.instructions = QLabel(
            "操作说明:\n"
            "1. 点击 '添加点击区域' 后，在屏幕上选择一个位置（鼠标停留后按 'Ctrl' 确认）。\n"
            "2. 添加完成后，点击 '开始点击'，每个区域仅点击一次。\n"
            "3. 按 'Esc' 键可随时终止操作。"
        )
        self.instructions.setWordWrap(True)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.instructions)
        layout.addWidget(self.positions_list)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.add_position_btn)
        btn_layout.addWidget(self.clear_positions_btn)
        btn_layout.addWidget(self.start_click_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # 信号和槽
        self.add_position_btn.clicked.connect(self.add_click_position)
        self.clear_positions_btn.clicked.connect(self.clear_positions)
        self.start_click_btn.clicked.connect(self.start_click)

    def add_click_position(self):
        # 提示用户选择位置
        QMessageBox.information(self, "选择位置", "将鼠标移动到目标位置并按 'Ctrl' 确认。")
        position = self.get_mouse_position()
        if position:
            self.click_positions.append(position)
            self.positions_list.addItem(f"位置: {position}")

    def clear_positions(self):
        self.click_positions.clear()
        self.positions_list.clear()

    def start_click(self):
        if not self.click_positions:
            QMessageBox.warning(self, "警告", "请先添加至少一个点击区域。")
            return

        QMessageBox.information(self, "提示", "开始点击，每个区域将只点击一次。按 'Esc' 可随时终止。")
        threading.Thread(target=self.click_once, daemon=True).start()

    def click_once(self):
        try:
            while self.click_positions:
                # 遍历点击区域
                for position in self.click_positions[:]:
                    if keyboard.is_pressed("esc"):  # 检测 'Esc' 停止点击
                        self.click_positions.clear()
                        break
                    pyautogui.click(*position)
                    self.click_positions.remove(position)  # 点击完成后移除区域
                    self.positions_list.clear()
                    for pos in self.click_positions:
                        self.positions_list.addItem(f"位置: {pos}")
        except Exception as e:
            print("点击过程被中断:", e)

    def get_mouse_position(self):
        """
        获取鼠标点击位置。用户需按下 Ctrl 键确认位置。
        """
        while True:
            x, y = pyautogui.position()
            if keyboard.is_pressed("ctrl"):  # 按下 'Ctrl' 键确认位置
                return x, y

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClickAreaSelector()
    window.show()
    sys.exit(app.exec_())
