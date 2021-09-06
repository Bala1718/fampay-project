# Loads all the necessary imports for the views to work
from django.shortcuts import render
from googleapiclient.discovery import build
from api_code.models import Youtubevideo
from django.conf import settings
'''                                                                                                                                      
Getting all the Credentials.                                                                                                             
'''

yt_api_vers = settings.YOUTUBE_API_VERSION
yt_service_name = settings.YOUTUBE_API_SERVICE_NAME
dev_key = settings.DEVELOPER_KEY

file = open("date.txt", "r+")
updated_date = file.read()
final_updated_date = "2018-01-" + updated_date + "T00:00:00Z"
file.close()
file = open("date.txt", "w+")
file.write(str(int(float(updated_date)) + 1))
file.close()

'''
Building Youtube Object
'''
yt_object = build(yt_service_name, yt_api_vers,
                  developerKey=dev_key)

'''
Search Query with Youtube Videos with Date
'''
def youtube_search_keyword(query, max_results):
    search_keyword = yt_object.search().list(q=query, part="id, snippet", maxResults=max_results,
                                             relevanceLanguage='en', type='video', order='date',
                                             publishedAfter=final_updated_date).execute()

    videos_l = search_keyword.get("items", [])
    videos = []
    for x in videos_l:
        if x['id']['kind'] == "youtube#video":
            videos.append([x["snippet"]["title"],
                           x["id"]["videoId"], x['snippet']['description'],
                           x['snippet']['thumbnails']['default']['url'], x['snippet']['publishedAt']])
    return videos


def index(request):
    data = []
    file = open("update.txt", "r+")
    new_total = file.read()
    new_total_final = int(new_total)
    file.close()

    file = open("update.txt", "w+")
    file.write(str(int(new_total) + 1))
    file.close()

    # Youtube search videos
    search_vid = youtube_search_keyword('Virat Kohli Centuries', new_total_final)

    for i in range(len(search_vid)):
        result = search_vid[i]

        # Initializes the VideoData object, which is how the videos will be saved in the database
        new_vid = Youtubevideo(i, result[0], result[2], result[3], result[1], result[4])

        if new_vid not in list(Youtubevideo.objects.all()):
            new_vid.save()

    for i in Youtubevideo.objects.all():
        new_dict = {'id': i.id, 'title': i.title, 'description': i.description, 'url': i.url,
                    'unique_id': i.unique_id, 'published_at': i.published_at}

        data.append(new_dict)
    return render(request, 'index.html', {"data": data})
