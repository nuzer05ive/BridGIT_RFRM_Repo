import numpy as np
import matplotlib.pyplot as plt

def recursive_fractal(n, R=1, factor=0.618, output_file="RFRM_output.png"):
    """
    Recursive Fractal Function for RFRM Visualization.
    
    Parameters:
    - n: Number of recursive iterations
    - R: Initial radius (default 1)
    - factor: Scaling factor (Golden Ratio approximation)
    - output_file: File to save the visualization
    """
    radii = [R * (factor ** i) for i in range(n)]
    angles = np.linspace(0, 2 * np.pi, 100)

    plt.figure(figsize=(6, 6))
    for r in radii:
        plt.plot(r * np.cos(angles), r * np.sin(angles), label=f'Iteration {r:.3f}')
    
    plt.title('Recursive Fractal Retrograde Model')
    plt.legend()
    plt.axis('equal')

    # Save the output to the specified file
    plt.savefig(output_file)
    print(f"Visualization saved as {output_file}")

# Example usage
recursive_fractal(8)
