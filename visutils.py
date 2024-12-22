import numpy as np
import camutils
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D

def set_axes_equal_3d(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    limits = np.array([ax.get_xlim3d(),ax.get_ylim3d(),ax.get_zlim3d()])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    ax.set_xlim3d([origin[0] - radius, origin[0] + radius])
    ax.set_ylim3d([origin[1] - radius, origin[1] + radius])
    ax.set_zlim3d([origin[2] - radius, origin[2] + radius])

def label_axes(ax):
    '''Label x,y,z axes with default labels'''
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')


def vis_scene(camL,camR,pts3,looklength=20):
  '''Visualize a stereo scene reconstruction

  Parameters
  ----------
    camL,camR : Camera
    pts3 : 2D numpy.array (dtype=float) of shape (3,N)

  '''

  # generate coordinates of a line segment running from the center
  # of the camera to 3 units in front of the camera
  lookL = np.hstack((camL.t,camL.t+camL.R @ np.array([[0,0,looklength]]).T))
  lookR = np.hstack((camR.t,camR.t+camR.R @ np.array([[0,0,looklength]]).T))

  # 3D plot showing cameras and points
  fig = plt.figure()
  ax = fig.add_subplot(2,2,1,projection='3d')
  ax.plot(pts3[0,:],pts3[1,:],pts3[2,:],'.')
  ax.plot(camR.t[0],camR.t[1],camR.t[2],'ro')
  ax.plot(camL.t[0],camL.t[1],camL.t[2],'bo')
  ax.plot(lookL[0,:],lookL[1,:],lookL[2,:],'b')
  ax.plot(lookR[0,:],lookR[1,:],lookR[2,:],'r')
  set_axes_equal_3d(ax)
  label_axes(ax)
  plt.title('scene 3D view')

  # 2D view of the XZ axis
  ax = fig.add_subplot(2,2,2)
  ax.plot(pts3[0,:],pts3[2,:],'.')
  ax.plot(camR.t[0],camR.t[2],'ro')
  ax.plot(camL.t[0],camL.t[2],'bo')
  ax.plot(lookL[0,:],lookL[2,:],'b')
  ax.plot(lookR[0,:],lookR[2,:],'r')
  plt.title('XZ-view')
  plt.grid()
  plt.xlabel('x')
  plt.ylabel('z')

  # 2D view of the YZ axis
  ax = fig.add_subplot(2,2,3)
  ax.plot(pts3[1,:],pts3[2,:],'.')
  ax.plot(camR.t[1],camR.t[2],'ro')
  ax.plot(camL.t[1],camL.t[2],'bo')
  ax.plot(lookL[1,:],lookL[2,:],'b')
  ax.plot(lookR[1,:],lookR[2,:],'r')
  plt.title('YZ-view')
  plt.grid()
  plt.xlabel('y')
  plt.ylabel('z')

  # 2D view of the XY axis
  ax = fig.add_subplot(2,2,4)
  ax.plot(pts3[0,:],pts3[1,:],'.')
  ax.plot(camR.t[0],camR.t[1],'ro')
  ax.plot(camL.t[0],camL.t[1],'bo')
  ax.plot(lookL[0,:],lookL[1,:],'b')
  ax.plot(lookR[0,:],lookR[1,:],'r')
  ax.invert_yaxis()
  plt.title('XY-view')
  plt.grid()
  plt.xlabel('x')
  plt.ylabel('y')



def visualize_cameras_pts_recovered_pts(cams,recovered_points,points):
    fig = plt.figure()
    fig.tight_layout(pad=1.5,h_pad=0.5,w_pad=0.5)

    pts3=points
    pts3r = recovered_points
    
    # generate coordinates of a line segment running from the center
    # of the camera to 3 units in front of the camera

    looks = []
    for cam in cams:
        look = np.hstack((cam.t,cam.t+cam.R @ np.array([[0,0,6]]).T))
        looks.append(look)
        
 
    ax = fig.add_subplot(2,2,1,projection='3d')
    ax.plot(pts3[0,:],pts3[1,:],pts3[2,:],'b*')
    ax.plot(pts3r[0,:],pts3r[1,:],pts3r[2,:],'rx')
    for cam,look in zip(cams,looks):
        ax.plot(cam.t[0],cam.t[1],cam.t[2],'ro')
        ax.plot(look[0,:],look[1,:],look[2,:],'r')
    set_axes_equal_3d(ax)
    label_axes(ax)
    plt.title('scene 3D view')
    
    ax = fig.add_subplot(2,2,2)
    ax.plot(pts3[0,:],pts3[2,:],'b*')
    ax.plot(pts3r[0,:],pts3r[2,:],'rx')
    for cam,alook in zip(cams,looks):
        ax.plot(cam.t[0],cam.t[2],'ro')
        ax.plot(alook[0,:],alook[2,:],'r')
    ax.set_aspect('equal')
    plt.title('XZ-view')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('z')
    
    ax = fig.add_subplot(2,2,3)
    ax.plot(pts3[1,:],pts3[2,:],'b*')
    ax.plot(pts3r[1,:],pts3r[2,:],'rx')
    for cam,look in zip(cams,looks):
        ax.plot(cam.t[1],cam.t[2],'ro')
        ax.plot(look[1,:],look[2,:],'r')
    ax.set_aspect('equal')
    plt.title('YZ-view')
    plt.grid()
    plt.xlabel('y')
    plt.ylabel('z')

    ax = fig.add_subplot(2,2,4)
    ax.plot(pts3[0,:],pts3[1,:],'b*')
    ax.plot(pts3r[0,:],pts3r[1,:],'rx')
    for cam,look in zip(cams,looks):
        ax.plot(cam.t[0],cam.t[1],'ro')
        ax.plot(look[0,:],look[1,:],'r')
    ax.set_aspect('equal')
    plt.title('XY-view')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    
    fig.tight_layout(pad=1.1,h_pad=0,w_pad=0)

    print("Legend: Red is for ""reconstructed""!")