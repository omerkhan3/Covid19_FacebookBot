Facebook Corona Virus Bot


Functionality
User can subscribe to country and state/city (if in United States)
Type name of country state and city
Need to map to both country/state/city codes to name too; case in-sensitve
Map common typings of countries - “Holland” vs “Netherlands”, “US” vs “USA”
User can change subscription to country/state/city afterwards
Integrates with API data sources (http://coronavirusapi.com/ for state and https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest for countries).
Cronjob runs python script every x interval of time and sends updates.
User can unsubscribe

Tech Stack:
Python 3.X with API integration
Firebase - store User ID + Subscriptions
Google Cloud integration - cronjob schedule

Facebook API:
https://developers.facebook.com/docs/messenger-platform/
https://developers.facebook.com/docs/workplace/integrations/custom-integrations/bots/#botsinchat
https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start/

Simple Python implementation:

Need to review memory optimization
Efficiency in class design
Available functions & arguments 

