# Synthetic ID Card Image Generation

This Python script generates synthetic ID card images by applying various post-processing techniques to original ID card images.

## Overview

The script processes images in a specified folder, applies random post-processing techniques such as blur, noise, color adjustments (HSV), rotation, scaling, and translation, and saves the synthetic images to an output folder.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Saianiruthm/synthetic-id-card-generation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd synthetic-id-card-generation
   ```

3. Place your original ID card images in the `img` folder.

4. Adjust the parameters in the script if needed, such as the number of synthetic images per original ID card (`num_images_per_id`), post-processing probabilities (`blur_prob`, `noise_prob`, `color_prob`, `transform_prob`), and post-processing parameters in the `post_processing` dictionary.

5. Run the script:

   ```bash
   python task_3.py
   ```

   This will generate synthetic ID card images based on the original images in the `img` folder and save them to the `outimg` folder.

## Parameters

- `image_folder_path`: Path to the folder containing the original ID card images.
- `num_images_per_id`: Number of synthetic ID card images to generate per original ID card image.
- `output_folder`: Folder where the synthetic ID card images will be saved.
- `blur_prob`: Probability for applying Gaussian blur.
- `noise_prob`: Probability for adding Gaussian noise.
- `color_prob`: Probability for HSV color adjustment.
- `transform_prob`: Probability for rotation, scaling, and translation.

## Post-processing Techniques

- **Blur**: Gaussian blur with kernel sizes [3, 5, 7, 9].
- **Noise**: Gaussian noise with mean 0 and standard deviation 10.
- **Color Adjustment**: HSV color adjustment with random changes in hue, saturation, and value (brightness).
- **Transform**: Rotation, scaling, and translation with random angles, scales, and shifts.

## License

This project is licensed under the [MIT License](LICENSE).

