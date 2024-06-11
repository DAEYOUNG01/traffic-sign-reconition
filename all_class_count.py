import os

def count_txt_files(directory):
    txt_count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            txt_count += 1
    return txt_count

# 사용 예시
input_directory = r'C:\Users\USER\Desktop\기말고사 데이터 셋\right_sign_9\valid\labels'

txt_file_count = count_txt_files(input_directory)
print(f"폴더 내부의 .txt 파일 개수: {txt_file_count}")
