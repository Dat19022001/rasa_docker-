from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
list_of_level4 = ['giao_thuc_TCP','giao_thuc_IP','giao_thuc_HTTP','giao_thuc_FTP','giao_thuc_SMTP','giao_thuc_POP3','giao_thuc_MIME','giao_thuc_WAP','mo_hinh_OSI','mo_hinh_TCP/IP','PPPoE']
list_of_level2 = ['mo_hinh_tinh_toan_mang_tap_trung','mo_hinh_tinh_toan_mang_phan_tan','mo_hinh_tinh_toan_mang_cong_tac','mang_LAN','mang_MAN','mang_WAN','mang_hinh_sao','mang_tuyen_tinh','mang_hinh_vong','mang_ket_hop','mang_chuyen_mach_kenh','mang_chuyen_mach_thong_bao','mang_chuyen_mach_goi','mo_hinh_mang_ngang_hang','mo_hinh_mang_khach_chu','mo_hinh_workgroup','mo_hinh_domain','bang_thong','do_tre','thong_luong','phuong_thuc_unicast','phuong_thuc_multicast','phuong_thuc_broadcast','giao_thuc_truyen_thong','thiet_bi_truyen_dan','thiet_bi_ket_noi','point_to_point','Ethernet','token_ring','FDDI','mang_thue_bao','mang_chuyen_mach','ATM','x.25','frame_relay','DSL','ARPANET','NFSNET','internet','mang_khong_day','lien_mang','ISDN']
list_of_level3 = ['dinh_nghia_giao_thuc_truyen_thong','cac_loai_giao_thuc_tieu_bieu','giao_thuc_phi_ket_noi','giao_thuc_duong_ham','wireless_access_point','wireless_ethernet_bridge','card_mang','repeater','hub','bridge','modem','switch','router','brouter','gateway']
list_of_level1 = ['lich_su_mang_may_tinh','mo_hinh_tinh_toan_mang','dinh_nghia_mang_may_tinh','phan_loai_mang','mo_hinh_mang','phuong_phap_truyen_tin','mo_hinh_ung_dung_mang','mo_hinh_quan_ly_mang','thong_so_mang','phuong_phap_truyen_thong_du_lieu','thiet_bi_mang','cong_nghe_mang']

lists = [list_of_level1,list_of_level2,list_of_level3,list_of_level4]

class ActionWeatherFormSubmit(Action):
    def name(self) -> Text:
        return "action_return_answers"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict]:
      
      
        index = 0
        slot = tracker.get_slot('slot_mang_may_tinh')
        intent_name = tracker.latest_message['intent']['name']
        print(intent_name)
        df = pd.read_csv('D:/rasa/actions/rasadb.csv', sep=',')
       
        for j in lists:
            t = ''
            index = index + 1
            if intent_name in j:
                column_name = 'level' + str(index)
                return_df = df[df[column_name] == intent_name]
                return_df = return_df.reset_index(drop=True)
                num = return_df.value.count()
                i = 0
                while i < num:
                    t = t + '\n' + return_df.value[i] + '\n'
                    i = i+1  
                    # slot = None
                break
        print(t)
        dispatcher.utter_message(t)
        return []