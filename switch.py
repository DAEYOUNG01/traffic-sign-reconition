import os

# 폴더 경로 설정 (백슬래시를 이스케이프 문자로 인식하지 않도록 raw 문자열 사용)
folder_path = r'C:\Users\USER\Desktop\trafficsign2.v4i.yolov8\valid\labels'

# 변경할 클래스 번호 설정
old_class = '10'  # 변경 전 클래스 번호
new_class = '9'  # 변경 후 클래스 번호

# 폴더 내의 모든 파일에 대해 클래스 번호 변경
for filename in os.listdir(folder_path):
    # 파일 경로 설정
    file_path = os.path.join(folder_path, filename)
    
    # 파일이 텍스트 파일인 경우에만 처리
    if filename.endswith('.txt'):
        # 파일 읽기
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # 파일 쓰기 (클래스 번호 변경)
        with open(file_path, 'w') as file:
            for line in lines:
                parts = line.split()
                if parts[0] == old_class:
                    parts[0] = new_class
                new_line = ' '.join(parts) + '\n'
                file.write(new_line)
                
        print(f'Updated: {filename}')
