#!/usr/bin/python
#Dumps list of posts to blip.fm
#gevanoff@gmail.com

import requests, json, sys, getopt

def print_usage():
    print """Usage: blipdump -u <username> -o <offset> -n <number of blips>
  Defaults to username signum, 5 results, 0 offset
"""
    sys.exit(1)

def is_number(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

username = 'signum'
numoffset = '0'
numresults = '5'

try:
  opts, args = getopt.getopt(sys.argv[1:], 'u:o:n:h', ['username=', 'offset=', 'number=', 'help'])
except getopt.GetOptError:
  print_usage()
for opt, arg in opts:
  if opt in ('-h', '--help'):
    print_usage()
  elif opt in ('-u', '--username'):
    username = arg
  elif opt in ('-o', '--offset'):
    if is_number(arg):
      numoffset = arg
    else:
      print "The offset value must be an integer"
      print_usage()
  elif opt in ('-n', '--number'):
    if is_number(arg):
      numresults = arg
    else:
      print "The number of blips value must be an integer"
      print_usage()
  else:
    print_usage()


url = 'http://api.blip.fm/blip/getUserProfile.json?apiKey=&username=' + username + '&offset=' + numoffset + '&limit=' + numresults
r = requests.get(url)
tracklist = r.json()
for Bliptrack in tracklist['result']['collection']['Blip']:
    for key, value in Bliptrack.iteritems():
        if Bliptrack['type'] == 'youtubeVideo':
          blipurl = 'https://youtu.be/' + Bliptrack['url']
#        elif Bliptrack['type'] == 'songUrl':
#          blipurl = 'http://blip.fm/' + Bliptrack['url']
        else:
          blipurl = Bliptrack['type'] + ' ' + Bliptrack['url']
        artist = Bliptrack['artist']
        trackname = Bliptrack['title']
        bliptime = Bliptrack['insTime']
        #print key, 'is:', value
    print trackname, ',', artist, ',', blipurl, ',', bliptime    
