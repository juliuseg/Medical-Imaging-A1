# Import the required libraries
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
import skimage as ski
#T1 weighted phantom data
path = 'MRI/datacropped/'
v1_info = nib.load(path + '3D_T1w_20240920074836_A1B1.nii.gz').header
v1 = nib.load(path + '3D_T1w_20240920074836_A1B1.nii.gz').get_fdata()

print(v1_info)

print(v1_info['pixdim'])


voxel_size = v1_info['pixdim'][1:4]  # Extract voxel size (x, y, z)
print(f"Voxel size (in mm): x = {voxel_size[0]}, y = {voxel_size[1]}, z = {voxel_size[2]}")

slice_index = 375  # Get the middle slice along the third axis (axial)

# Extract the slice
axial_slice = v1[:, :, slice_index]
print (axial_slice.shape)

# Create the figure
fig, ax = plt.subplots()

# Plot the image with proper scaling
extent = [0, axial_slice.shape[0] * voxel_size[0], 0, axial_slice.shape[1] * voxel_size[1]]
ax.imshow(axial_slice.T, cmap='gray', origin='lower', extent=extent)

# Set axis labels with units
ax.set_xlabel('mm (x-axis)')
ax.set_ylabel('mm (y-axis)')
plt.title(f'Axial Slice at index {slice_index}')

# Display the plot
plt.show()

# Define slice index for the coronal plane (middle of the second axis)
#Fra y 160 til 336
coronal_slice_index = 275 #agurk 206 #275 #normal  # Adjust as needed

# Extract the coronal slice
coronal_slice = v1[:, coronal_slice_index, :]

# Create the figure
fig, ax = plt.subplots()

# Plot the image with proper scaling
extent = [0, coronal_slice.shape[0] * voxel_size[0], 0, coronal_slice.shape[1] * voxel_size[2]]
ax.imshow(coronal_slice.T, cmap='gray', origin='lower', extent=extent)

# Set axis labels with units
ax.set_xlabel('mm (x-axis)')
ax.set_ylabel('mm (z-axis)')
plt.title(f'Coronal Slice at index {coronal_slice_index}')

# Display the plot
plt.show()

# Define slice index for the sagittal plane (middle of the first axis)
#Fra 64 til 665 z
sagittal_slice_index = 200  # Adjust as needed

# Extract the sagittal slice
sagittal_slice = v1[sagittal_slice_index, :, :]

# Create the figure
fig, ax = plt.subplots()

# Plot the image with proper scaling
extent = [0, sagittal_slice.shape[0] * voxel_size[1], 0, sagittal_slice.shape[1] * voxel_size[2]]
ax.imshow(sagittal_slice.T, cmap='gray', origin='lower', extent=extent)

# Set axis labels with units
ax.set_xlabel('mm (y-axis)')
ax.set_ylabel('mm (z-axis)')
plt.title(f'Sagittal Slice at index {sagittal_slice_index}')

# Display the plot
plt.show()


# Define the ranges in millimeters
# Axial slice (x, y) in mm
axial_x_mm_start, axial_x_mm_end = 111, 140
axial_y_mm_start, axial_y_mm_end = 74, 95

# Coronal slice (x, z) in mm
coronal_x_mm_start, coronal_x_mm_end = 110, 146
coronal_z_mm_start, coronal_z_mm_end = 92, 131

# Sagittal slice (y, z) in mm
sagittal_y_mm_start, sagittal_y_mm_end = 73, 94
sagittal_z_mm_start, sagittal_z_mm_end = 90, 130

# Convert millimeters to voxel indices
axial_x_start, axial_x_end = int(axial_x_mm_start / voxel_size[0]), int(axial_x_mm_end / voxel_size[0])
axial_y_start, axial_y_end = int(axial_y_mm_start / voxel_size[1]), int(axial_y_mm_end / voxel_size[1])

coronal_x_start, coronal_x_end = int(coronal_x_mm_start / voxel_size[0]), int(coronal_x_mm_end / voxel_size[0])
coronal_z_start, coronal_z_end = int(coronal_z_mm_start / voxel_size[2]), int(coronal_z_mm_end / voxel_size[2])

sagittal_y_start, sagittal_y_end = int(sagittal_y_mm_start / voxel_size[1]), int(sagittal_y_mm_end / voxel_size[1])
sagittal_z_start, sagittal_z_end = int(sagittal_z_mm_start / voxel_size[2]), int(sagittal_z_mm_end / voxel_size[2])

# Adjust and display Axial slice
axial_slice_cropped = v1[axial_x_start:axial_x_end, axial_y_start:axial_y_end, slice_index]
plt.imshow(axial_slice_cropped.T, cmap='gray', origin='lower')
plt.title('Object 3 Axial Slice')
plt.xlabel('mm (x-axis)')
plt.ylabel('mm (y-axis)')
plt.show()

# Adjust and display Coronal slice
coronal_slice_cropped = v1[coronal_x_start:coronal_x_end, coronal_slice_index, coronal_z_start:coronal_z_end]
plt.imshow(coronal_slice_cropped.T, cmap='gray', origin='lower')
plt.title('Object 3 Coronal Slice')
plt.xlabel('mm (x-axis)')
plt.ylabel('mm (z-axis)')
plt.show()

# Adjust and display Sagittal slice
sagittal_slice_cropped = v1[sagittal_slice_index, sagittal_y_start:sagittal_y_end, sagittal_z_start:sagittal_z_end]
plt.imshow(sagittal_slice_cropped.T, cmap='gray', origin='lower')
plt.title('Object 3 Sagittal Slice')
plt.xlabel('mm (y-axis)')
plt.ylabel('mm (z-axis)')
plt.show()

# Intensity profiles for cropped slices

# Define the row for the horizontal line (adjust to fit the cropped image size)
line_row_axial = 20  # Example row index for Axial slice
line_row_coronal = 20  # Example row index for Coronal slice
line_row_sagittal = 20  # Example row index for Sagittal slice

# Axial slice intensity profile
axial_intensity_profile = axial_slice_cropped[line_row_axial, :]

# Coronal slice intensity profile
coronal_intensity_profile = coronal_slice_cropped[line_row_coronal, :]

# Sagittal slice intensity profile
sagittal_intensity_profile = sagittal_slice_cropped[line_row_sagittal, :]



# Plot each intensity profile with labels
#plt.plot(axial_intensity_profile, label='Axial Intensity Profile', color='r')
plt.plot(coronal_intensity_profile, label='Coronal Intensity Profile', color='g')


# Add title and labels
plt.title('Intensity Profiles Through the Phantom (Horizontal Line)')
plt.xlabel('Pixel Index')
plt.ylabel('Intensity')
plt.legend()
plt.grid(True)

# Display the plot
#plt.show()
# Plot intensity profiles
plt.figure(figsize=(10, 6))
plt.plot(sagittal_intensity_profile, label='Sagittal Intensity Profile', color='b')
# Add title and labels
plt.title('Intensity Profiles Through the Phantom (Horizontal Line)')
plt.xlabel('Pixel Index')
plt.ylabel('Intensity')
plt.legend()
plt.grid(True)

# Display the plot
#plt.show()
