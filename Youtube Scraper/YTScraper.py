# To get a Google Dev API Code follow instructions here 
# https://www.geeksforgeeks.org/youtube-data-api-set-1/
from googleapiclient.discovery import build
import os.path

#Needed inorder to create a youtube object
DEV_API_KEY = "AIzaSyBr-rPteg-j7txp7UJxEEFrzLEGxNpkR10"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DIR_PATH = r"C:\Users\alexr\OneDrive\Desktop\Python-Projects\Youtube Comment Scraper"

#Youtube object creation
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                                            developerKey = DEV_API_KEY)

def youtube_search_comments(video_id, maxAmount):

    video_response=youtube_object.commentThreads().list(
        part='id,snippet,replies',
        videoId=video_id,
        maxResults=maxAmount).execute()
    
    comments = ''
    for item in video_response['items']:
            comment = item['snippet']['topLevelComment']
            comments += comment['snippet']['textDisplay'] + '\r'
    file_name = "comments.txt"
    file_path = os.path.join(DIR_PATH, file_name)

    with open(file_path, 'w') as txt_file:
        txt_file.write(comments)        

    print("Completed Search, results have been written in videos.txt.")



def youtube_search_keyword(query, max_results):
    #retreiving youtube serach resutls
    search_keyword = youtube_object.search().list(q = query, part = "id, snippet",
                                               maxResults = max_results).execute()

    results = search_keyword.get("items", [])
    videos = []
    playlists = []
    channels = []
    videoTitles = ' '
    for result in results:
        # video result object
        if result['id']['kind'] == "youtube#video":
            videos.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"],
                            result["id"]["videoId"], result['snippet']['description'],
                            result['snippet']['thumbnails']['default']['url']))
            videoTitles += result["snippet"]["title"] + "\n"
            
  
        # playlist result object
        elif result['id']['kind'] == "youtube#playlist":
            playlists.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"],
                                 result["id"]["playlistId"],
                                 result['snippet']['description'],
                                 result['snippet']['thumbnails']['default']['url']))
  
        # channel result object
        elif result['id']['kind'] == "youtube#channel":
            channels.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"],
                                   result["id"]["channelId"], 
                                   result['snippet']['description'], 
                                   result['snippet']['thumbnails']['default']['url']))

    file_name = "videos.txt"
    file_path = os.path.join(DIR_PATH, file_name)

    with open(file_path, 'w') as txt_file:
        txt_file.write(videoTitles)
   
def main():

    option = input("Are you looking for comments on a video, or searching up videos by keywords? (Comments or Videos) ")
    
    if option == "comments" or option == "Comments" or option == "comment" or option == "Comment":
        videoID = input("What is the videos ID? ")
        maxSearch = input("How many results do you want to search for?: ")
        youtube_search_comments(videoID, maxSearch)
    elif option == "videos" or option == "Videos" or option == "video" or option == "Video":
        keyword = input("Enter keyword for search: ")
        maxSearch = input("How many results do you want to search for?: ")
        youtube_search_keyword(keyword, maxSearch)           
    else:
        print("Invalid Response")
        main()

    
main()