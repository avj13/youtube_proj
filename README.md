# Project Goal

API Service to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Basic Workings:

- Server will call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.


- Support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Dashboard to view the stored videos with filters and sorting options (optional)
- Optimised search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`

# Reference:

- YouTube data v3 API: https://developers.google.com/youtube/v3/getting-started
- Search API reference: https://developers.google.com/youtube/v3/docs/search/list
    - To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
    - Without publishedAfter, it will give you cached results which will be too old
    
