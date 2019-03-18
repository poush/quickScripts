#////////////////////////______ OPENCV With CUDA/GPU for Python ___/////

# ================================== 
# 
#  TESTED ON UBUNTU 18.04 :D
# 
# By default it assumes that python>=2.7 and numpy>1.5 is installed
#
#
# Pre-Requisites:
# 1. gcc-5 (with g++-5) {Script will attempt to install this}
# 2. Nvidia Driver
# 3. CUDA toolkit installed
#
#
# Piyush Agrawal <@poush> <me@ipiyush.com> :P 
# ======================================

###########################
# Configuration

# VERSION TO BE INSTALLED
OPENCV_VERSION='3.4.5'

# INSTALL PYTHON? (keep false to install OPENCV in virtual environment)
PYTHON_INSTALL=false


# CPU CORES (or Threads)
CPU_CORES=4
##########################


# 0. KEEP UBUNTU OR DEBIAN UP TO DATE
sudo apt-get -y update
# sudo apt-get -y upgrade       # Uncomment this line to install the newest versions of all packages currently installed
# sudo apt-get -y dist-upgrade  # Uncomment this line to, in addition to 'upgrade', handles changing dependencies with new versions of packages
# sudo apt-get -y autoremove    # Uncomment this line to remove packages that are now no longer needed


# 1. INSTALL THE DEPENDENCIES

echo "====Step: 1/3\n===="
echo "===================\n"

# Build tools: Compiler
sudo apt-get install -y build-essential cmake g++-5

# GUI (if you want to use GTK instead of Qt, replace 'qt5-default' with 'libgtkglext1-dev' and remove '-DWITH_QT=ON' option in CMake):
sudo apt-get install -y qt5-default libvtk6-dev

# Media I/O:
sudo apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libtiff-dev libjasper-dev libopenexr-dev libgdal-dev

# Video I/O:
sudo apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev

# Parallelism and linear algebra libraries:
sudo apt-get install -y libtbb-dev libeigen3-dev


if [ "$PYTHON_INSTALL" = true ]
then
sudo apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy
fi

# Documentation:
sudo apt-get install -y doxygen


# 2. INSTALL THE LIBRARY
echo "====Step: 2/3\n===="
echo "===================\n"

sudo apt-get install -y unzip wget
wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip
unzip ${OPENCV_VERSION}.zip
rm ${OPENCV_VERSION}.zip
mv opencv-${OPENCV_VERSION} OpenCV

wget https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip
unzip ${OPENCV_VERSION}.zip
rm ${OPENCV_VERSION}.zip
mv opencv_contrib-${OPENCV_VERSION}.zip opencv_contrib

cd OpenCV
mkdir build
cd build
cmake -D WITH_TIFF=ON \
    -D BUILD_TIFF=ON \
	-D WITH_QT=ON \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_CUDA=ON \
    -D ENABLE_FAST_MATH=1 \
    -D CUDA_FAST_MATH=1 \
    -D WITH_CUBLAS=1 \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
    -D ENABLE_PRECOMPILED_HEADERS=OFF \
    -D BUILD_opencv_java=OFF \
    -D CUDA_HOST_COMPILER:FILEPATH=/usr/bin/gcc-5 \
    -D BUILD_EXAMPLES=ON ..


echo "====Step: 3/3\n===="
echo "===================\n"
make -j${CPU_CORES}
sudo make install
sudo ldconfig


PDIR="$(python -c 'import site; print(site.getsitepackages()[0])')"
PYTHON="$(python -c 'import sys; print(".".join([str(x) for x in sys.version_info[:2]]))')"

ln -s /usr/local/lib/python$PYTHON/site-packages/cv2/python-$PYTHON/cv2.*.so $PDIR/cv2.so

rm -rf OpenCV
rm -rf opencv_contrib
