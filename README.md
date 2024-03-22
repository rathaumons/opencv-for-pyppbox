# Customized OpenCV for [`pyppbox`](https://github.com/rathaumons/pyppbox)

##  `pyppbox-opencv` | `opencv-contrib-python` | `cv2`

* Updated: **March 22, 2024**
* Requirements: `['numpy>=1.26.4; python_version=="3.12.*"']`
* CUDA & cuDNN are included in the package.
* The supported hardware for **Python 3.12** + **CUDA 12.1**:
  ```
  NVIDIA GPU arch: 60 61 70 75 80 86 89
  NVIDIA PTX archs: 60 61 70 75 80 86 89
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

## My Build Notes:

* Install [CUDA 12.1](https://developer.nvidia.com/cuda-downloads) & [cuDNN 8.9](https://developer.nvidia.com/cudnn-downloads)
* Install [Python 3.12](https://www.python.org/downloads/windows/)
* Terminal `cmd` -> Install `numpy==1.26.4`
  ```
  pip install numpy==1.26.4
  ```
* Download sources [opencv](https://github.com/opencv/opencv/tags) & [opencv_contrib](https://github.com/opencv/opencv_contrib/tags)
* Terminal `cmd` -> Set base paths and vars (opencv 4.x.x)
  ```
  set "cvsource={Source path}\opencv-4.x.x"
  set "cvextmodules={Source path}\opencv_contrib-4.x.x\modules"
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
* Terminal `cmd` -> Add cuda 12.1
  ```
  -DWITH_CUDA=ON ^
  -DWITH_NVCUVID=ON ^
  -DCUDA_ARCH_BIN="6.0 6.1 7.0 7.5 8.0 8.6 8.9" ^
  -DCUDA_ARCH_PTX="6.0 6.1 7.0 7.5 8.0 8.6 8.9" ^
  -DWITH_CUBLAS=ON ^
  -DCUDA_FAST_MATH=ON ^
  -DCUDA_SDK_ROOT_DIR="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.1" ^
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
* Terminal `cmd` -> Config `nonfree` modules (Optional)
  ```
  -DOPENCV_ENABLE_NONFREE=ON -DBUILD_opencv_rgbd=OFF ^
  ```
* Terminal `cmd` -> Config python (3.12)
  ```
  -DPYTHON3_LIMITED_API=ON ^
  -DPYTHON3_EXECUTABLE="C:/dev/exc/python/p312/python.exe" ^
  -DPYTHON3_INCLUDE_DIR="C:/dev/exc/python/p312/include" ^
  -DPYTHON3_LIBRARY="C:/dev/exc/python/p312/libs/python312.lib" ^
  -DPYTHON3_NUMPY_INCLUDE_DIRS="C:/dev/exc/python/p312/lib/site-packages/numpy/core/include" ^
  -DPYTHON3_PACKAGES_PATH="C:/dev/exc/python/p312/Lib/site-packages" ^
  -DBUILD_opencv_python3=ON
  ```
* Terminal `cmd` -> Build cmake
  ```
  cmake --build %cvbuild% --target INSTALL --config Release
  ```
* Make ready & create WHL
  - Copy `{Python path}/Lib/site-packages/cv2/*` to [`cv2`](cv2) (Execpt those already present in [`cv2`](cv2))
  - Copy `cublas64_12.dll`, `cublasLt64_12.dll`, and `cudnn64_8.dll` from `{CUDA toolkit path}/CUDA/v12.1/bin` to [`cv2/cuda_bin`](cv2/cuda_bin) 
  - Copy `cvbuild/install/x64/vc16/bin/*` to [`cv2/python-3`](cv2/python-3)
  - Create WHL -> Run [`create_whl.cmd`](create_whl.cmd)
* Locate and install the newly created wheel
* Test your `cv2`
  ```
  import cv2
  cv2.__version__
  print(cv2.getBuildInformation()) 
  ```
