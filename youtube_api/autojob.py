import asyncio
import requests

from web_project import settings
from .models import Video

from datetime import datetime, timedelta
from django_cron import CronJobBase, Schedule


import googleapiclient.discovery


query = "fashion"


async def update_videos():
    try:
        while True:
            apiKeys = settings.GOOGLE_API_KEYS
            time_now = datetime.now()

            # to keep the request with refreshed results
            fetch_request_time = time_now - timedelta(minutes=5)

            api_service_name = "youtube"
            api_version = "v3"

            
            is_key_valid = False

            for key in apiKeys:
                try:
                    
                    # make the youtube API request
                    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=key)
                    request = youtube.search().list(q=query, part="snippet", order="date", maxResults=50, publishedAfter=(fetch_request_time.replace(microsecond=0).isoformat()+'Z'))
                    response = request.execute()

                    is_key_valid = True
                    
                except Exception as e:
                    print(e)
                    break
                
                if is_key_valid:
                    break


            if is_key_valid:

                videos = response.json()

                # update the database with the latest fetched videos
                for video in videos['items']:
                    Video.objects.update_or_create(
                        video_id = video['id']['videoId'],
                        title = video['snippet']['title'],
                        description = video['snippet']['description'],
                        published_at = video['snippet']['publishedAt'],
                        channelId = video['snippet']['channelId'],
                        channelTitle = video['snippet']['channelTitle'],
                        thumbnailsUrl = video['snippet']['thumbnails']['default']['url']
                    )
                # wait for 10 seconds before making the next request
                    print(video['snippet']['title'])

                await asyncio.sleep(10)
    except Exception as e:
        print(e)


async def run_background_task():
    
    # RUN_EVERY_MINS = 5  

    # schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    # code = 'api.call_youtube_api'    # a unique code
    update_videos()
