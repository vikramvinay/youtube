import os
import json
import requests

natok = 'bangla+natok'
music = 'bangla+music'
movies = 'bangla+movies'
talkshow ='bangla+talk+show'
crime ='bangla+crime'

save_to_file = open('Collected Data/youtube_magazine.txt','r+',buffering=-1)

i=0
pagetoken = ''
video = []

while i <9:
    ## You need to replace YOUR_API_KEY below with your YouTube API key
    url_start = "https://www.googleapis.com/youtube/v3/search?q=bangla+magazine&alt=json&part=id,snippet&key=YOUR_API_KEY&maxResults=50&pageToken="+pagetoken
    data = requests.get(url_start).json()
    if i== 0:
        total_results = data['pageInfo']['totalResults']
        total_results = 'total_results='+str(total_results)+'\n'
        save_to_file.write(total_results)
        save_to_file.flush()
        os.fsync(save_to_file.fileno())
    pagetoken = data['nextPageToken']
    print(pagetoken)
    id_no = 0
    while id_no <50:
        
        if data['items'][id_no]['id']['kind']== 'youtube#video':
            video_id = data['items'][id_no]['id']['videoId']
            #print(video_id)
            video.append(video_id)
        
        id_no += 1
        
    i += 1
    print(video)
    print(video.__len__())


for item in video:
    url_video = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id='+item+'&key=AIzaSyCS5ZCDczPnuJOge7Zwv4-sJEygFJHorfk'
    
    video_data = requests.get(url_video).json()
    #title = video_data['items'][0]['snippet']['title']
    #channel_id = video_data['items'][0]['snippet']['channelId']
    #channel_title = video_data['items'][0]['snippet']['channelTitle']
    views = video_data['items'][0]['statistics']['viewCount']
    likes = video_data['items'][0]['statistics']['likeCount']
    dislikes = video_data['items'][0]['statistics']['dislikeCount']
    favorite = video_data['items'][0]['statistics']['favoriteCount']
    comments = video_data['items'][0]['statistics']['commentCount']
    print(item, views, likes, dislikes, favorite, comments)
    video_stats = item+';'+views+';'+likes+';'+dislikes+';'+favorite+';'+comments+'\n'
    #video_stats = video_stats.encode('ascii','replace')
    #video_stats = video_stats.decode('ascii','replace')
    save_to_file.write(video_stats)
    save_to_file.flush()
    os.fsync(save_to_file.fileno())
    
save_to_file.close()        
    

