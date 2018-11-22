from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import datetime
import json

with open('opening_hours.json') as f:
    opening_hours = json.load(f)

class ActionCheckCurrentDate(Action):
    def name(self):
        return "action_check_current_date"

    def run(self, dispatcher, tracker, domain):
        week_day = datetime.datetime.today().strftime('%A')
        try:
            open_hour = opening_hours['items'][week_day]['open']
            close_hour = opening_hours['items'][week_day]['close']

            dispatcher.utter_message(f'On {week_day} we are open from {open_hour} till {close_hour}')

            return [SlotSet("matches", [f'We are open from {open_hour} till {close_hour}'])]

        except KeyError:
            print('No match for open hours')