from robodk import robolink

RDK = robolink.Robolink()

# Get camera object
cam = RDK.Item('Camera 1')

# Get and save image
file = RDK.getParam('PATH_OPENSTATION') + "/robodk_snapshot.png"
RDK.Cam2D_Snapshot(file, cam)
