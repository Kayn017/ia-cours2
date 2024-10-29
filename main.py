from src.ImageProcessor import ImageProcessor
import sys

image_path = sys.argv[1]
image_size = int(sys.argv[2])

processor = ImageProcessor(sys.argv[1])
processor.process_folder(image_size)
