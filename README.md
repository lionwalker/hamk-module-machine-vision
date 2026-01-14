# Machine Vision Assignment 1: OpenCV & RoboDK

**Student Name:** Lahiru Madhusanka Hewawasam Halloluwage
**Date:** January 14, 2026

---

## Setup & Execution Instructions

This repository is structured to work with the automated grading script.

### 1. Repository Structure
```text
.
├── task-a.py                # Image channel splitting
├── task-b1.py               # RoboDK snapshot script
├── task-b2.py               # Image annotation script
├── requirements.txt         # List of dependencies
├── img/                     # Input folder
│   └── 1200px-Arara_Azul_no_Pantanal.jpg
└── outputs/                 # Output folder for results & station
    ├── HAMK_Robotics_station_MG400_with_camera.rdk
    ├── robodk_snapshot.png
```

### 2. How to Run

To replicate the environment and run the scripts, execute the following commands in your terminal. 

> **Note:** Ensure you have Python installed.

#### **Clone and Prepare**
```bash
# 1. Clone the repository
git clone https://github.com/lionwalker/hamk-module-machine-vision.git
cd hamk-module-machine-vision

# 2. Create a virtual environment named 'assign1'
python -m venv assign1

# 3. Activate the virtual environment
# On Windows:
assign1\Scripts\activate
# On macOS/Linux:
source assign1/bin/activate

# 4. Install required libraries
pip install -r requirements.txt
```

#### **Post-Execution & Cleanup**
Once the scripts have finished running, you can deactivate the virtual environment and remove it to keep the repository clean.

```bash
# 1. Deactivate the virtual environment
deactivate

# 2. Remove the virtual environment folder (optional for local cleanup)
# On Windows:
rmdir /s /q assign1
# On macOS/Linux:
rm -rf assign1
```

## Summary of Generated Deliverables

After the execution of the scripts, the following files will be generated or updated in your repository to verify the successful completion of the tasks:

| File | Source Script | Description |
| :--- | :--- | :--- |
| `outputs/task-a.jpg` | `task-a.py` | A 2x2 visualization grid showing the original RGB image and its individual B, G, and R grayscale channels. |
| `outputs/robodk_annotated.png` | `task-b2.py` | The RoboDK snapshot annotated with geometric shapes (rectangle/circle) and text labels identifying specific parts. |

---

## Lab Report: Findings & Reflections

### 1. Technical Implementation Findings
* **RoboDK API Versioning:** During Task B1, I identified that the standard keyword arguments for `width` and `height` in the `Cam2D_Snapshot` method were not supported by the current API version.
* **Relative Path Management:** To ensure the grading script functions correctly, I implemented relative paths (`img/` and `outputs/`). This prevents "File Not Found" errors that occur when using absolute local paths (e.g., `D:\Developments\...`).
* **OpenCV Coordinate System:** Selecting coordinates manually for Task B2 required an understanding of the image coordinate system, where $(0,0)$ is the top-left corner. This was done using a standard image editor to find pixel locations for the rectangle and circle.

### 2. Process Evaluation
* **Time Consumption:** The total project took approximately 5 hours. Setting up the RoboDK station and troubleshooting the API communication were the most time-intensive phases.
* **System Performance:** The Python scripts run efficiently. The image processing via OpenCV is nearly instantaneous, while the RoboDK bridge for capturing images takes less than one second.

### 3. AI Assistance Disclosure
I utilized AI (Gemini) as a thought partner throughout this assignment for:
* **Error Detection:** Debugging the `TypeError` encountered with the RoboDK Python API.
* **Report Structure:** Organizing the Markdown syntax and ensuring the repository structure met the assignment's technical requirements.
* **Technical Guidance:** Clarifying the BGR vs. RGB color space differences between OpenCV and Matplotlib.

### 4. Future Improvements
If I were to extend this project, I would implement **Automatic Feature Detection**. Instead of manual coordinates, I would use color-based thresholding (HSV) or Contour Detection to automatically locate the objects on the table and draw the bounding boxes dynamically.