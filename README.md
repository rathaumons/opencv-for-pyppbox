# Customized OpenCV for [`pyppbox`](https://github.com/rathaumons/pyppbox)

##  `pyppbox-opencv` | `opencv-python` | `opencv-contrib-python`

* Updated: **January 11, 2025**
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
    To be built:                 aruco bgsegm bioinspired calib3d ccalib core cudev datasets dnn dnn_objdetect dnn_superres dpm face features2d flann fuzzy gapi hfs highgui img_hash imgcodecs imgproc intensity_transform line_descriptor mcc ml objdetect optflow phase_unwrapping photo plot python3 quality rapid reg rgbd saliency shape signal stereo stitching structured_light superres surface_matching text tracking video videoio videostab wechat_qrcode xfeatures2d ximgproc xobjdetect xphoto
    Disabled:                    cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping world
    Disabled by dependency:      -
    Unavailable:                 alphamat cannops cvv freetype hdf java julia matlab ovis python2 sfm ts viz
    Applications:                -
    Documentation:               NO
    Non-free algorithms:         NO
  ```

## My Build Notes (For Windows Only):

* Install [CUDA 12.1](https://developer.nvidia.com/cuda-downloads) & [cuDNN 8.9](https://developer.nvidia.com/cudnn-downloads)
* Install [Python 3.11](https://www.python.org/downloads/windows/)
* Terminal `cmd` -> Install the latest `numpy`
  ```
  pip install numpy
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
  -DOPENCV_VCSVERSION="4.11.0.100+cu121" ^
  ```
* Terminal `cmd` -> Add CUDA 12.1
  ```
  -DWITH_CUDA=ON ^
  -DWITH_NVCUVID=ON ^
  -DCUDA_ARCH_BIN="6.0 6.1 7.0 7.5 8.0 8.6 8.9 9.0" ^
  -DCUDA_ARCH_PTX="6.0 6.1 7.0 7.5 8.0 8.6 8.9 9.0" ^
  -DWITH_CUBLAS=ON ^
  -DCUDA_FAST_MATH=ON ^
  -DCUDA_SDK_ROOT_DIR="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.1" ^
  -DOPENCV_DNN_CUDA=ON ^
  -DWITH_MFX=ON ^
  -DWITH_OPENGL=ON ^
  ```
* Terminal `cmd` -> Config CUDA - lite
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
* Terminal `cmd` -> Config python
  ```
  -DPYTHON3_LIMITED_API=ON ^
  -DBUILD_opencv_python2=OFF ^
  -DBUILD_opencv_python3=ON
  ```
* Terminal `cmd` -> Build cmake
  ```
  cmake --build %cvbuild% --target INSTALL --config Release
  ```
* Make ready & create WHL
  - Clone `git clone --single-branch --branch "cp311+cu121" https://github.com/rathaumons/opencv-for-pyppbox.git`
  - Copy `{Python path}/Lib/site-packages/cv2/*` to [`cv2`](cv2) (Except those already present in [`cv2`](cv2))
  - Copy `cublas64_12.dll`, `cublasLt64_12.dll`, `cudnn64_8.dll`, `cudnn_cnn_infer64_8.dll`, `cudnn_ops_infer64_8.dll` from `{CUDA toolkit path}/CUDA/v12.1/bin` to [`cv2/cuda_bin`](cv2/cuda_bin) 
  - Copy `cvbuild/install/x64/vc16/bin/*` to [`cv2/python-3`](cv2/python-3)
  - Copy `cvbuild/install/etc/haarcascades/*` to [`cv2/data`](cv2/data)
  - Copy `cvbuild/install/etc/lbpcascades/*` to [`cv2/data`](cv2/data)
  - Copy `cvbuild/install/etc/quality/*` to [`cv2/data`](cv2/data)
  - Create WHL -> Run [`create_whl.cmd`](create_whl.cmd)
* Locate and install the newly created wheel
* Test your `cv2`
  ```
  import cv2
  cv2.__version__
  print(cv2.getBuildInformation()) 
  ```
