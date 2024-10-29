from src.ImageProcessor import ImageProcessor
import sys

if len(sys.argv) != 3:
    print("Usage: python main.py <folder_path> <image_size>")
    sys.exit(1)

image_path = sys.argv[1]
image_size = int(sys.argv[2])

processor = ImageProcessor(sys.argv[1])
processor.process_folder(image_size)
