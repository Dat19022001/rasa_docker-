
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionWhatToEat(Action):
    def name(self) -> Text:
        return "action_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        age = tracker.get_slot("age")
        print(age)
        return []
