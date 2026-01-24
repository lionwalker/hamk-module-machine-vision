import cv2
import numpy as np
from datetime import date

INPUT_FILE = "outputs/robodk_snapshot.png"
OUTPUT_FILE = "outputs/robodk_annotated.png"

NAME = "Lahiru Hewawasam"
CURRENT_DATE = "10/12/2025"

# Annotation details

# Object 1: A Blue Box
OBJ1_LABEL = "Box"
# (Top-Left X, Top-Left Y, Bottom-Right X, Bottom-Right Y)
OBJ1_RECT_COORDS = (182, 240, 230, 285)
OBJ1_COLOR = (0, 0, 255)  # BGR Red
OBJ1_TEXT_COORDS = (180, 225)  # Text below the object

# Object 2: A Red Cone
OBJ2_LABEL = "Cone"
# (Center X, Center Y, Radius)
OBJ2_CIRCLE_COORDS = (212, 150, 35)
OBJ2_COLOR = (255, 0, 0)  # BGR Blue
OBJ2_TEXT_COORDS = (190, 100)  # Text above the object

# 1. Load the image
img = cv2.imread(INPUT_FILE)
if img is None:  # Check if image loaded successfully
    print(f"Error: Could not read file {INPUT_FILE}")

title_text = f"Annotated by {NAME}"
date_text = f"Date: {CURRENT_DATE}"
cv2.putText(
    img,
    title_text,
    (10, 10),                        # Starting position (X, Y)
    cv2.FONT_HERSHEY_SIMPLEX,      # Font type
    0.5,                           # Font scale
    (0, 0, 0),                     # Color: Black (BGR)
    1,                             # Thickness
    cv2.LINE_AA                    # Line type for smoothness
)
cv2.putText(
    img,
    date_text,
    (10, 30),                       # Starting position (X, Y)
    cv2.FONT_HERSHEY_SIMPLEX,      # Font type
    0.4,                           # Font scale
    (0, 0, 0),                     # Color: Black (BGR)
    1,                             # Thickness
    cv2.LINE_AA                    # Line type for smoothness
)

# --- Object 1 Annotation (Rectangle) ---
x1, y1, x2, y2 = OBJ1_RECT_COORDS
cv2.rectangle(img, (x1, y1), (x2, y2), OBJ1_COLOR, 2)
cv2.putText(
    img,
    OBJ1_LABEL,
    OBJ1_TEXT_COORDS,
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (0, 0, 0),
    1,
    cv2.LINE_AA
)

# --- Object 2 Annotation (Cone) ---
center_x, center_y, radius = OBJ2_CIRCLE_COORDS
cv2.circle(img, (center_x, center_y), radius, OBJ2_COLOR, 2)
cv2.putText(
    img,
    OBJ2_LABEL,
    OBJ2_TEXT_COORDS,
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (0, 0, 0),
    1,
    cv2.LINE_AA
)

# Save the annotated image
cv2.imwrite(OUTPUT_FILE, img)
print(f"Successfully saved annotated image to {OUTPUT_FILE}")
