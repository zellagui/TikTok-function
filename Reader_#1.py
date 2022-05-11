import requests
import json
import urllib.request
from distutils.dir_util import copy_tree


content_name = '#roblox_159721'  #+-+-+-+-+-+-+-+-+-+-+CHANGE THIS with the new #name+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+

video_time = 0
time = 550 # change this value for more video ( this is scheduled for video of 7 min)

video_name = None
video_list = []
video_dict = {
    'username': None,
    'description': None,
    'content_id': None,
    'video_download': None
}

#+-+-+-+-+-+-+-+-+-+-+CHANGE THIS with 3_data_video.json file generated with get_vids#.py+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+
file = '/Users/zela/Documents/Webapp/Ratio-Bot/.idea/video_by#/data_video#/#roblox_159721/#159721_data_video.json'
video_path = []

with open(file, 'r') as f:
    data = json.load(f)

for content in data:
    if(content['video_duration'] > 42):
        continue

    video_time = content['video_duration'] + video_time



    username = content['username']
    video_dict['username'] = username

    description = content['description']
    video_dict['description'] = description

    content_id = content['content_id']
    video_dict['content_id'] = content_id

    video_link = content['video_download']
    video_dict['video_download'] = video_link

    dict_copy = video_dict.copy()
    video_list.append(dict_copy)

    video_name = '/Users/zela/Documents/Webapp/Ratio-Bot/.idea/video_by#/data_video#/'+content_name+'/'+ content_id +'.mp4' #change the first part fo another directory [path]



    r = requests.get(video_link, allow_redirects=True)

    open(video_name, 'wb').write(r.content)

    video_path.append(video_name) #List of all path

    if(video_time > time): # if video is longer than 8.6 minutes break
        break;


print(len(video_path))

print('The duration of the video is around: ' + str(video_time/60) + " Minutes")

copy_tree("/Users/zela/Documents/Webapp/Ratio-Bot/.idea/video_by#/data_video#", #Copy entir directory to TIKTOP FOLDER (PERSONAL)
          "/Users/zela/Desktop/TIKTOP/Tiktion_functions/video_by#")
