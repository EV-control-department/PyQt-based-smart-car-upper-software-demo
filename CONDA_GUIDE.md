# Miniconda 虚拟环境配置指南

本指南将介绍如何使用 Miniconda 创建并配置一个专门用于本项目（小车上位机）的 Python 虚拟环境。

## 1. 安装 Miniconda
如果你还没有安装 Miniconda，请访问 [Miniconda 官网](https://docs.anaconda.com/miniconda/) 下载并安装适用于 Windows 的版本。

## 2. 打开终端
在 VS Code 终端中进行操作。

### 2.1 初始化 PowerShell (这部分没有实操过，因为我暂时无法找到一个没有装过conda的电脑来验证，只是根据网上的信息来总结的)
如果你在 Windows 上首选使用 **PowerShell** (VS Code 默认终端)，需要执行以下步骤以启用 conda 脚本运行：

1. **初始化 PowerShell**:
   在终端运行：
   ```powershell
   conda init powershell
   ```
2. **修改执行策略 (权限错误解决)**:
   如果在后续步骤中出现“在此系统上禁止运行脚本”的错误，请运行以下命令：
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. **重启终端**:
   **必须**关闭并重新打开 VS Code 或终端，上述配置才会生效。

## 3. 创建虚拟环境

### 方法 A：手动创建 (推荐初学者)
运行以下命令创建一个名为 `car_env` 的虚拟环境，并指定 Python 版本（建议使用与开发环境一致的 3.12.12）：

```bash
conda create -n car_env python=3.12.12
```

### 方法 B：通过配置文件创建 (一键克隆环境)
如果你已经有了项目提供的 `environment.yml` 文件，可以使用以下命令直接创建完全一致的环境：

```bash
conda env create -f environment.yml
```

> **注**: `environment.yml` 会自动包含 Python 版本、conda 包以及 pip 依赖，是最推荐的复现环境方式。

## 4. 激活虚拟环境
创建完成后，需要激活环境才能使用：

```bash
conda activate car_env
```

激活后，你会发现终端提示符前缀变成了 `(car_env)`。

## 5. 安装依赖库
>注：如果已经使用environment.yml文件创建了环境，那么可以跳过这一步。
在激活的环境下，进入项目根目录，运行以下命令安装本项目确定的版本：

```bash
pip install PySide6==6.10.1 pygame==2.6.1 pygame_gui==0.6.13
```

或者直接使用 `requirements.txt` 文件安装（这是复刻别人的项目的环境的常用的方法）：

```bash
pip install -r requirements.txt
```

## 6. 在 VS Code 中切换环境
1. 在 VS Code 中打开任意 `.py` 文件。
2. 点击右下角的 Python 版本号（或按下 `Ctrl + Shift + P` 输入 `Python: Select Interpreter`）。
3. 在列表中找到并选择带有 `('car_env': conda)` 字样的解释器。

## 7. 常用命令小结
- **列出所有环境**: `conda env list`
- **退出当前环境**: `conda deactivate`
- **删除环境**: `conda remove -n car_env --all`
- **查看已安装包**: `conda list` (或 `pip list`)

---
祝开发顺利！
