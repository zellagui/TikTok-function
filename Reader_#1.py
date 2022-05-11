import requests
import json
import urllib.request
from moviepy.editor import *

video_time = 0
time = 500 # change this value for more video ( this is scheduled for video of 7 min)

video_name = None
video_list = []
video_dict = {
    'username': None,
    'description': None,
    'content_id': None,
    'video_download': None
}

file = '/Users/zela/Documents/Webapp/Ratio-Bot/.idea/Tiktion_functions/video_by#/data_video#/#20884_data_video.json'
video_path = []

with open(file, 'r') as f:
    data = json.load(f)

for content in data:

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

    video_name = '/Users/zela/Documents/Webapp/Ratio-Bot/.idea/Tiktion_functions/video_by#/data_video#/Video/video_'+content_id+'.mp4' #change the first part fo another directory [path]

    r = requests.get(video_link, allow_redirects=True)
    open(video_name, 'wb').write(r.content)

    video_path.append(video_name) #List of all path

    if(video_time > time): # if video is longer than 8.6 minutes break
        break;


print(len(video_path))

print('The duration of the video is around: ' + str(video_time/60) + " Minutes")

clip1 = VideoFileClip('/Users/zela/Documents/Webapp/Ratio-Bot/.idea/Tiktion_functions/video_6760948081396681989.mp4')
clip2 = VideoFileClip('/Users/zela/Documents/Webapp/Ratio-Bot/.idea/Tiktion_functions/video_6857645697915751686.mp4')

final_clip = concatenate_videoclips([clip1, clip2])
final_clip.write_videofile('output.mp4')