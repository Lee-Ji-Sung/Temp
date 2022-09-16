import numpy as np
import pandas as pd
import open3d as o3d


if __name__ == "__main__":

    
    print(f"Load a ply point cloud. print it, and render it")
    ply_point_cloud = o3d.data.PLYPointCloud()
    pcd = o3d.io.read_point_cloud(ply_point_cloud.path)
    print(pcd)
    print(np.asarray(pcd.points))
    o3d.visualization.draw_geometries([pcd])
    
    
    print(f"test file...")