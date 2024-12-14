from datetime import datetime
import json
import locale
import os
import zipfile

def delete_all_files_in_folder(targetFolder):
    # Check if the target folder exists
    if not os.path.exists(targetFolder):
        print(f"The folder '{targetFolder}' does not exist.")
        return

    # List all files in the target folder
    for item in os.listdir(targetFolder):
        itemPath = os.path.join(targetFolder, item)

        # Check if the item is not .gitkeep
        if item != '.gitkeep':
            # If it's a directory, remove it and all its contents
            if os.path.isdir(itemPath):
                print(f'Deleting: {itemPath}')
                shutil.rmtree(itemPath)
            # If it's a file, remove it
            elif os.path.isfile(itemPath):
                print(f'Deleting: {itemPath}')
                os.remove(itemPath)

    print(f'All items in folder {targetFolder} have been deleted.')

def delete_files_except(dirpath, exceptFileEnding):
    # List all files in the directory, excluding zip files
    files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f)) and not f.endswith(exceptFileEnding)]

    # Remove every other file
    for i in range(len(files)):
        if i % 2 == 0:  # Change this condition to remove every other file
            fileToRemove = os.path.join(dirpath, files[i])
            print(f'Removing: {fileToRemove}')
            os.remove(fileToRemove)

def unpack_zip_files_in_subfolders(sourceFolder, targetFolder):
    # Walk through the directory
    for dirPath, dirNames, fileNames in os.walk(sourceFolder):
        # Delete every other file except zip in the current directory
        #delete_files_except(dirPath, '.zip')

        for filename in fileNames:
            # Check if the file is a zip file
            if filename.endswith('.zip'):
                zipFilePath = os.path.join(dirPath, filename)
                print(f'Unpacking: {zipFilePath}')

                # Create a ZipFile object and extract its contents
                with zipfile.ZipFile(zipFilePath, 'r') as zipRef:
                    zipRef.extractall(targetFolder)  # Extract to the same directory as the zip file

                # Delete the zip file after unpacking
                #os.remove(zipFilePath)
                #print(f'Deleted: {zipFilePath}')

def convert_to_locale_date(dateString, localeName='de_CH'):
    # Set the locale to Swiss German (or any other locale you prefer)
    locale.setlocale(locale.LC_TIME, localeName)

    # Parse the input date string in the format YYYYMMDD
    dateObject = datetime.strptime(dateString, "%Y%m%d")

    # Format the date into the locale-specific format
    return dateObject.strftime("%x")  # %x gives the locale's appropriate date representation

def convert_to_iso8601_date(dateString):
    # Parse the input date string in the format YYYYMMDD
    date_object = datetime.strptime(dateString, "%Y%m%d")

    # Format the date into ISO 8601 format YYYY-MM-DD
    return date_object.strftime("%Y-%m-%d")

def json_record_type_00(line):
    return {
        'recordType': line[0:2].strip(),
        'canton': line[2:4].strip(),
        'sslNumber': line[4:19].strip(),
        'creationDate': convert_to_iso8601_date(line[19:27].strip()),
        'text1': line[27:67].strip(),
        'text2': line[67:107].strip(),
        'codeState': line[107:110].strip()
    }

def json_record_type_06(line):
    return {
        'recordType': line[0:2].strip(),
        'transactionType': line[2:4].strip(),
        'canton': line[4:6].strip(),
        'taxAtSourceCode': line[6:16].strip(),
        'validFrom': convert_to_iso8601_date(line[16:24].strip()),
        'taxableIncomeFromInCHF': line[24:33].strip(),
        'tariffStepInCHF': line[33:42].strip(),
        'sexCode': line[42:43].strip(),
        'numberOfChildren': int(line[43:45].strip()),
        'minTaxInCHF': line[45:54].strip(),
        'taxRateInPercent': line[54:59].strip(),
        'codeState': line[59:62].strip()
    }

def json_record_type_11(line):
    return {
        'recordType': line[0:2].strip(),
        'transactionType': line[2:4].strip(),
        'canton': line[4:6].strip(),
        'codeTaxType': line[6:16].strip(),
        'validFrom': convert_to_iso8601_date(line[16:24].strip()),
        'taxableIncomeFromInCHF': line[24:33].strip(),
        'tariffStepInCHF': line[33:42].strip(),
        'sexCode': line[42:43].strip(),
        'numberOfChildren': int(line[43:45].strip()),
        'minTaxInCHF': line[45:54].strip(),
        'taxRateInPercent': line[54:59].strip(),
        'codeState': line[59:62].strip()
    }

def json_record_type_12(line):
    return {
        'recordType': line[0:2].strip(),
        'transactionType': line[2:4].strip(),
        'canton': line[4:6].strip(),
        'codePurchaseCommission': line[6:16].strip(),
        'validFrom': convert_to_iso8601_date(line[16:24].strip()),
        'taxableIncomeFromInCHF': line[24:33].strip(),
        'tariffStepInCHF': line[33:42].strip(),
        'sexCode': line[42:43].strip(),
        'numberOfChildren': int(line[43:45].strip()),
        'minTaxInCHF': line[45:54].strip(),
        'taxRateInPercent': line[54:59].strip(),
        'codeState': line[59:62].strip()
    }

def json_record_type_13(line):
    return {
        'recordType': line[0:2].strip(),
        'transactionType': line[2:4].strip(),
        'canton': line[4:6].strip(),
        'codeMedianValue': line[6:16].strip(),
        'validFrom': convert_to_iso8601_date(line[16:24].strip()),
        'taxableIncomeFromInCHF': line[24:33].strip(),
        'tariffStepInCHF': line[33:42].strip(),
        'sexCode': line[42:43].strip(),
        'numberOfChildren': int(line[43:45].strip()),
        'minTaxInCHF': line[45:54].strip(),
        'taxRateInPercent': line[54:59].strip(),
        'codeState': line[59:62].strip()
    }

def json_record_type_99(line):
    return {
        'recordType': line[0:2].strip(),
        'sslNumberSender': line[2:17].strip(),
        'cantonSender': line[17:19].strip(),
        'transmittedRecords': int(line[19:27].strip()),
        'checksumAmount': line[27:36].strip(),
        'codeState': line[36:39].strip()
    }

def process_txt_files(targetFolder):
    records = []
    jsonObject = []

    # Check if the target folder exists
    if not os.path.exists(targetFolder):
        print(f"The folder '{targetFolder}' does not exist.")
        return

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
                            case '00': records.append(json_record_type_00(line))
                            case '06': records.append(json_record_type_06(line))
                            case '11': records.append(json_record_type_11(line))
                            case '12': records.append(json_record_type_12(line))
                            case '13': records.append(json_record_type_13(line))
                            case '99': records.append(json_record_type_99(line))

            # Save the records to a JSON file
            jsonFileName = filename[:-4] + '.json'
            outputPath = os.path.join(targetFolder, jsonFileName)
            with open(outputPath, 'w') as jsonFile:
                json.dump(records, jsonFile, indent=4)

            print(f"Data has been saved to '{outputPath}'.")

            # Delete the txt file after saved as json
            os.remove(filePath)
            print(f'Deleted: {filePath}')

if __name__ == "__main__":
    sourceFolder = './source/'
    targetFolder = './target/'
    delete_all_files_in_folder(targetFolder)
    unpack_zip_files_in_subfolders(sourceFolder, targetFolder)
    process_txt_files(targetFolder)
