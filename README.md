# 3D Object Reconstruction form 2D image scans
## Overview
This projct demonstrates a comprehensive pipeline for 3D reconstruction of a mannequin using multi-view camera calibration, triangulation, mesh alignment, and advance mesh processing techniques. By combining image-based reconstruction, point cloud alignment, and meshing, the workflow generates a textured 3D model suitable for visualization and analysis.

## Features
- **Camera Calibration:** Computes intrinsic and extinsic camera parameters to accurately map 2D image coordinates to 3D space.
- **Triangulation:** Uses calibrated multi-view images to generate dense 3D points from stereo correspondences.
- **Point Cloud Alignment:** Aligns and merges multiple point clouds using Iterative Closest Point (ICP) algorithms for precise reconstruction.
- **Mesh Reconstruction:** Converts combined point clouds into a 3D mesh using alpha-shape meshing
- **Texture Mapping:** Applies texture from images to the reconstructed mesh for realistic visualization.
- **Noise Reduction:** Cleans up the mesh by removing unreferenced vertices and small disconnected components.


## Installation
#### Ensure you have the following libraries installed:
- **Python 3.8+**
- **Open3D** for point cloud and mesh processing
- **NumPy** for numerical/linear algebraic operations
- **Trimesh** for point cloud conversion
- **Matplotlib** for visualization during debugging

#### Install dependencies using ```pip```
```pip install open3d numpy trimesh matplotlib```

## Usage

