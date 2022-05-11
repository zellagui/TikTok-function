06/05/2022 - Montreal - Zela

This is the first function Created with the Tiktok API.
The purpose is to get access to all data to download the content only from an HASHTAG by ID.
The ID of # are stored in this file: #ID#.json
Function FIRST_CONNEXION:
    Connect for the pirst time to the API without ANY cursor.
    load Data into JSON form
        RETURN DATA

Function GET_DATA_CONTENT(DATA):
    2 dict with this form :
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
                            dict_hashtag = {
                                    'title' : None,
                                    'id' : None,
                                    'isCommerce' : None
                                }

    A loop occure over all the Data and retrieve this information for each item.
    Add the dict{} to list_dict[] then to all_video_data [].
    Dump all the data in a file.
        RETURN NEXT CURSOR

def connexion_loop(cursor):
    Loop with range = NB_PAGE.
    #Already  called (get_data_content) for first_connexion, so Add 1 for the nb of total page.
    Number of page returned [By 30 items in each page].
        RETURN CURSOR       (Which is get_data_content(data))


Main:
    data = first_connexion()
    get_data_content(data)
    for info in data: #data from the first connexion
        cursor = data['cursor'] #get access to the first next cursor
    connexion_loop(cursor)


For next run make sur :
    -API key still working
    -get the good file path for list_#