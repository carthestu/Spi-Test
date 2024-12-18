# Import the necessary modules from the picamera library
import picamera
import picamera.array

def get_grayscale_values(coordinates):
    # Initialize the PiCamera object using a context manager
    with picamera.PiCamera() as camera:
        # Set the resolution to the desired size (optional)
        camera.resolution = (640, 480)
        
        # Create an output array to store the captured image in RGB format
        with picamera.array.PiRGBArray(camera) as output:
            # Capture an image and store it in the output array
            camera.capture(output, 'rgb')
            
            # List to store the grayscale values
            grayscale_values = []
            
            # Iterate over the coordinates to get the grayscale values
            for coordinate in coordinates:
                x, y = coordinate
                red = output.array[y, x, 0]   # Red value
                green = output.array[y, x, 1] # Green value
                blue = output.array[y, x, 2]  # Blue value
                
                # Calculate the grayscale value
                grayscale = round((red + green + blue) / 3)
                
                # Append the grayscale value to the list
                grayscale_values.append(grayscale)
            
            return grayscale_values

# Example usage
coordinates = [[100, 100], [50, 200]]
grayscale_values = get_grayscale_values(coordinates)
print(grayscale_values)
