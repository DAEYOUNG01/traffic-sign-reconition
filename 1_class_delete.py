import os

def delete_target_class_files(input_directory, image_directory, target_class):
    # 1. 타겟 클래스가 포함된 텍스트 파일과 대응되는 이미지 파일 찾기
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):  # 텍스트 파일만 처리
            file_path = os.path.join(input_directory, filename)
            delete_file = False  # 기본값은 파일 유지

            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if parts and parts[0] == str(target_class):
                        delete_file = True  # 타겟 클래스가 포함된 파일은 삭제
                        break

            if delete_file:
                os.remove(file_path)
                print(f"삭제된 텍스트 파일: {file_path}")

                # 해당 텍스트 파일에 대응되는 이미지 파일도 삭제
                image_file_path = os.path.join(image_directory, os.path.splitext(filename)[0] + ".jpg")
                if os.path.exists(image_file_path):
                    os.remove(image_file_path)
                    print(f"삭제된 이미지 파일: {image_file_path}")

# 사용 예시
input_directory = r'C:\Users\USER\Desktop\데이터 셋\train\labels'
image_directory = r'C:\Users\USER\Desktop\데이터 셋\train\images'
target_class = 1

delete_target_class_files(input_directory, image_directory, target_class)

print(f"클래스 {target_class}가 포함된 텍스트 파일 및 연동된 이미지 파일 삭제 완료.")
