# 이미지 개수를 세는 파이썬입니다.

import os

def count_image_files(directory):
    image_count = 0
    for filename in os.listdir(directory):
        if filename.endswith((".jpg", ".png")):
            image_count += 1
    return image_count

# 사용 예시
input_directory = r'C:\Users\USER\Desktop\train\wheelbarrow_7\valid\images'

image_file_count = count_image_files(input_directory)
print(f"폴더 내부의 이미지 파일(.jpg, .png) 개수: {image_file_count}")
