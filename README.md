# OpenCV - Customized for [`pyppbox`](https://github.com/rathaumons/pyppbox)

##  `pyppbox-opencv` | `opencv-contrib-python` | `cv2`

* Updated: **May 12, 2023**
* Requires `numpy>=1.24.3`
* Uses the default path of CUDA & CUDNN `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vxx.x`. 
* If your CUDA & CUDNN were installed in a different location, simply modify the `YOUR_PYTHON\Lib\site-packages\cv2\config.py` accordingly.
* The supported hardware for Python 3.9/3.10 + **CUDA 11.8+**:
  ```
  NVIDIA GPU arch: 60 61 70 75 80 86 89
  NVIDIA PTX archs: 60 61 70 75 80 86 89
  ```
* The supported hardware for Python 3.9/3.10 + **CUDA 11.7**:
  ```
  NVIDIA GPU arch: 60 61 70 75 80 86
  NVIDIA PTX archs: 60 61 70 75 80 86
  ```
* OpenCV modules:
  ```
  OpenCV modules:
    To be built:                 aruco barcode bgsegm bioinspired calib3d ccalib core cudev datasets dnn dnn_objdetect dnn_superres dpm face features2d flann fuzzy gapi hfs highgui img_hash imgcodecs imgproc intensity_transform line_descriptor mcc ml objdetect optflow phase_unwrapping photo plot python3 quality rapid reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking video videoio videostab wechat_qrcode xfeatures2d ximgproc xobjdetect xphoto
    Disabled:                    cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping world
    Disabled by dependency:      -
    Unavailable:                 alphamat cvv freetype hdf java julia matlab ovis python2 sfm ts viz
    Applications:                -
    Documentation:               NO
    Non-free algorithms:         NO
  ```

## The [prebuilt WHLs are available here](https://github.com/rathaumons/pyppbox-custpkg)!

## Manual build note:

* Install [cuda](https://developer.nvidia.com/cuda-downloads) & [cudnn](https://developer.nvidia.com/rdp/cudnn-download)
* Install [python](https://www.python.org/downloads/windows/)
* Terminal `cmd` -> Install `numpy`
  ```
  pip install numpy>=1.24.3
  ```
* Download sources [opencv](https://github.com/opencv/opencv/tags) & [opencv_contrib](https://github.com/opencv/opencv_contrib/tags)
* Terminal `cmd` -> Set base vars (opencv 4.7.0)
  ```
  set "cvsource=D:\DEV\opencv\build\opencv-4.7.0"
  set "cvextmodules=D:\DEV\opencv\build\opencv_contrib-4.7.0\modules"
  set "cvbuild=%cvsource%\cvbuild"
  set "bt=Release"
  set "gt=Visual Studio 16 2019"
  ```
* Terminal `cmd` -> Set main cmake
  ```
  cmake -S "%cvsource%/" -B "%cvbuild%/" -G "%gt%" -A x64 -DCMAKE_BUILD_TYPE=%bt% ^
  -DOPENCV_EXTRA_MODULES_PATH="%cvextmodules%/" ^
  -DINSTALL_TESTS=OFF -DINSTALL_C_EXAMPLES=OFF -DBUILD_EXAMPLES=OFF ^
  -DBUILD_SHARED_LIBS=ON ^
  -DBUILD_opencv_world=OFF ^
  -DBUILD_opencv_gapi=ON ^
  -DBUILD_OPENEXR=ON ^
  -DBUILD_PNG=ON ^
  -DINSTALL_CREATE_DISTRIB=ON ^
  -DBUILD_DOCS=OFF ^
  -DBUILD_PERF_TESTS=OFF ^
  -DBUILD_TESTS=OFF ^
  -DBUILD_opencv_apps=OFF ^
  -DBUILD_opencv_python2=OFF ^
  ```
* Terminal `cmd` -> Add cuda 11.8
  ```
  -DWITH_CUDA=ON ^
  -DWITH_NVCUVID=ON ^
  -DCUDA_ARCH_BIN="6.0 6.1 7.0 7.5 8.0 8.6 8.9" ^
  -DCUDA_ARCH_PTX="6.0 6.1 7.0 7.5 8.0 8.6 8.9" ^
  -DWITH_CUBLAS=ON ^
  -DCUDA_FAST_MATH=ON ^
  -DCUDA_SDK_ROOT_DIR="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8" ^
  -DOPENCV_DNN_CUDA=ON ^
  -DWITH_MFX=ON ^
  -DWITH_OPENGL=ON ^
  ```
* Terminal `cmd` -> Config cuda - lite
  ```
  -DBUILD_opencv_cudaarithm=OFF ^
  -DBUILD_opencv_cudabgsegm=OFF ^
  -DBUILD_opencv_cudacodec=OFF ^
  -DBUILD_opencv_cudafeatures2d=OFF ^
  -DBUILD_opencv_cudafilters=OFF ^
  -DBUILD_opencv_cudaimgproc=OFF ^
  -DBUILD_opencv_cudalegacy=OFF ^
  -DBUILD_opencv_cudaobjdetect=OFF ^
  -DBUILD_opencv_cudaoptflow=OFF ^
  -DBUILD_opencv_cudastereo=OFF ^
  -DBUILD_opencv_cudawarping=OFF ^
  ```
* Termianl `cmd` -> Config `nonfree` modules (Optional)
  ```
  -DOPENCV_ENABLE_NONFREE=ON -DBUILD_opencv_rgbd=OFF ^
  ```
* Terminal `cmd` -> Config python (3.10)
  ```
  -DPYTHON3_LIMITED_API=ON ^
  -DPYTHON3_EXECUTABLE="C:/dev/exc/python/p310/python.exe" ^
  -DPYTHON3_INCLUDE_DIR="C:/dev/exc/python/p310/include" ^
  -DPYTHON3_LIBRARY="C:/dev/exc/python/p310/libs/python310.lib" ^
  -DPYTHON3_NUMPY_INCLUDE_DIRS="C:/dev/exc/python/p310/lib/site-packages/numpy/core/include" ^
  -DPYTHON3_PACKAGES_PATH="C:/dev/exc/python/p310/Lib/site-packages" ^
  -DBUILD_opencv_python3=ON
  ```
* Termianl `cmd` -> Build cmake
  ```
  cmake --build %cvbuild% --target INSTALL --config Release
  ```
* Make ready & create WHL
  - Copy `.../cvbuild/install/x64/vc16/bin/*` to [`cv2`](cv2)
  - Copy `.../cvbuild/lib/python3/Release/cv2.pyd` to [`cv2`](cv2)
  - Verify all files in [`cv2`](cv2) with [`pyd_dll`](cv2/pyd_dll)
  - Verify the cuda toolkit path in [`config.py`](cv2/config.py)
  - Create WHL -> Run [`creat_whl.cmd`](creat_whl.cmd)
* Test your `cv2`
  ```
  import cv2
  cv2.__version__
  print(cv2.getBuildInformation()) 
  ```
