'''
Author:     Aaron Dumbrow adumbrow@icloud.com
Date:       06/04/2019
Purpose:    This script leverages the python-plexapi, https://github.com/pkkid/python-plexapi, to sync the watched status across multiple Plex servers.
Version:    0.1
'''
import plexapi, sys

#Help file incase you forget to pass the arguments.
#TODO: Need to rewrite this with the argparse methodology
if len(sys.argv) != 3:
    print("Usage: python PlexStatusSync.py <IP of plex server> <token from your plex server>")

#Constant Variables
#TODO how do we store multiple Plex servers?
PlexServer = sys.argv[1]
Token = sys.argv[2]

#Function to create a connection to the Plex Server
#TODO: Need to test this.
def getPlexConnection( plexserver, token )
    #Connect to the Plex server
    from plexapi.server import PlexServer
    baseurl = 'http://' + plexserver + ':32400'
    #token = sys.argv[2]  --Left this in so I don't lose how I did it originally.
    plex = PlexServer(baseurl, token)
    return plex;

'''
#Function to get the watched status of an item
def getWatchedStatus( connection, type )
    #get the status of what we are looking at.
    items = connection.library.section(type)
    for item in items.search()
        if item.isWatched
            print(item.title + " is watched")
    return;
'''

#Test code
#Create connection
getPlexConnection( PlexServer,Token )
#get the unread movies
movies = plex.library.section('Movies')
#plexapi.video.Video.isWatched()?  https://python-plexapi.readthedocs.io/en/latest/modules/video.html#plexapi.video.Video.isWatched
for video in movies.search(unwatched=True):
        print(video.title)
