# Migration Scripts

After **TEDIOUS**, **REDUNDANT** migration operations from ubuntu 16.04/18.04 to ubuntu20.04. It is necessary to write some scripts to automate the migration work, though some simple code...


<p align="center">
<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20220324205932211.png" alt="image-20220324205932211"  width=20% height=20% />
</p>

## Migration

### C++

- opencv3->opencv4.2 api

### CMakeLists

- C++11->C++14 (`CMAKE_CXX_FLAGS`)

## Usage

modify the `src_dir` variable in `migration.py`  and execute. The repositories tested are as follows.

- [vins-fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion.git)

## Reference

- [pysed](https://github.com/mahmoudadel2/pysed)

