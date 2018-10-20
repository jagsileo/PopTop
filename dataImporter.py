import os, time
from datetime import datetime
from slackclient import SlackClient
access_token = os.environ['POPTOP_ACCESS_TOKEN']

date_from = os.environ["DATE_FROM"]
date_to = os.environ["DATE_TO"]


sc =SlackClient(access_token)


def getChannel(channelname):
    scope = 'channels.list'   
    channels = sc.api_call(scope)
    channel_id = None
    print(channelname)
    for channel in channels['channels']:
        if channel['name'] == channelname:
            return channel['id']
    if channel_id == None:
        raise Exception("cannot find channel " + channelname)
    return

def writeChannelMessagesToFile(filename, channelname):
    try:
        with open(filename, 'w') as f:
            f.write("")
    except IOError as e:
            print("Couldn't open or write to file (%s)." % e)        
    has_more = True
    oldest = (datetime.strptime(date_from, "%Y-%m-%d") - datetime(1970, 1, 1)).total_seconds()
    latest = (datetime.strptime(date_to, "%Y-%m-%d") - datetime(1970, 1, 1)).total_seconds()
    scope = 'channels.history'    
    channel_id = getChannel(channelname)
    while (has_more == True) and (latest >= oldest) :
        history = sc.api_call(scope, channel=channel_id, oldest=oldest, latest=latest)
        has_more = history['has_more']
        messages = history['messages']
        latest = messages[len(messages) - 1]['ts']
        try:
            with open(filename, 'a') as f:
                
                for messageInfo in history['messages']: 
                     f.write(messageInfo['text'].encode('utf-8'))
        except IOError as e:
            print("Couldn't open or write to file (%s)." % e)

        
        f.close()
    return filename    
