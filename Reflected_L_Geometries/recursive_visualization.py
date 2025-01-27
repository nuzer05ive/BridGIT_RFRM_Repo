import numpy as np
import matplotlib.pyplot as plt

def generate_l_geometry(n):
    """
    Generates reflected L geometries at increasing recursion levels.

    Parameters:
    - n: Number of recursion levels
    """
    angles = [0, np.pi/2, np.pi, 3*np.pi/2]
    for i in range(n):
        plt.plot([0, np.cos(angles[i])], [0, np.sin(angles[i])], linewidth=2)
    
    plt.title("Reflected L Geometries")
    plt.show()

# Example usage
generate_l_geometry(4)
