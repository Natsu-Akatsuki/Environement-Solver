# Migration Scripts

After **TEDIOUS**, **REDUNDANT** migration operations from ubuntu 16.04/18.04 to ubuntu20.04. It is necessary to write some scripts to automate the migration work, though some simple code...


<p align="center">
<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20220324205932211.png" alt="image-20220324205932211"  width=20% height=20% />
</p>

## Requirement

```bash
$ pip3 install pathlib easydict
```

## Migration

### C++

- opencv3->opencv4.2 api

### CMakeLists

- obey Policy CMP0048 (i.e. VERSION 2.8.3 -> VERSION 3.16.0)
- C++11 -> C++14 (`CMAKE_CXX_FLAGS`)

### Ros

- strip any leading / character in frame_id (e.g `/camera` -> `camera`)

## Usage

The repositories tested are as follows.

- CMakeLists example

```bash
$ python3 migration.py --cfg=config/CMakeLists.yml
```

- [vins-fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion.git)

```bash
$ git clone https://github.com/HKUST-Aerial-Robotics/VINS-Fusion.git
# modify the parameter in cfg
$ python3 migration.py --cfg=config/vins_fusion.yml
```

<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20220406103824811.png" alt="image-20220406103824811" style="zoom: 80%;" />

- [livox_horizon_loam](https://github.com/Livox-SDK/livox_horizon_loam.git)

```bash
$ git clone https://github.com/Livox-SDK/livox_horizon_loam.git
# modify the parameter in cfg
$ python3 migration.py --cfg=config/horizon_slam.yml
```
- [OpenPCDet]()

```bash
$ git clone https://github.com/open-mmlab/OpenPCDet
# modify the parameter in cfg
$ python3 migration.py --cfg=config/openpcdet.yml
```

## Reference

- [pysed](https://github.com/mahmoudadel2/pysed)
