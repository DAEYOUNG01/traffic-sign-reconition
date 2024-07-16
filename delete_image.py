# 타겟 클래스에 대한 이미지 및 라벨 삭제 파이썬 입니다.

import os

def find_images_to_keep(input_directory, image_directory, target_class):
    files_to_keep = set()

    # 6번 클래스가 포함된 텍스트 파일 찾기
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):  # 텍스트 파일만 처리
            file_path = os.path.join(input_directory, filename)
            keep_file = False  # 기본값은 파일 삭제

            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if parts and parts[0] == str(target_class):
                        keep_file = True  # 6번 클래스가 포함된 파일은 유지
                        break

            if keep_file:
                files_to_keep.add(os.path.splitext(filename)[0])
            else:
                os.remove(file_path)
                print(f"삭제된 텍스트 파일: {file_path}")

                # 해당 텍스트 파일에 대응되는 이미지 파일도 삭제
                image_file_path = os.path.join(image_directory, os.path.splitext(filename)[0] + ".jpg")
                if os.path.exists(image_file_path):
                    os.remove(image_file_path)
                    print(f"삭제된 이미지 파일: {image_file_path}")


input_directory = r'C:\Users\USER\Desktop\PBL2.v5i.yolov8 (1)\valid\labels'
image_directory = r'C:\Users\USER\Desktop\PBL2.v5i.yolov8 (1)\valid\images'
target_class = 6

find_images_to_keep(input_directory, image_directory, target_class)

print(f"클래스 {target_class}를 제외한 나머지 텍스트 파일 및 연동된 이미지 파일 삭제 완료.")
