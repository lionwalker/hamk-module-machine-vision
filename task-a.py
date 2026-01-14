import cv2
import matplotlib.pyplot as plt

# 1. Downloaded image
file = 'img/1200px-Arara_Azul_no_Pantanal.jpg'

# 2. Load the image using OpenCV
img = cv2.imread(file)
if img is None:  # Check if image loaded successfully
    print(f"Error: Could not read file {file}")
else:

    # convert BGR2GB to use in matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 3. Split the BGR image into separate B, G, R channels
    B, G, R = cv2.split(img)

    # 5. Create the 2x2 grid for plotting
    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    # fig.tight_layout(pad=0.1)  # Add space between plots

    # Plot 1: Original Image
    axs[0, 0].imshow(img_rgb)
    axs[0, 0].set_title(f'Original | Lahiru Hewawasam', fontsize=7)
    axs[0, 0].axis('off')

    # Plot 2: Red Channel
    axs[0, 1].imshow(R, cmap='gray')
    axs[0, 1].set_title('RED Channel', fontsize=7)
    axs[0, 1].axis('off')

    # Plot 3: Green Channel
    axs[1, 0].imshow(G, cmap='gray')
    axs[1, 0].set_title('GREEN Channel', fontsize=7)
    axs[1, 0].axis('off')

    # Plot 4: Blue Channel
    axs[1, 1].imshow(B, cmap='gray')
    axs[1, 1].set_title('BLUE Channel', fontsize=7)
    axs[1, 1].axis('off')

    # 6. Save the 4-image grid
    output_path = "outputs/task-a.jpg"
    plt.savefig(output_path)
    print(f"Successfully saved the 4-image grid to {output_path}")

    # show the plot
    # plt.show()
