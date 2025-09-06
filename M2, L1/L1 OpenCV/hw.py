import cv2

# Read the image
img = cv2.imread("Space Logo.webp")

# Check if image loaded properly
if img is None:
    print("Error: Could not read the image.")
    exit()

# Resize to fixed size (say 400x400)
resized = cv2.resize(img, (400, 400))

# Show results
cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Optionally save the resized image
cv2.imwrite("Space Logo_resized.webp", resized)

