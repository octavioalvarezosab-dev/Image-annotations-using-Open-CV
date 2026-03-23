# Installation Instructions for OpenCV and LabelMe

This document provides step-by-step instructions on how to install OpenCV and LabelMe, which are essential for running the image annotations using the OpenCV in the repository. 

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- pip (Python package installer)

## Installing OpenCV

### Step 1: Install Python and pip
If you haven't installed Python yet, download and install it from the official [Python website](https://www.python.org/downloads/). Make sure to check the box that says "Add Python to PATH" during the installation.

### Step 2: Install OpenCV using pip
Open your command line or terminal and run the following command:
```bash
pip install opencv-python
```

### Step 3: Verify OpenCV Installation
To verify that OpenCV has been installed correctly, open a Python shell and run:
```python
import cv2
print(cv2.__version__)
```
If you see the version number printed out, OpenCV has been installed successfully.

## Installing LabelMe

### Step 1: Install LabelMe using pip
In your command line or terminal, run the following command:
```bash
pip install labelme
```

### Step 2: Verify LabelMe Installation
To verify the installation of LabelMe, run the following command in your command line:
```bash
labelme --version
```
If you see the version number, LabelMe has been installed successfully.

### Step 3: Running LabelMe
You can start LabelMe by simply typing the following command in your terminal:
```bash
labelme
```

## Conclusion
You have successfully installed OpenCV and LabelMe. You can now proceed to use this repository for image annotations using OpenCV. 

For any issues during the installation, refer to the official documentation or seek help in the community forums.