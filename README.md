# Customized OpenCV for [`pyppbox`](https://github.com/rathaumons/pyppbox)

##  `pyppbox-opencv` | `opencv-python` | `opencv-contrib-python`

* Updated: **January 19, 2025**
* Requirements: `['numpy>=1.26.4; python_version=="3.11.*"']`
* CUDA & cuDNN are included in the package.
* The supported hardware for **Python 3.11** + **CUDA 12.1**:
  ```
  NVIDIA GPU arch: 60 61 70 75 80 86 89 90
  NVIDIA PTX archs: 60 61 70 75 80 86 89 90
  ```
* OpenCV modules:
  ```
  OpenCV modules:
    To be built:                 alphamat aruco bgsegm bioinspired calib3d ccalib core cudev datasets dnn dnn_objdetect dnn_superres dpm face features2d flann freetype fuzzy gapi hfs highgui img_hash imgcodecs imgproc intensity_transform line_descriptor mcc ml objdetect optflow phase_unwrapping photo plot python3 quality rapid reg rgbd saliency shape signal stereo stitching structured_light superres surface_matching text tracking video videoio videostab wechat_qrcode xfeatures2d ximgproc xobjdetect xphoto
    Disabled:                    cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping world
    Disabled by dependency:      -
    Unavailable:                 cannops cvv hdf java julia matlab ovis python2 sfm ts viz
    Applications:                -
    Documentation:               NO
    Non-free algorithms:         NO
  ```

## My Build Notes (For Linux Only):

* Install and use gcc/g++ 9 to build
* Install required libraries
  ```
  sudo apt-get install libglew-dev \
  libv4l-dev \
  libxvidcore-dev \
  libx264-dev \
  libtiff-dev \
  libtiff5-dev \
  zlib1g-dev \
  libjpeg-dev \
  libpng-dev \
  libavcodec-dev \
  libavformat-dev \
  libavutil-dev \
  libpostproc-dev \
  libswscale-dev \
  libeigen3-dev \
  libtbb-dev \
  libgtk-3-dev \
  libgtk2.0-dev \
  libatlas-base-dev \
  openexr \
  pkg-config
  ```
* Install [CUDA 12.1](https://developer.nvidia.com/cuda-downloads) & [cuDNN 8.9](https://developer.nvidia.com/cudnn-downloads)
* Install Python using [miniconda](https://docs.anaconda.com/miniconda/#quick-command-line-install)
* Create Python 3.11 conda env named `cv2p311`
  ```
  conda update --all
  conda create --name cv2p311 python=3.11
  ```
* Terminal -> ***Activate conda env*** and install the latest `numpy`
  ```
  conda activate cv2p311
  pip install numpy
  ```
* Download and extract sources [opencv](https://github.com/opencv/opencv/tags) & [opencv_contrib](https://github.com/opencv/opencv_contrib/tags)
* Same conda terminal -> Set paths and vars (opencv 4.x.x)
  ```
  export cvbuild="{your path}/cvbuild"
  export cvinstall="{your path}/install"
  export cvsource="{your path}/opencv-4.11.0"
  export cvextmodules="{your path}/opencv_contrib-4.11.0/modules"
  export bt="Release"
  ```
* Same conda terminal -> Set main cmake
  ```
  cmake -S "$cvsource" -B "$cvbuild" -DCMAKE_BUILD_TYPE="$bt" \
  -DOPENCV_EXTRA_MODULES_PATH="$cvextmodules" \
  -DINSTALL_TESTS=OFF -DINSTALL_C_EXAMPLES=OFF -DBUILD_EXAMPLES=OFF \
  -DCMAKE_INSTALL_PREFIX="$cvinstall" \
  -DCMAKE_INSTALL_RPATH=$(python -c "from distutils.sysconfig import get_python_lib; print(str(get_python_lib()) + '/cv2/python-3')") \
  -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
  -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_opencv_world=OFF \
  -DBUILD_opencv_gapi=ON \
  -DBUILD_OPENEXR=ON \
  -DBUILD_PNG=ON \
  -DINSTALL_CREATE_DISTRIB=ON \
  -DBUILD_DOCS=OFF \
  -DBUILD_PERF_TESTS=OFF \
  -DBUILD_TESTS=OFF \
  -DBUILD_opencv_apps=OFF \
  -DOPENCV_VCSVERSION="4.11.0.100+cu121" \
  ```
* Same conda terminal -> Add CUDA 12.1
  ```
  -DWITH_CUDA=ON \
  -DWITH_CUDNN=ON \
  -DWITH_NVCUVID=ON \
  -DCUDA_ARCH_BIN="6.0 6.1 7.0 7.5 8.0 8.6 8.9 9.0" \
  -DCUDA_ARCH_PTX="6.0 6.1 7.0 7.5 8.0 8.6 8.9 9.0" \
  -DWITH_CUBLAS=ON \
  -DCUDA_FAST_MATH=ON \
  -DCUDA_SDK_ROOT_DIR="/usr/local/cuda" \
  -DOPENCV_DNN_CUDA=ON \
  -DWITH_MFX=ON \
  -DWITH_OPENGL=ON \
  ```
* Same conda terminal -> Config CUDA - lite
  ```
  -DBUILD_opencv_cudaarithm=OFF \
  -DBUILD_opencv_cudabgsegm=OFF \
  -DBUILD_opencv_cudacodec=OFF \
  -DBUILD_opencv_cudafeatures2d=OFF \
  -DBUILD_opencv_cudafilters=OFF \
  -DBUILD_opencv_cudaimgproc=OFF \
  -DBUILD_opencv_cudalegacy=OFF \
  -DBUILD_opencv_cudaobjdetect=OFF \
  -DBUILD_opencv_cudaoptflow=OFF \
  -DBUILD_opencv_cudastereo=OFF \
  -DBUILD_opencv_cudawarping=OFF \
  ```
* Same conda terminal -> Config `nonfree` modules (Optional)
  ```
  -DOPENCV_ENABLE_NONFREE=ON -DBUILD_opencv_rgbd=OFF \
  ```
* Same conda terminal -> Config python
  ```
  -DPYTHON3_LIMITED_API=ON \
  -DPYTHON3_EXECUTABLE=$(which python) \
  -DPYTHON3_INCLUDE_DIR=$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
  -DPYTHON3_LIBRARY=$(python -c "from distutils.sysconfig import get_config_var;from os.path import dirname,join ; print(join(dirname(get_config_var('LIBPC')),get_config_var('LDLIBRARY')))") \
  -DPYTHON3_NUMPY_INCLUDE_DIRS=$(python -c "import numpy; print(numpy.get_include())") \
  -DPYTHON3_PACKAGES_PATH=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
  -DBUILD_NEW_PYTHON_SUPPORT=ON \
  -DBUILD_opencv_python2=OFF \
  -DBUILD_opencv_python3=ON \
  -DHAVE_opencv_python3=ON
  ```
* Same conda terminal -> Build cmake
  ```
  numproc=$(nproc)
  cmake --build "$cvbuild" -j $numproc
  ```
* Same conda terminal -> Install
  ```
  cmake --install "$cvbuild"
  ```
* Make ready & create WHL
  - Clone `git clone --single-branch --branch "cp311+cu121-linux" https://github.com/rathaumons/opencv-for-pyppbox.git`
  - Check and see all the libs inside [`cv2/python-3/linux`](cv2/python-3/linux), and copy all those files from `/usr/local/cuda/lib64` and `{your path}/install/lib` to `{conda evn path}/Lib/site-packages/cv2/python-3` -> Same conda terminal:
    ```
    # copy libopencv_*.so.411 to cv2/python-3
    export sp=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
    cp $cvbuild/lib/libopencv_*.so.411 $sp/cv2/python-3
    
    # copy necessary cuda libs to cv2/python-3
    export cupath="/usr/local/cuda-12.1/lib64"
    cp $cupath/libcudnn.so.8 $sp/cv2/python-3
    cp $cupath/libcublas.so.12 $sp/cv2/python-3
    cp $cupath/libcublasLt.so.12 $sp/cv2/python-3
    cp $cupath/libcudnn_cnn_infer.so.8 $sp/cv2/python-3
    cp $cupath/libcudnn_ops_infer.so.8 $sp/cv2/python-3
    cp $cupath/libOpenCL.so.1 $sp/cv2/python-3
    
    # set permissions
    chmod 644 $sp/cv2/python-3/*.so*
    
    # patch the shared libs using patchelf
    sudo apt-get install -y patchelf
    patchelf --set-rpath '$ORIGIN' $sp/cv2/python-3/*.so*
    ```
  - Copy `{your path}/install/share/opencv4/haarcascades/*` to `{conda evn path}/Lib/site-packages/cv2/data`
  - Copy `{your path}/install/share/opencv4/lbpcascades/*` to `{conda evn path}/Lib/site-packages/cv2/data`
  - Copy `{your path}/install/share/opencv4/quality/*` to `{conda evn path}/Lib/site-packages/cv2/data`
  - Copy `{conda evn path}/Lib/site-packages/cv2/*` to [`cv2`](cv2) (Except those already present in [`cv2`](cv2))

  - Same conda terminal -> Create WHL
    ```
    # install pip tools
    pip install setuptools wheel build
    
    # inside the cloned repo opencv-for-pyppbox
    cd opencv-for-pyppbox
    python -m build --wheel --skip-dependency-check --no-isolation
    ```
* Locate and install the newly created wheel under `opencv-for-pyppbox/dist`
* Same conda terminal -> Test your `cv2`
  ```
  import cv2
  cv2.__version__
  print(cv2.getBuildInformation()) 
  ```
* Update conda lib if import error; for example, if you built on a linux which came with gcc/g++ 13 as defaults:
  ```
  conda update --all
  conda install -c conda-forge gcc=13
  ```
