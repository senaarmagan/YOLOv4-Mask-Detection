import glob
import os

dataset_path = ("C:/Users/Sena Armağan/Documents/PythonPojects/Kaggle/mask detection/darknet/mask_data/images")

# Percentage of images to be used for the test set
percentage_test = 20;

# Create and/or truncate train.txt and test.txt
file_train = open('training.txt', 'w')  
file_test = open('testing.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.png")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test+1:
        counter = 1
        file_test.write( "mask_data/images/" + title + '.png' + "\n")
    else:
        file_train.write( "mask_data/images/" + title + '.png' + "\n")
        counter = counter + 1
