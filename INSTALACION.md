# Instalación de OpenCV y LabelMe en Linux

## Requisitos Previos
Antes de comenzar la instalación de OpenCV y LabelMe, asegúrate de que tu sistema esté actualizado. Abre una terminal y ejecuta:

```bash
sudo apt-get update
sudo apt-get upgrade
```

## Instalación de Dependencias
Para compilar OpenCV y LabelMe, necesitas instalar ciertas dependencias. Ejecuta los siguientes comandos:

```bash
sudo apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libjpeg-dev libpng-dev libtiff-dev libatlas-base-dev gfortran libhdf5-dev
sudo apt-get install python3-dev python3-numpy python3-pyqt5
```

## Instalación de OpenCV
1. **Clona el repositorio de OpenCV y OpenCV contrib**:
   ```bash
   git clone https://github.com/opencv/opencv.git
   git clone https://github.com/opencv/opencv_contrib.git
   ```

2. **Crea un directorio de compilación**:
   ```bash
   cd opencv
   mkdir build
   cd build
   ```

3. **Configura la compilación utilizando CMake**:
   ```bash
   cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ..
   ```

4. **Compila OpenCV**:
   ```bash
   make -j$(nproc)
   ```

5. **Instala OpenCV**:
   ```bash
   sudo make install
   ```

6. **Verifica la instalación**:
   Ejecuta Python e importa OpenCV:
   ```bash
   python3 -c "import cv2; print(cv2.__version__)"
   ```

## Instalación de LabelMe
1. **Clona el repositorio de LabelMe**:
   ```bash
   git clone https://github.com/wgacofe/labelme.git
   ```

2. **Cambia al directorio de LabelMe**:
   ```bash
   cd labelme
   ```

3. **Instala LabelMe**:
   ```bash
   pip install -e .
   ```

4. **Verifica la instalación**:
   Ejecuta LabelMe en la terminal:
   ```bash
   labelme
   ```
   
## Conclusión
Ahora tienes OpenCV y LabelMe instalados en tu sistema Linux. Para cualquier duda, consulta la documentación oficial de OpenCV y LabelMe.