from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests




class ActionChangeNameYes(Action):
    def name(self) -> Text:
        return "action_change_name_yes"
      
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
        name = tracker.get_slot('user_name')
        
        payload = {
          "idChat":tracker.sender_id,
          "name": name
        }
        api_url = "http://localhost:8000/api/updateUser"
        headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"} 
      
        response = requests.put(api_url, headers=headers, data=payload)
        # print(tracker.latest_message)
        
        if(response.status_code == 200):
          data = response.json()
        # Lấy giá trị của khóa 'name'
          dispatcher.utter_message("Xin chào "+ name + ". Tôi có thể giúp gì cho bạn")
        
        return []
class ActionChangeNameNo(Action):
  def name(self) -> Text:
      return "action_change_name_no"      
  def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        payload = {
          "idChat":tracker.sender_id,
        }
        api_url = "http://localhost:8000/api/user"
        headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
        response = requests.post(api_url, headers=headers, data=payload)
       
        
        if(response.status_code == 200):
          data = response.json()
        # Lấy giá trị của khóa 'name'
          user_name = data['User']['name']
          dispatcher.utter_message("Xin chào "+ user_name + ". Tôi có thể giúp gì cho bạn")
        return []