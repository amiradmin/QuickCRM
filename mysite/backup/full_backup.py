import os
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from os import listdir
import schedule
import asyncio
from datetime import date
import time



# async def full_document_backup(dir_name: str):
async def full_document_backup( dir_name):
    """
    upload Django Media files
    """

    sharepoint_url = 'https://tescan2.sharepoint.com/sites/TESCanadaInc/'
        # # Initialize the client credentials
    user_credentials = UserCredential("amir.behvandi@tescan.ca", "Eddy@747")
    ctx = ClientContext(sharepoint_url).with_credentials(user_credentials)

    if dir_name:
        result = ctx.web.folders.add(f'Shared Documents/{dir_name}').execute_query()




    list_title = "Documents"
    # target_folder = ctx.web.lists.get_by_title(list_title).root_folder
    target_folder = ctx.web.get_folder_by_server_relative_url(f'Shared Documents/{dir_name}')


    # Working Code
    for root, dirs, files in os.walk(os.path.abspath("/home/amir/media/")):
        for folder in dirs:
            # print(folder)
            # if folder != 'admin':
            if folder == 'exam_result_file':
                sharepoint_path = f'Shared Documents/{dir_name}/{folder}'
                target_folder = ctx.web.get_folder_by_server_relative_url(sharepoint_path)
                result = ctx.web.folders.add(sharepoint_path).execute_query()
                # print(sharepoint_path)
                local_folder = os.path.join(root, folder)
                print(local_folder)
                # for root, dirs, files in os.walk(os.path.abspath(local_folder)):
                file_list = []
                #
                for file in listdir(local_folder) :
                    print(os.path.join(local_folder, file))
                    file_list.append(os.path.join(local_folder, file))


                for file in file_list:
                    path = file
                    with open(path, 'rb') as content_file:
                        file_content = content_file.read()
                        # target_folder = ctx.web.lists.get_by_title(list_title).root_folder
                    name = os.path.basename(file)
                    target_file = target_folder.upload_file(name, file_content).execute_query()
                    print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl))
                print("="*50)
        break


    # End Working Code


# full_document_backup('ERP Files Backup')

async def db_backup(delay):
    today = date.today()
    local_target_folder = "/home/amir/db_backup/backup-" + str(today)
    print(local_target_folder)
    os.system('sshpass -p "Eddy747today2022"  /usr/bin/pg_dump --file "'+ local_target_folder +'" --host "72.10.172.208" --port "5432" --username "tes_dbuser"  --verbose --format=c --blobs  "testdb" ')

    sharepoint_url = 'https://tescan2.sharepoint.com/sites/TESCanadaInc/'
        # # Initialize the client credentials
    user_credentials = UserCredential("amir.behvandi@tescan.ca", "Eddy@747")
    ctx = ClientContext(sharepoint_url).with_credentials(user_credentials)
    sharepoint_path = f'Shared Documents/ERP_DB_Backup/'
    target_folder = ctx.web.get_folder_by_server_relative_url(sharepoint_path)
    result = ctx.web.folders.add(sharepoint_path).execute_query()
    folder = 'db_backup'
    root = '/home/amir/'
    local_folder = os.path.join(root, folder)
    print(local_folder)
                # for root, dirs, files in os.walk(os.path.abspath(local_folder)):
    file_list = []
                #
    for file in listdir(local_folder) :
        print(os.path.join(local_folder, file))
        file_list.append(os.path.join(local_folder, file))

    for file in file_list:
        path = file
        with open(path, 'rb') as content_file:
            file_content = content_file.read()
                        # target_folder = ctx.web.lists.get_by_title(list_title).root_folder
            name = os.path.basename(file)
            target_file = target_folder.upload_file(name, file_content).execute_query()
            print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl))
    print("Task 2 Db backup")




async def main():
    task1 = asyncio.create_task(
        full_document_backup('ERP Files Backup')
        # full_document_backup('ERP Files Backup')
        )


    task2 = asyncio.create_task(
        db_backup(2)


        )

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
#
asyncio.run(main())
