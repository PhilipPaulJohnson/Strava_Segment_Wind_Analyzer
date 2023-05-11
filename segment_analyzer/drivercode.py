import pycurl
import certifi
from io import BytesIO
import json 
import dateutil.parser as d_parser
import datetime

from src.models import Effort, db
from src import create_app

from nu_auth import access_token

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


bearer = access_token

def date_conv(text):
    date = d_parser.parse(text)
    return str(date.isoformat())

def time_conv(inte):
    time = datetime.timedelta(seconds=inte)
    return time

def meters_conv(inte):
    miles = inte*0.000621371
    return miles

# Strava API variables
segment_id = 18672981
start_date = '2023-01-01'
end_date = '2023-01-31'
per_page = 40 #strava may reject request if too large

# Timeline Weather API variables
apikey = "key=JAEMLVA9PJZH3Z4XFSL7HM5Y7"
maxDistance = "13000" #weather station selection distance in meters from segment start point. 19k is 11.8 miles / 13k is 8.1 miles
timelineAuthCode = 'Authorization: Bearer fa58f4d6f0ee70e48fc2334d2ed959da7325413d'


conv_start_date = date_conv(start_date)
conv_end_date = date_conv(end_date)

#to list segment efforts
url = 'https://www.strava.com/api/v3/segment_efforts?segment_id=' + str(segment_id) + '&start_date_local=' + conv_start_date + '&end_date_local=' + conv_end_date + '&per_page=' + str(per_page)
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.setopt(pycurl.HTTPHEADER, ['Content-type:application/json','Authorization: Bearer ' + bearer])
c.perform()
c.close()

body = buffer.getvalue()
#print(body.decode('iso-8859-1'))

y = json.loads(body)
#print(y)
activity_count = str(len(y))
print('\n' + 'activity count: ' + activity_count + '\n')

act_count = 0
for activity in y:
    #print('activity number: ' + str((act_count)+1))
    print('effort ID: ' + str(y[act_count]['id']))
    print('segment name: ' + y[act_count]['name'])
    print('activity date/time: ' + str(y[act_count]['start_date_local']))
    print('activity ID: ' + str(y[act_count]['activity']['id']) + '\n')
    act_count = act_count + 1

user = input('please enter the effort ID: ')

#get segment effort
url = 'https://www.strava.com/api/v3/segment_efforts/' + user
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.setopt(pycurl.HTTPHEADER, ['Content-type:application/json','Authorization: Bearer ' + bearer])
c.perform()
c.close()

body = buffer.getvalue()
#print(body.decode('iso-8859-1'))
y = json.loads(body)
#print(y)
#print('\n')
#print(y.keys())
#_________________________________________________________________

print('\n' + '(effort ID)' + '\n')

effort__id = (str(y.get('id')))
effort_id = ('effort id: ' + str(y.get('id')))
print(effort_id)
effort__name = (y.get('name'))
effort_name = ('effort name: ' + y.get('name'))
print(effort_name)

print('\n' + '(athlete)' + '\n')

athlete__username = (str(y.get('athlete')['username']))
athlete_username = ('athlete username: ' + str(y.get('athlete')['username']))
print(athlete_username)

print('\n' + '(segment)' + '\n')

segment__name = (y.get('segment')['name'])
segment_name = ('segment name: ' + y.get('segment')['name'])
print(segment_name)
segment__id = (str(y.get('segment')['id']))
segment_id = ('segment id: ' + str(y.get('segment')['id']))
print(segment_id)

start_latlng = str(y.get('segment')['start_latlng'])
form__start_latlng = start_latlng[1:-1].replace(' ', '')
form_start_latlng = ('start latlng: ' + str(form__start_latlng))

start__date_time = y.get('start_date_local')
start_date_time = ('start date/time: ' + start__date_time)
print(start_date_time)
conv__elap_time = time_conv(y.get('elapsed_time'))
conv_elap_time = ('elapsed time: ' + str(conv__elap_time))
print(conv_elap_time)
conv__movi_time = time_conv(y.get('moving_time'))
conv_movi_time = ('moving time: ' + str(conv__movi_time))
print(conv_movi_time)
conv_effo_dist = meters_conv(y.get('distance'))
conv__effo_dist = format(conv_effo_dist,'.2f')
conv_effo_dist = ('effort distance: ' + str(conv__effo_dist))
print(conv_effo_dist)

conv_segm_dist = meters_conv(y.get('segment')['distance'])
conv__segm_dist = format(conv_segm_dist,'.2f')
conv_segm_dist = ('segment distance: ' + str(conv__segm_dist))
print(conv_segm_dist)

average__watts = (str(y.get('average_watts')))
average_watts = ('average watts: ' + str(y.get('average_watts')))
print(average_watts)
average__heartrate = str(y.get('average_heartrate'))
average_heartrate = ('average heartrate: ' + str(y.get('average_heartrate')))
print(average_heartrate)
max__heartrate = (str(y.get('max_heartrate')))
max_heart_rate = ('max heartrate: ' + str(y.get('max_heartrate')))
print(max_heart_rate)
#____________________________________________________________________

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + form__start_latlng + "/" + start__date_time + "/?" + apikey + "&include=current&maxDistance=" + maxDistance
#print(url)
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.setopt(pycurl.HTTPHEADER, ['Content-type:application/json', timelineAuthCode])
c.perform()
c.close()

body = buffer.getvalue()
#print(body.decode('iso-8859-1'))
y = json.loads(body)
#print(y.keys())

wind__speed = (str(y.get('currentConditions')['windspeed']))
wind_speed = ('wind speed: ' + str(y.get('currentConditions')['windspeed']))
print(wind_speed)
wind__direction = (str(y.get('currentConditions')['winddir']))
wind_direction = ('wind direction: ' + str(y.get('currentConditions')['winddir']))
print(wind_direction)
print('\n')

user = input('transfer effort ID to database: ' + effort__id + '? (y/n): ')

# starting to build function to import mulitple selections
# user = input('transfer effort id(s) seperated by a space: ')
# user_split = user.split(" ")

if user == 'y':
    def main():
        """Main driver function"""
        app = create_app()
        app.app_context().push()    
        
        sin_effort = None  # save last user
        sin_effort = Effort(
            effort_id = effort__id,
            effort_name = effort__name,
            athlete_username = athlete__username,
            segment_name = segment__name,
            segment_id = segment__id,
            start_date_time = start__date_time,
            elapsed_time = conv__elap_time,
            moving_time = conv__movi_time,
            effort_distance = conv__effo_dist,
            segment_distance = conv__segm_dist,
            average_watts = average__watts,
            average_heart_rate = average__heartrate,
            max_heart_rate = max__heartrate,
            wind_speed = wind__speed,
            wind_direction = wind__direction,
        )

        db.session.add(sin_effort)
        
        db.session.commit()

    # run script
    main()




