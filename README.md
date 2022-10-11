# Environment Solver

<div align="center">

[English](README_en.md) | 简体中文

</div>

## 简介

在调用别人的仓库时，往往可能因环境依赖问题，而出现接口冲突的情况。本仓库主要存放一些实现`API`替换的脚本，以避免在高版本环境下对低版本代码迁移时（e.g. `kinetic`/`melodic`->`noetic`）所涉及的重复替换工作。

## 依赖

```bash
$ pip3 install pathlib easydict
```

## 功能

### C++

- 迁移OpenCV API

|           OpenCV 3            |           OpenCV 4.2           |
| :---------------------------: | :----------------------------: |
|         `CV_RGB2GRAY`         |      `cv::COLOR_RGB2GRAY`      |
|         `CV_GRAY2RGB`         |      `cv::COLOR_GRAY2RGB`      |
|         `CV_BGR2GRAY`         |      `cv::COLOR_BGR2GRAY`      |
|         `CV_GRAY2BGR`         |      `cv::COLOR_GRAY2BGR`      |
|   `CV_FONT_HERSHEY_SIMPLEX`   |   `cv::FONT_HERSHEY_SIMPLEX`   |
|   `CV_LOAD_IMAGE_GRAYSCALE`   |     `cv::IMREAD_GRAYSCALE`     |
|          `CV_MINMAX`          |       `cv::NORM_MINMAX`        |
|            `CV_AA`            |         `cv::LINE_AA`          |
|  `CV_CALIB_CB_FILTER_QUADS`   |  `cv::CALIB_CB_FILTER_QUADS`   |
| `CV_CALIB_CB_ADAPTIVE_THRESH` | `cv::CALIB_CB_ADAPTIVE_THRESH` |
| `CV_CALIB_CB_NORMALIZE_IMAGE` | `cv::CALIB_CB_NORMALIZE_IMAGE` |
|   `CV_CALIB_CB_FAST_CHECK`    |   `cv::CALIB_CB_FAST_CHECK`    |
|   `CV_CHAIN_APPROX_SIMPLE`    |   `cv::CHAIN_APPROX_SIMPLE`    |
|       `CV_TERMCRIT_EPS`       |    `cv::TermCriteria::EPS`     |
|      `CV_TERMCRIT_ITER`       |  `cv::TermCriteria::MAX_ITER`  |
|  `CV_CALIB_CB_FILTER_QUADS`   |  `cv::CALIB_CB_FILTER_QUADS`   |
|        `CV_RETR_CCOMP`        |        `cv::RETR_CCOMP`        |
|       `CV_SHAPE_CROSS`        |       `cv::MORPH_CROSS`        |
|        `CV_SHAPE_RECT`        |        `cv::MORPH_RECT`        |
| `CV_ADAPTIVE_THRESH_MEAN_C `  |  `cv::ADAPTIVE_THRESH_MEAN_C`  |

- 头文件

|              —              |      原       |        修正后        |
| :-------------------------: | :-----------: | :------------------: |
| `OpenCV 3` ->  `OpenCV 4.2` | `opencv/cv.h` | `opencv2/opencv.hpp` |

### CMakeLists

- 遵循`Policy CMP0048`，指定使用更高级的`CMake`版本（i.e. `VERSION 2.8.3` -> `VERSION 3.16.0`）
- 使用更高级的C++标准，`C++11` -> `C++14`（ubuntu20.04下apt安装的pcl库，依赖的C++标准为`C++14`）

### ROS

- 对于`melodic`到`noetic`的迁移需移除`frame_id`前面的前导符（e.g `/camera` -> `camera`）
- 缺乏依赖时，若是`ROS`第三方库，则最高效的方法是使用`rosdep`来安装缺失的依赖（在`rosdep`可用的情况下），否则再具体问题具体分析

## 参考用例

需根据仓库实际的路径，修改csv文件`Search DIR`字段的内容

- CMakeLists

```bash
$ python3 migration.py -c cfg/CMakeLists.csv
```

- [vins-fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion.git)

```bash
$ git clone https://github.com/HKUST-Aerial-Robotics/VINS-Fusion.git
# 需根据仓库实际的路径，修改csv文件Search DIR字段的内容
$ python3 migration.py -c cfg/CMakeLists.csv cofig/vins_fusion.csv
```

- [livox_horizon_loam](https://github.com/Livox-SDK/livox_horizon_loam.git)

```bash
$ git clone https://github.com/Livox-SDK/livox_horizon_loam.git
$ python3 migration.py -c cfg/CMakeLists.csv cfg/livox_horizon_slam.csv
```
## 待办事项

- [ ] 整理`Pytorch`算子的`API`

## 参考资料

- [pysed](https://github.com/mahmoudadel2/pysed)