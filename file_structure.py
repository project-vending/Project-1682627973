
import os

# Define the folder structure
folders = ['raw-data', 'refined-data', 'curated-data', 'query']

# Create the folders
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        
# Create empty files in each folder
for folder in folders:
    if folder != 'query':
        for i in range(1, 5):
            filename = folder + '/' + folder + '_file_' + str(i) + '.csv'
            with open(filename, 'w') as f:
                pass
