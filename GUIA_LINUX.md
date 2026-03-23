# Linux-Specific Instructions for Image Annotations Using Open CV

## Prerequisites
Before starting, ensure you have the following installed:
- Python 3.x
- OpenCV library
- NumPy library
- Other dependencies as specified in the project.

### Installation of Dependencies
Use the following commands to install the required dependencies:
```bash
sudo apt update
sudo apt install python3-opencv python3-numpy
```

## Setting Up the Environment
It is recommended to create a virtual environment for Python projects:
```bash
sudo apt install python3-venv
mkdir my_project && cd my_project
python3 -m venv venv
source venv/bin/activate
```

## Running the Application
To run the application, use the following command:
```bash
python3 main.py
```

## Best Practices
- Always use a virtual environment for projects to avoid dependency conflicts.
- Regularly update your packages:
  ```bash
sudo apt update && sudo apt upgrade
```
- Comment your code effectively to provide clarity on complex logical flows.
- Use version control (Git) to manage changes and collaborate with others.

## Troubleshooting
- If you encounter any issues related to OpenCV, ensure that you have the latest version installed:
```bash
pip install opencv-python --upgrade
```
- Check the compatibility of your system's Python version with the OpenCV library.

For any other specific issues, refer to the [OpenCV documentation](https://docs.opencv.org/) or seek help on forums.
