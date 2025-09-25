import cv2
import numpy as np

def apply_color_filter(image, filter_type):

  filtered_image = image.copy()
  if filter_type == "red_tint":
    filtered_image [ :, :, 0] = 0
    filtered_image [ :, :, 1] = 0
  elif filter_type == "blue_tint":
    filtered_image [ :, :, 1] = 0
    filtered_image [ :, :, 2] = 0
  elif filter_type == "green_tint":
    filtered_image [ :, :, 0] = 0
    filtered_image [ :, :, 2] = 0
  elif filter_type == "increase_red":
    filtered_image [:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
  elif filter_type == "decrease_blue":
    filtered_image [:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
  
  return filtered_image

image_path = 'HydroVolt Water Electricity Project.png'
image = cv2.imread(image_path)

if image is None:
  print('ERROR 404')
else:
  filter_type = "original"

print("press the following keys to apply a certain funtion:")
print("1: Red Filter")
print("2: Blue Filter")
print("3: Green Filter")
print("4: Increase_Red")
print("5: Decrease_Blue")
print("6: Exit Program")

while True:
  filtered_image = apply_color_filter(image, filter_type)
  cv2.imshow("filtered_image", filtered_image)
  key = cv2.waitKey(0) & 0xFF

  if key == ord('1'):
    filter_type = "red_tint"
  elif key == ord('2'):
    filter_type = "blue_tint"
  elif key == ord('3'):
    filter_type = "green_tint"
  elif key == ord('4'):
    filter_type = "increase_red"
  elif key == ord('5'):
    filter_type = "decrease_blue"
  elif key == ord('6'):
    print("exiting program...")

    break

  else:
    print("Error Occoured: Invalid Key")

  cv2.destroyAllWindows()