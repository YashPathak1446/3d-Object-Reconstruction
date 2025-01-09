# 3D Object Reconstruction form 2D image scans
## Overview
This projct demonstrates a comprehensive pipeline for 3D reconstruction of a mannequin using multi-view camera calibration, triangulation, mesh alignment, and advance mesh processing techniques. By combining image-based reconstruction, point cloud alignment, and meshing, the workflow generates a textured 3D model suitable for visualization and analysis.

## Live Demonstration
https://github.com/user-attachments/assets/27916bb3-f4b4-4010-9efd-34d4748bdc15



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
**1. Camera Calibration**
- Use the ```calib_jpg_u/``` folder containing checkerboard images for stereo calibration.
- The calibration code ```project.ipynb``` calculates intrinsic and extrinsic camera parameters.  
- Use calibration code to calculate camera matrices and distortion coefficients.

**2. 3D Point Cloud Generation**
- Triangulate 2D points from left and right camera views to generate 3D points through triangulation function in ```camutils.py```.
- Prune points outside the bounding box for cleaner reconstruction.

**3. Point Cloud Alignment**
- Align point clouds from ```manny/``` using ICP.
- Sample and align point clouds using the ICP algorithm to merge multiple viewpoints.
- Merge scans from all orientations (```grab_o_u``` to ```grab_4_u```) into a sinngle combined point cloud.
- Visualize the aligned point clouds to validate the alignment process through functions in ```visutils.py```.

**4. Mesh Reconstruction**
- Convert the combined point cloud into a 3D mesh using alpha-shape meshing.
- Clean up the mesh by removing the small disconnected components and unreferences vertices.

**5. Texture Mapping**
- Apply textures from the original images to the final mesh for photorealistic rendering.

## Project Structure
```
.
├── calib_jpg_u/
│   ├── frame_C0_01.jpg          # Checkerboard calibration viewpoint camera 0
│   ├── ...
|   ├── frame_C0_21.jpg
|   ├──frame_C1_01.jpg          # Checkerboard calibration viewpoint camera 1
|   ├──...
|   └── frame_C1_21.jpg
├── manny/                        # Folder consisting all mannequin scans
│   └── grab_0_u                  # Rotation orientation 0 of mannequin
│       ├── color_C0_00.png       # Structured light on manny0 from cam0 viewpoint
│       ├── ...
│       ├── color_C0_39.png
│       ├── color_C1_00.png       # Structured light on manny0 from cam1 viewpoint
│       ├── ...
│       └── color_C1_39.png
│   └── grab_1_u                  # Rotation orientation 1 of mannequin
│       ├── color_C0_00.png       # Structured light on manny1 from cam0 viewpoint
│       ├── ...
│       ├── color_C0_39.png
│       ├── color_C1_00.png       # Structured light on manny1 from cam1 viewpoint
│       ├── ...
│       └── color_C1_39.png
│   └── grab_2_u                  # Rotation orientation 2 of mannequin
│       ├── color_C0_00.png       # Structured light on manny2 from cam0 viewpoint
│       ├── ...
│       ├──color_C0_39.png
│       ├── color_C1_00.png       # Structured light on manny2 from cam1 viewpoint
│       ├── ...
│       └── color_C1_39.png
│   └── grab_3_u                  # Rotation orientation 3 of mannequin
│       ├── color_C0_00.png       # Structured light on manny3 from cam0 viewpoint
│       ├── ...
│       ├── color_C0_39.png
│       ├── color_C1_00.png       # Structured light on manny3 from cam1 viewpoint
│       ├── ...
│       └── color_C1_39.png
│   └── grab_4_u                  # Rotation orientation 4 of mannequin
│       ├── color_C0_00.png       # Structured light on manny4 from cam0 viewpoint
│       ├── ...
│       ├── color_C0_39.png
│       ├── color_C1_00.png       # Structured light on manny4 from cam1 viewpoint
│       ├── ...
│       └── color_C1_39.png        
|
├── camutils.py                   # Class Camera, also defines triangulation
|
├── combined_mesh.blend           # BPY Blend of combined mesh obj
|
├── combined_mesh.obj             # Obj of combined mesh obj
|
├── project.ipynb                 # File with all the code
|
├── mesh_manny                    # Folder containig 5 trimesh scans of mannequin
|   ├── mesh_manny0.obj
|   ├── mesh_manny1.obj
|   ├── mesh_manny2.obj
|   ├── mesh_manny3.obj
|   ├── mesh_manny4.obj
|
├── texture_triangle_mesh.obj     # Textured mesh of combined manny point cloud
|
├── visutils.ipynb                # Visualization using 3D Graph 
|
└── README.md                    # Project documentation
```
## Acknowledgments
- Open3d for 3D processing tools.
- The 3D reconstruction community for inspiration and techniques.
