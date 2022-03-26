# Migration Scripts

After **TEDIOUS**, **REDUNDANT** migration operations from ubuntu 16.04/18.04 to ubuntu20.04. It is necessary to write some scripts to automate the migration work, though some simple code...


<p align="center">
<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20220324205932211.png" alt="image-20220324205932211"  width=20% height=20% />
</p>

## Requirement

```bash
$ pip3 install pathlib
```

## Migration

### C++

- opencv3->opencv4.2 api

### CMakeLists

- obeyPolicy CMP0048 (i.e. VERSION 2.8.3 -> VERSION 3.16.0)
- C++11 -> C++14 (`CMAKE_CXX_FLAGS`)

### Ros

- strip any leading / character in frame_id (e.g `/camera` -> `camera`)

## Usage

The repositories tested are as follows.

- [vins-fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion.git)

```bash
$ git clone https://github.com/HKUST-Aerial-Robotics/VINS-Fusion.git
$ migration.py --src=~/VINS-Fusion --reg=replace/common/CMakeLists.replace
$ migration.py --src=~/VINS-Fusion --reg=replace/common/opencv.replace
```

- [livox_horizon_loam](https://github.com/Livox-SDK/livox_horizon_loam.git)

```bash
$ git clone https://github.com/Livox-SDK/livox_horizon_loam.git
$ migration.py --src=~/livox_horizon_loam --reg=replace/example/horizon_slam.replace
$ migration.py --src=~/livox_horizon_loam --reg=replace/common/CMakeLists.replace
```
- [kaho slam](https://github.com/kahowang/sensor-fusion-for-localization-and-mapping.git)

```bash
$ git clone https://github.com/kahowang/sensor-fusion-for-localization-and-mapping.git
$ migration.py --src=~/sensor-fusion-for-localization-and-mapping --reg=replace/example/kaho_slam.replace
```

## Reference

- [pysed](https://github.com/mahmoudadel2/pysed)
