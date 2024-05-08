import cv2
import numpy as np
import random
import os


def apply_post_processing(id_card_syn, post_processing, blur_prob, noise_prob, color_prob, transform_prob):
    """
    Apply post-processing techniques to the synthetic ID card image based on the given probabilities and parameters.
    @param id_card_syn - the synthetic ID card image
    @param post_processing - a dictionary containing post-processing techniques and their parameters
    @param blur_prob - probability for blur technique
    @param noise_prob - probability for noise technique
    @param color_prob - probability for color technique
    @param transform_prob - probability for transform technique
    @return the processed synthetic ID card image
    """
    # Apply the post-processing techniques randomly
    for technique, params in post_processing.items():
        # Generate a random number between 0 and 1
        r = random.random()

        # Check if the random number is less than the probability of applying the technique
        if technique == "blur" and r < blur_prob:
            kernel_size = random.choice(params["kernel_sizes"])
            id_card_syn = cv2.GaussianBlur(id_card_syn, (kernel_size, kernel_size), 0)
        elif technique == "noise" and r < noise_prob:
            noise = np.random.normal(params["mean"], params["std"], id_card_syn.shape)
            id_card_syn = id_card_syn + noise.astype(np.int8)
        elif technique == "color" and r < color_prob:
            # Ensure the image is in BGR format (CV_8U) before color conversion
            if id_card_syn.dtype != np.uint8:
                    id_card_syn = cv2.convertScaleAbs(id_card_syn)
            id_card_syn = cv2.cvtColor(id_card_syn, cv2.COLOR_BGR2HSV)
            id_card_syn[:,:,0] = id_card_syn[:,:,0] + np.random.randint(-params["hue"], params["hue"])
            id_card_syn[:,:,1] = id_card_syn[:,:,1] + np.random.randint(-params["saturation"], params["saturation"])
            id_card_syn[:,:,2] = id_card_syn[:,:,2] + np.random.randint(-params["value"], params["value"])
            id_card_syn = cv2.cvtColor(id_card_syn, cv2.COLOR_HSV2BGR)
        elif technique == "transform" and r < transform_prob:
            height, width = id_card_syn.shape[:2]
            center = (width / 2, height / 2)
            angle = np.random.uniform(-params["angle"], params["angle"])
            scale = 1 + np.random.uniform(-params["scale"], params["scale"])
            shift_x = np.random.randint(-params["shift"], params["shift"])
            shift_y = np.random.randint(-params["shift"], params["shift"])
            matrix = cv2.getRotationMatrix2D(center, angle, scale)
            matrix[0, 2] += shift_x
            matrix[1, 2] += shift_y
            id_card_syn = cv2.warpAffine(id_card_syn, matrix, (width, height))
    return id_card_syn


def generate_synthetic_id_cards_for_folder(image_folder_path, num_images_per_id, output_folder):
    """
    Generate synthetic ID cards by applying `apply_post_processing` function based on the images in a specified folder.
    @param image_folder_path - The path to the folder containing the original ID card images.
    @param num_images_per_id - The number of synthetic ID card images to generate per original ID card image.
    @param output_folder - The folder where the synthetic ID card images will be saved.
    @return None
    """
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the post-processing techniques and their parameters
    post_processing = {
        "blur": {"kernel_sizes": [3, 5, 7, 9]},  # Gaussian blur
        "noise": {"mean": 0, "std": 10},  # Gaussian noise
        "color": {"hue": 30, "saturation": 30, "value": 30},  # HSV color adjustment
        "transform": {"angle": 30, "scale": 0.3, "shift": 30}  # Rotation, scaling, and translation
    }

    # Process each image in the specified folder
    for image_name in os.listdir(image_folder_path):
        image_path = os.path.join(image_folder_path, image_name)
        # Load the original ID card image
        id_card = cv2.imread(image_path)

        # Check if the image was loaded successfully
        if id_card is None:
            print(f"Could not load image {image_name}. Skipping...")
            continue

        # Generate synthetic images for the current ID card
        for i in range(num_images_per_id):
            # Copy the original ID card image
            id_card_syn = id_card.copy()

            # Apply post-processing
            id_card_syn = apply_post_processing(id_card_syn, post_processing, blur_prob=0.8, noise_prob=0.8, color_prob=0.8, transform_prob=0.8)

            # Save the synthetic ID card image in the output folder
            synthetic_image_name = f"synthetic_{os.path.splitext(image_name)[0]}_{i}.jpg"
            cv2.imwrite(os.path.join(output_folder, synthetic_image_name), id_card_syn)

            # Print the progress
            print(f"Generated synthetic image {synthetic_image_name}")


image_folder_path = "/home/saianiruth/Downloads/task_3/img"
num_images_per_id = 100
output_folder = "/home/saianiruth/Downloads/task_3/outimg"

generate_synthetic_id_cards_for_folder(image_folder_path, num_images_per_id, output_folder)

