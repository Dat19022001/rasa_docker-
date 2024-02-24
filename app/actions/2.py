# import pandas as pd

# # Đọc dữ liệu từ file CSV
# csv_path = "D:/rasa/actions/test.csv"
# df = pd.read_csv(csv_path, delimiter='\t')

# # Tạo một dictionary để lưu trữ câu hỏi cho mỗi intent
# intents_data = {}

# # Duyệt qua từng dòng trong DataFrame
# for index, row in df.iterrows():
#     parts = row['intent,question'].split(',')
#     intent_name = parts[0].strip()
#     question = parts[1].strip()

#     # Kiểm tra xem intent đã được thêm vào dictionary chưa
#     if intent_name not in intents_data:
#         intents_data[intent_name] = []

#     # Thêm câu hỏi vào danh sách câu hỏi của intent
#     intents_data[intent_name].append(question)

# # Tạo định dạng YAML từ dữ liệu intents

# yaml_content = "version: \"3.1\"\n\nnlu:\n"
# for intent_name, questions in intents_data.items():
#     yaml_content += f"  - intent: {intent_name}\n"
#     yaml_content += "     examples: |\n"
#     for question in questions:
#         yaml_content += f"        - {question}\n"

# # Lưu định dạng YAML vào một tệp
# with open("./data/nlu.yml", "w") as yaml_file:
#     yaml_file.write(yaml_content)