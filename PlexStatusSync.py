'''
Author:     Aaron Dumbrow adumbrow@icloud.com
Date:       06/04/2019
Purpose:    This script leverages the python-plexapi, https://github.com/pkkid/python-plexapi, to sync the watched status across multiple Plex servers.
Version:
'''
import plexapi, sys

#Help file incase you forget to pass the arguments.
if len(sys.argv) != 3:
    print("Usage: python PlexStatusSync.py <IP of plex server> <token from your plex server")

#Connect to the Plex server
from plexapi.server import PlexServer
baseurl = 'http://' + (sys.argv[1]) + ':32400'
token = sys.argv[2]
plex = PlexServer(baseurl, token)

'''
movies = plex.library.section('Movies')
for video in movies.search(unwatched=True):
        print(video.title)
'''
