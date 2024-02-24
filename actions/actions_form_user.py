from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

api_url = "http://localhost:8000/api/user"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}  # Thay YOUR_ACCESS_TOKEN bằng mã thông báo của bạn
# payload = {"idChat": "1236", "name":"Đạt"}  # Thay đổi payload theo yêu cầu của API
class ActionWhatToEat(Action):
    def name(self) -> Text:
        return "action_form_name"
      
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
        payload = {
          "idChat":tracker.sender_id,
        }
      
        response = requests.post(api_url, headers=headers, data=payload)
        print(tracker.latest_message)
        
        if(response.status_code == 200):
          print(response)
          data = response.json()
        # Lấy giá trị của khóa 'name'
          user_name = data['User']['name']
          dispatcher.utter_message("Xin chào "+ user_name + ". Tôi có thể giúp gì cho bạn")
        else:
          dispatcher.utter_message("Bạn có thể cho tôi biết tên cho tiện xưng hô được không ạ")
        
        return []
      
class ActionCreateUSer(Action):
  def name(self) -> Text:
     return "action_create_User"
  
  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]
          ) -> List[Dict[Text, Any]]:
    name = tracker.get_slot('user_name')
    print (name)
    payload = {
      "idChat": tracker.sender_id,
      "name":name
    }
    api_urls = "http://localhost:8000/api/createUser"
    response = requests.post(api_urls,headers=headers,data=payload)
    
    if(response.status_code == 201):
      data = response.json()
      userName = data['User']['name']
      dispatcher.utter_message("Xin chào "+ userName + ". Tôi có thể giúp gì cho bạn")
    else:
        buttons = [{"title": "Có", "payload": "/change_name_yes"},
                   {"title": "Không", "payload": "/change_name_no"}]

        # Sử dụng dispatcher để hiển thị tin nhắn và nút
        dispatcher.utter_message(f"Bạn có muốn đổi tên thành {name} không ạ?",buttons=buttons)
        # image_path = "https://www.elle.vn/wp-content/uploads/2017/07/25/hinh-anh-dep-1.jpg"

        # # Sử dụng dispatcher.utter_attachment để gửi ảnh
        # dispatcher.utter_attachment({"image": image_path})
      
    return []
