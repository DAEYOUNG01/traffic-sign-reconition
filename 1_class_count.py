# 하나의 클래스 개수를 세는 파이썬 입니다.

import os

def count_class_in_txt_files(directory, target_class):
    class_count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if parts and parts[0] == str(target_class):
                        class_count += 1
                        break  # 해당 파일에 타겟 클래스가 있으면 더 이상 읽지 않고 다음 파일로 이동
    return class_count

# 사용 예시
input_directory = r'C:\Users\USER\Desktop\기말고사 데이터 셋\right_sign_9\valid\labels'
target_class = 9

class_file_count = count_class_in_txt_files(input_directory, target_class)
print(f"클래스 {target_class}가 포함된 .txt 파일 개수: {class_file_count}")
