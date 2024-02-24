
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionWhatToEat(Action):
    def name(self) -> Text:
        return "action_what_to_eat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        print(tracker.latest_message)
        dispatcher.utter_message("Ăn susi nha")
        return []
