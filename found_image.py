import os

def find_image_for_text_file(text_file_path, image_directory):
    # 텍스트 파일 이름에서 확장자를 제거하고 기본 이름을 얻습니다.
    base_name = os.path.splitext(os.path.basename(text_file_path))[0]

    # 이미지 파일에서 찾을 수 있는 확장자 목록
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

    for ext in image_extensions:
        image_file_path = os.path.join(image_directory, base_name + ext)
        if os.path.exists(image_file_path):
            return image_file_path
    
    return None

# 사용 예시
text_file_path = r'C:\Users\USER\Desktop\trafficsign2.v4i.yolov8\test\labels\-2023-07-31-11-53-57_png.rf.9f41ed6c62497738050ad3a72a026980.txt'
image_directory = r'C:\Users\USER\Desktop\trafficsign2.v4i.yolov8\test\images'

image_file_path = find_image_for_text_file(text_file_path, image_directory)

if image_file_path:
    print(f"이미지 파일을 찾았습니다: {image_file_path}")
else:
    print("해당 텍스트 파일에 대한 이미지 파일을 찾을 수 없습니다.")
