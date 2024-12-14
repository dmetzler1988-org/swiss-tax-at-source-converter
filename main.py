from modules import FileService

if __name__ == "__main__":
    sourceFolder = './source/'
    targetFolder = './target/'

    FileService.delete_all_files_in_folder(targetFolder)
    FileService.unpack_zip_files_in_subfolders(sourceFolder, targetFolder)
    FileService.process_txt_files(targetFolder)
