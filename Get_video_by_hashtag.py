import requests
import json
import os

id = '20884' #MTL

all_video_data = []
all_hashtag_data = []

def first_connexion():

    headers = {
        'X-API-KEY': '37maK1w2e7oDLhQdOGDoLG9rubDTXX5i',
        'accept': 'application/json',
    }
    params = {
        'id': id, #Modify this value [id] to get another Hashtag feed - The link between Hashtags and ID is stored in the #_data_file
    }

    response = requests.get('https://api.tikapi.io/public/hashtag', params=params, headers=headers)
    data = response.json()
    return data

def get_data_content(data):
    #To only presevre data needed in a list of dictionary
    dict = {'author_id': None,
         'username': None,
         'followers_Count': None,
         'create_time': None,
         'description': None,
         'content_id': None,
         'content_isAd': None,
         'commentCount': None,
         'diggCount': None,
         'playCount': None,
         'shareCount': None,
         'video_duration': None,
         'video_download': None
    }
    list_dict = [] #for each items there will be a dict like above stored in this list

    dict_hashtag = {
        'title' : None,
        'id' : None,
        'isCommerce' : None
    }
    list_hashtags = [None] #hashtag will be stored in this list

    #for next page generation
    cursor = None
    hasNext = None

    for info in data:
        cursor = data['cursor']
        hasNext = data['hasMore']

    itemlist = data['itemList']

    for item in itemlist:

       author_id = item["author"]['id'] #retrieve DATA from Itemlist
       dict['author_id'] = author_id #export data to our dict

       username = item["author"]['uniqueId']
       dict['username'] = username

       followers_Count = item['authorStats']['followerCount']
       dict['followers_Count'] = followers_Count

       create_time = item['createTime']
       dict['create_time'] = create_time

       description = item['desc']
       dict['description'] = description

       content_id = item['id']
       dict['content_id'] = content_id

       content_isAd = item['isAd']
       dict['content_isAd'] = content_isAd

       comment_count = item['stats']['commentCount']
       dict['commentCount'] = comment_count

       digg_count = item['stats']['diggCount']
       dict['diggCount'] = digg_count

       play_count = item['stats']['playCount']
       dict['playCount'] = play_count

       share_count = item['stats']['shareCount']
       dict['shareCount'] = share_count

       video_download = item['video']['downloadAddr']
       dict['video_download'] = video_download

       video_duration = item['video']['duration']
       dict['video_duration'] = video_duration

       dict_copy = dict.copy()
       list_dict.append(dict_copy)

       #Hashtag data stored  into a dictionary into a list
       hashtags_list = item['challenges']

       for hashtag in hashtags_list:
        dict_hashtag['title'] = hashtag['title']
        dict_hashtag['id'] = hashtag['id']
        dict_hashtag['isCommerce'] = hashtag['isCommerce']

        dict_hashtag_copy = dict_hashtag.copy()
        list_hashtags.append(dict_hashtag_copy)

    list_hashtags.pop(0)

    # For simplicity purpose all the lists are added in the big an final list.
    # Append all those list to the final one, at the end of the loop.
    for i in list_hashtags:
        all_hashtag_data.append(i)

    for i in list_dict:
        all_video_data.append(i)

    #get the final List[video_data] sorted by number of likes
    sorted_all_video_data = sorted(all_video_data, key=lambda d: d['diggCount'], reverse=True)

    with open('#'+ id +'_data_video.json','w') as w:
        json.dump(sorted_all_video_data, w, indent=4)

    remove_dup(all_hashtag_data) #Sort the list


    with open('#'+ id +'#.json','w') as w:
        json.dump(all_hashtag_data, w, indent=4)

    print(str(cursor) + ' = cursor ')

    #making there is more element
    if(hasNext == True):
        return cursor
    else:
        print("No more page found")

def connexion_loop(cursor):
    NB_PAGE = 2 #Number of page returned [By 30 items in each page]. Already one called (get_data_content), so Add 1.
    for i in range(NB_PAGE):
        headers = {
            'X-API-KEY': '37maK1w2e7oDLhQdOGDoLG9rubDTXX5i',
            'accept': 'application/json',
        }
        params = {
            'id': id, #Modify this value [id] to get another Hashtag feed - The link between Hashtags and ID is stored in the #_data_file
            'count': '30',
            'cursor': cursor,
        }
        response = requests.get('https://api.tikapi.io/public/hashtag', params=params, headers=headers)
        data = response.json()

        if cursor == None:
            print('first cursor')
            pass
        else:
            cursor = get_data_content(data) # call again function with the data / get new cursor
    return cursor

def remove_dup(a): # remove duplicated value in list
    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[i] == a[j]:
                del a[j]
            else:
                j += 1
        i += 1
#MAIN
# The first connexion to the API
data = first_connexion()
get_data_content(data)
for info in data: #data from the first connexion
    cursor = data['cursor'] #get access to the first next cursor
connexion_loop(cursor)