import webbrowser
import httplib
import json

class Movie():

        
    def __init__(self,movie_title):

        #create api connection to database holding movie information
        conn = httplib.HTTPSConnection("api.themoviedb.org")
        payload = "{}"
        conn.request("GET", "/3/search/movie?api_key=83376f3d65f3bdf99855d374655e815e&query="+str(movie_title), payload)
        res = conn.getresponse()
        data = res.read()
        parsed_data = json.loads(data)
        conn.close()
        #get video details using the id from the initial search
        video_id = parsed_data['results'][0]['id']
        conn.request("GET", "/3/movie/"+str(video_id)+"/videos?api_key=83376f3d65f3bdf99855d374655e815e&language=en-US", payload)
        vid_res = conn.getresponse()
        video_data = vid_res.read()
        parsed_video_data = json.loads(video_data)
        conn.close()
        self.title = str(parsed_data['results'][0]['title']).encode("utf-8")
        self.storyline = str(parsed_data['results'][0]['overview'].encode("utf-8"))
        self.poster_image_url = str("https://image.tmdb.org/t/p/w1280/"+parsed_data['results'][0]['poster_path']).encode("utf-8")
        self.trailer_youtube_url = str("https://www.youtube.com/watch?v="+parsed_video_data['results'][0]['key']).encode("utf-8")
        conn.close()
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
