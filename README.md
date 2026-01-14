# PyQt-based-smart-car-upper-software-demo
为 2026 年 E 唯协会寒假第二次培训准备的智能小车上位机示例（基于 PySide6/PyQt）。

> **快速开始**: 强烈建议使用 Miniconda 进行环境管理，详见 [环境配置指南 (CONDA_GUIDE.md)](CONDA_GUIDE.md)。

**简介**
- **目的**: 演示如何使用 Python 和 PySide6 实现一个简单的小车上位机（GUI），包括遥控、状态显示与基础 UI 结构。
- **适用人群**: 对嵌入式小车、机器人上位机或 PySide6 GUI 开发感兴趣的初学者与培训学员。

**主要功能**
- **实时遥控显示**: 提供示例界面用于发送控制命令（方向、速度等）。
- **UI 原型**: 包含基于 Qt Designer 的 UI 文件和对应的 Python 绑定代码示例。
- **示例脚本**: 提供带摇杆支持的演示脚本与普通演示脚本以便对比学习。

**依赖环境**
- Python 3.8 及以上
- PySide6

推荐安装命令：

```bash
python -m pip install --upgrade pip
pip install PySide6
```

**运行示例**
- 运行主演示（GUI）:

```bash
python demo_Pyside6.py
```

- 运行带摇杆的演示（如果有外部摇杆并希望测试）:

```bash
python demo_Pyside6_joystick.py
```

**文件说明**
- **[demo_Pyside6.py](demo_Pyside6.py)**: 主演示脚本，演示如何载入 UI 并运行主界面。
- **[demo_Pyside6_joystick.py](demo_Pyside6_joystick.py)**: 带摇杆输入的演示脚本示例。
- **[demo_ui.py](demo_ui.py)**: UI 绑定或辅助脚本（视实现而定）。
- **[demo1.ui](demo1.ui)**: 使用 Qt Designer 创建的界面文件，可用 Qt Designer 编辑或通过工具转换为 Python。
- **[LICENSE](LICENSE)**: 仓库许可文件。

如果需要将 `.ui` 文件转换为 Python（使用 PySide6）:

```bash
pyside6-uic demo1.ui -o demo_ui.py
```

**开发与二次开发建议**
- 首先在虚拟环境中安装依赖以避免污染系统环境。
- 在 `demo1.ui` 中修改布局后，可重新转换为 Python 或直接在运行时载入 `.ui` 文件。
- 若要与真实小车通信，请在 GUI 中添加串口/UDP/TCP 的通信模块，并把控制命令映射到按钮或摇杆事件上。

**许可 & 贡献**
- 本项目包含 `LICENSE` 文件，请参阅以了解使用与分发限制。
- 欢迎提交 Issue 或 Pull Request，或在培训中根据此示例进行扩展与教学。