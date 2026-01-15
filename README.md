# Smart Car Upper Software Demo (PySide6)

为 2026 年 E 唯协会寒假第二次培训准备的智能小车上位机示例工程。基于 Python 3.12 + PySide6 开发，演示了基础的 GUI 交互与游戏手柄控制逻辑。

> **推荐**: 详见 [环境配置指南 (CONDA_GUIDE.md)](CONDA_GUIDE.md) 了解如何从零配置开发环境。

> **离线部署**: 如果需要在**无网络环境**的电脑上运行本项目，请参考下方的 [环境离线迁移](#环境离线迁移) 章节。

## 简介
本项目旨在帮助嵌入式或机器人方向的初学者快速上手编写上位机软件：
- **主要技术栈**: Python 3.12, PySide6 (Qt for Python), Pygame (手柄输入).
- **核心功能**:
    - **基础 UI 框架**：使用 Qt Designer 设计界面，分离界面与逻辑。
    - **控件交互**：通过滑块 (Slider) 模拟小车速度与方向控制。
    - **硬件输入**：通过 Pygame 接入 USB/蓝牙游戏手柄，实时控制界面控件。

## 目录结构
```text
.
├── demo_Pyside6.py          # [基础] 主程序，仅使用鼠标/触摸控制
├── demo_Pyside6_joystick.py # [进阶] 带手柄支持的主程序 (需连接手柄)
├── demo_ui.py               # [生成] 由 demo1.ui 编译生成的 Python UI 代码
├── demo1.ui                 # [源码] Qt Designer 界面设计文件
├── requirements.txt         # [依赖] pip 依赖列表
├── environment.yml          # [依赖] Conda 环境配置文件
├── CONDA_GUIDE.md           # [文档] 详细的环境配置教程
└── README.md                # [文档] 项目说明书
```

## 环境配置

### 方式一：使用 Conda (推荐)
如果你安装了 Anaconda 或 Miniconda，可以一键创建环境：

```bash
# 1. 创建名为 car_env 的环境
conda env create -f environment.yml

# 2. 激活环境
conda activate car_env
```

### 方式二：使用 pip
如果你使用标准的 Python 环境 (建议 Python 3.10 及以上，开发环境为 3.12)：

```bash
# 1. (可选) 创建并激活虚拟环境
python -m venv venv
# Windows 激活:
.\venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt
```

## 运行演示

### 1. 基础演示
启动基础界面，使用鼠标拖动“速度”和“方向”滑块，观察上方数值变化。

```bash
python demo_Pyside6.py
```

### 2. 手柄控制演示
**前提**: 请先将游戏手柄（Xbox/PS/通用手柄）连接至电脑。
启动后，脚本会自动检测手柄。推动左摇杆控制**方向**，推动左摇杆上下（或右摇杆，视手柄映射）控制**速度**。界面上的滑块会跟随摇杆移动。

```bash
python demo_Pyside6_joystick.py
```
> *若未检测到手柄，程序会输出提示并作为普通 GUI 运行。*

## 离线环境使用

当网络连接不稳定（如 pip/conda 无法连接服务器）或需要快速在机器上配置时，可以使用打包好的**离线环境包 (`.zip`)**。压缩包可能从QQ群获取


1.  将 `car_env_packed.zip` 解压到一个**路径不含中文**的文件夹（建议解压目录名简短，例如 `E:\env`）。
2.  进入解压后的目录，运行激活脚本：
    双击 `activate.bat` 脚本。
    *(在命令行窗口中，终端前缀出现 `(car_env)` 即代表环境已激活)*
3.  此时环境已准备就绪（包含所有 Python 库），可直接运行项目：
    ```bash
    python demo_Pyside6_joystick.py
    ```

## 开发说明

### 修改界面
1. 使用 **Qt Designer** 打开 `demo1.ui` 进行可视化编辑。
2. 保存后，使用以下命令重新生成 Python 代码：
   ```bash
   pyside6-uic demo1.ui -o demo_ui.py
   ```
   *注意：不要直接修改 `demo_ui.py`，因为下次编译会覆盖它。请在 `demo_Pyside6.py` 的子类中编写逻辑。*

## 许可 & 贡献
- 开源协议详见 LICENSE。
- 欢迎提交 Issue 或 Pull Request，或在培训中根据此示例进行扩展与教学。