from InstagramAPI import InstagramAPI
import numpy as np
import time

username = ''
pwd = ''
API = InstagramAPI(username,pwd)
API.login()
time.sleep(2)

API.getProfileData()
my_id = API.LastJson['user']['pk']

API.getUsernameInfo(my_id)
n_media = API.LastJson['user']['media_count']

# API.getTotalSelfFollowers()
# followers_details=API.LastJson
# print(followers_details['users'][0]['username'])
# followers=[]
# for i in range(len(followers_details['users'])):
# 	followers.append(followers_details['users'][i]['username'])
# print(len(followers))
# # print(followers)	

# API.getTotalSelfFollowings()
# followings_details=API.LastJson
# # print(followings_details)
# followings=[]
# for i in range(len(followings_details['users'])):
# 	followings.append(followings_details['users'][i]['username'])
# print(len(followings))
# print(followings)

# media_ids = []
# max_id = ''
# for i in range(int(n_media/18)+1): 
#     API.getUserFeed(usernameId=my_id, maxid = max_id)
#     media_ids += API.LastJson['items'] 
#     if API.LastJson['more_available']==False:
#         print("no more avaliable")            
#         break
#     max_id = API.LastJson['next_max_id'] 
#     print(i, "   next media id = ", max_id, "  ", len(media_ids))
#     time.sleep(3)

# likers = []
# m_id = 0
# print("wait %.1f minutes" % (n_media*2/60.))
# for i in range(len(media_ids)):
#     m_id = media_ids[i]['id']
#     API.getMediaLikers(m_id)
#     likers += [API.LastJson]
#     time.sleep(2)
# print("done!")

# users = []
# for i in likers:
#         users += map(lambda x: i['users'][x]['username'],
#                      range(len(i['users'])))
# users_set = set(users)

# print("all users = ", len(users), " uniqum users = ", len(users_set))


# l_dict = {}
# for user in users_set:
#    # l_dict structure - {username:number_of_liked_posts} 
#    l_dict[user] = users.count(user)
# print(l_dict)   
