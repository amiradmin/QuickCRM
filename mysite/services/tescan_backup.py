import os

os.system('sudo rm -r /home/amir/rep_media')
os.system('sshpass -p "q95yPd18npk8fC" scp -r root@185.231.59.78:/home/QuickCRM/mysite/media/ /home/amir/rep_media')