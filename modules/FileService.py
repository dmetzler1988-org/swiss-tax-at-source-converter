import json
import os
import sys
import zipfile

from modules import JsonModelService

def check_folder_exist(folder):
    # Check if the folder exist
    if not os.path.exists(folder):
        print(f"The folder '{folder}' does not exist.")
        sys.exit()

def delete_all_files_in_folder(targetFolder):
    check_folder_exist(targetFolder)

    # List all files in the target folder
    for item in os.listdir(targetFolder):
        itemPath = os.path.join(targetFolder, item)

        # Check if the item is not .gitkeep
        if item != '.gitkeep':
            # Delete folder with all content if exist
            delete_folder(itemPath)
            # Delete the file if exist
            delete_file(itemPath)

    print(f'All items in folder {targetFolder} have been deleted.')

def delete_files_except(dirpath, exceptFileEnding):
    # List all files in the directory, excluding zip files
    files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f)) and not f.endswith(exceptFileEnding)]

    # Remove every other file
    for i in range(len(files)):
        if i % 2 == 0:  # Change this condition to remove every other file
            fileToRemove = os.path.join(dirpath, files[i])
            delete_file(fileToRemove)

def delete_file(filePath):
    if os.path.isfile(filePath):
        os.remove(filePath)
        print(f'Deleted: {filePath}')

def delete_folder(folderPath):
    if os.path.isdir(folderPath):
        shutil.rmtree(folderPath)
        print(f'Deleted: {folderPath}')

def unpack_zip_files_in_subfolders(sourceFolder, targetFolder):
    # Walk through the directory
    for dirPath, dirNames, fileNames in os.walk(sourceFolder):
        for filename in fileNames:
            # Check if the file is a zip file
            if filename.endswith('.zip'):
                zipFilePath = os.path.join(dirPath, filename)
                print(f'Unpacking: {zipFilePath}')

                # Create a ZipFile object and extract its contents
                with zipfile.ZipFile(zipFilePath, 'r') as zipRef:
                    zipRef.extractall(targetFolder)  # Extract to the same directory as the zip file

                # Delete the zip file after unpacking
                #delete_file(zipFilePath)

def create_json_file(filename, targetFolder, content):
    # Save the content to a JSON file
    jsonFileName = filename[:-4] + '.json'
    outputPath = os.path.join(targetFolder, jsonFileName)
    with open(outputPath, 'w') as jsonFile:
        json.dump(content, jsonFile, indent=4)

    print(f"Data has been saved to '{outputPath}'.")

def process_txt_files(targetFolder):
    records = []
    jsonObject = []

    # Check if the folder exist or exit
    check_folder_exist(targetFolder)

    # List all .txt files in the target folder
    for filename in os.listdir(targetFolder):
        if filename.endswith('.txt'):
            filePath = os.path.join(targetFolder, filename)
            print(f'Reading: {filePath}')

            # Read the content of the .txt file
            with open(filePath, 'r') as file:
                lines = file.readlines()  # Read all lines
                jsonStructure = []

                if len(lines) > 0:
                    for line in lines:
                        content = line.strip()  # Strip whitespace

                        match line[0:2]:
                            case '00': records.append(JsonModelService.json_record_type_00(line))
                            case '06': records.append(JsonModelService.json_record_type_06(line))
                            case '11': records.append(JsonModelService.json_record_type_11(line))
                            case '12': records.append(JsonModelService.json_record_type_12(line))
                            case '13': records.append(JsonModelService.json_record_type_13(line))
                            case '99': records.append(JsonModelService.json_record_type_99(line))

            # Save the records to a JSON file
            create_json_file(filename, targetFolder, records)

            # Delete the txt file after saved as json
            delete_file(filePath)