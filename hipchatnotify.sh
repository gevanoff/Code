#!/bin/bash
#gevanoff 2014/09/11
#Send notification messages to internal HipChat

usage()
{
cat << EOF
usage: $0 options

This script sends a notification to Hip Chat.

OPTIONS:
   -h      Show this message
   -u      HipChat User self identification (defaults to username)
   -m      Message, in quotes (must be set)
   -c      Color: yellow, red, green, purple, gray, random (default: "yellow")
   -e      Environment/Room (default: opsint)
           stage -> "stage" 
           prod -> "Push It"
           ops -> "Ops"
           opsint -> "OpsInt"
           opsnoc -> "FiveWalls"
           solr -> "solr"
           outage -> "Production Outages"
           changes -> "Changes & Alerts"

EXAMPLE:
  $0 -u ExampleBot -m "Testing message to Ops" -c gray -e ops

EOF
}

failout()
{
  echo "$1 ."
  exit 1
}

#Variables
MSGCOLOR=
MSGUSER=
MSGENV=
ROOMID=
#CONFIG="room_id=OpsInt&from=${USER}&color=${MSGCOLOR}"
CONFIG="room_id=${ROOMID}&from=${MSGUSER}&color=${MSGCOLOR}"
MESSAGE=
LOCALDIR=~/cmdline-utils

#getopts grabs flags from command line
while getopts "hu:m:c:e:" OPTION
do
  case $OPTION in
    h)
      usage
      exit 1
      ;;
    u)
      MSGUSER=$OPTARG
      ;;
    c)
      MSGCOLOR=$OPTARG
      ;;
    e)
      MSGENV=$OPTARG
      ;;
    m)
      MESSAGE=$OPTARG
      if [[ -z $MESSAGE ]] ; then
        echo "-m requires a message in quotes"
        usage
        exit 1
      fi
      ;;
    ?)
      usage
      exit 1
      ;;
  esac
done

#Check to make sure there is a message
if [[ -z $MESSAGE ]] ; then
  echo "A message is required"
  usage
  exit 1
fi

#Set user to default if it doesn't exist
if [[ -z $MSGUSER ]] ; then
  MSGUSER=`whoami`
fi

#Set message color to default if it doesn't exit
if [[ -z $MSGCOLOR ]] ; then
  MSGCOLOR=yellow
fi
#  Color: yellow, red, green, purple, gray, random (default: "yellow")
case "$MSGCOLOR" in
  yellow)
    ;;
  red)
    ;;
  green)
    ;;
  purple)
    ;;
  gray)
    ;;
  random)
    ;;
  ?)
    echo "-c requires a valid color:" 
    echo "yellow, red, green, purple, gray, random"
    usage
    exit 1
    ;;
esac

#Set room to OpsInt if it isn't set
if [[ -z $MSGENV ]] ; then
  MSGENV=opsint
fi

#Set ROOMID. Replace spaces with %20
case "$MSGENV" in
  opsint)
    ROOMID="OpsInt"
    ;;
  ops)
    ROOMID="Ops"
    ;;
  opsnoc)
    ROOMID="FiveWalls"
    ;;
  stage)
    ROOMID="stage"
    ;;
  prod)
    ROOMID="Push%20It"
    ;;
  solr)
    ROOMID="solr"
    ;;
  outage)
    ROOMID="Production%20Outage%20Notifications"
    ;;
  changes)
    ROOMID="Changes%20%26%20Alerts"
    ;;
  ?)
    echo "-e requires a valid environment (check case)"
    usage
    exit 1
    ;;
esac

#CONFIG="room_id=OpsInt&from=${USER}&color=${MSGCOLOR}"
CONFIG="room_id=${ROOMID}&from=${MSGUSER}&color=${MSGCOLOR}"
AUTH=actualauthtokenhere

#New hipchat server
curl -d $CONFIG --data-urlencode "message=${MESSAGE}" 'https://hipchat.example.com/v1/rooms/message?auth_token=$AUTH&format=json'

#hipchat v2 version needs oauth token
#curl -H "Content-Type: application/json" \
#-X POST \
#-d "{\"color\": \"${MSGCOLOR}\", \"message_format\": \"text\", \"message\": \"${MESSAGE}\" }" \
#https://api.hipchat.com/v2/room/$ROOM_ID/notification=033f3b2f67790a2aaaa054761f1666
echo ""
