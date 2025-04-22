# sync-click-app(软件exe版本直接在Releases中下载)
windows桌面级同步点击器（轻量级应用），支持多位置同步点击，本地打包exe

# 同步点击工具 - SyncClicker

## **简介**
一款基于 PyQt5 和 PyAutoGUI 的桌面工具，用于快速录制屏幕点击位置并批量执行同步点击操作。支持快捷键中断和动态位置管理。

## **功能特性**
- 📌 **位置录制**：通过 `Ctrl` 键快速捕获鼠标当前位置。
- 🖱️ **批量点击**：一键执行所有录制位置的点击操作。
- 🚨 **中断保护**：按下 `Esc` 键可随时终止点击过程。
- 🧹 **动态管理**：支持清空已录制的位置列表。

## **快速开始**
### 依赖安装
```bash
#安装依赖
pip install PyQt5 pyautogui keyboard
#本地py环境运行测试
python sync_clicker.py
#打包程序
pyinstaller --onefile --windowed --icon=click.ico sync_click2.py
```
## 打包后软件使用说明​​
(软件exe直接下载见Releases)
### 添加点击位置​​：
点击 添加点击区域 按钮。
移动鼠标到目标位置，按下 Ctrl 键保存坐标。
### ​​执行点击​​：
点击 开始点击，程序将按顺序点击所有已保存位置。  
按下 Esc 可立即停止。
### ​​清空记录​​：
点击 清空所有区域 以重置位置列表。
