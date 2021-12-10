import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

current_dir = 'data/test'

# Percentage of images to be used for the test set
percentage_test = 0;

# Create and/or truncate train.txt and test.txt
file_train = open('data/newtest.txt', 'w')


# Populate train.txt and test.txt
counter = 1

for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_train.write("data/test" + "/" + title + '.jpg' + "\n")
    counter = counter + 1
    
