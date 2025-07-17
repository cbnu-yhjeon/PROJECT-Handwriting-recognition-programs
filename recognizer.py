import tensorflow as tf
import cv2
import numpy as np
import sys


def preprocess_image(image_path):
    """사용자가 그린 이미지를 모델 입력에 맞게 전처리하는 함수"""
    # 1. 이미지를 흑백으로 읽어오기
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"이미지 파일을 찾을 수 없습니다: {image_path}")
    # 2. MNIST와 같이 배경은 검은색, 글씨는 흰색으로 반전
    img = cv2.bitwise_not(img)
    # 3. 이미지 크기를 28x28로 조정
    img = cv2.resize(img, (28, 28))
    # 4. 데이터를 float32 타입으로 바꾸고 0~1 사이로 정규화
    img = img.astype('float32') / 255.0
    # 5. 모델 입력 형식에 맞게 차원 확장 (1, 28, 28, 1)
    img = np.reshape(img, (1, 28, 28, 1))

    return img


def recognize_digit(model_path, image_path):
    """모델을 로드하고 이미지를 인식하여 결과를 반환하는 함수"""
    # 1. 학습된 모델 로드
    try:
        model = tf.keras.models.load_model(model_path)
    except Exception as e:
        print(f"모델 파일 로드 오류: {e}")
        return None

    # 2. 이미지 전처리
    processed_image = preprocess_image(image_path)
    # 3. 숫자 예측
    prediction = model.predict(processed_image)
    # 4. 가장 확률이 높은 숫자의 인덱스 반환
    recognized_digit = np.argmax(prediction)

    return recognized_digit


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("사용법: python 3_recognize.py <model.h5> <image.png>")
        sys.exit(1)

    model_file = sys.argv[1]
    image_file = sys.argv[2]

    STUDENT_ID = model_file.split('.')[0]

    # 숫자 인식 실행
    result = recognize_digit(model_file, image_file)

    if result is not None:
        print(f"인식된 숫자: {result}")

        # 프로그램 출력: 평가용 이미지의 숫자를 파일로 출력
        # 파일이름: <학번>.txt
        output_filename = f"{STUDENT_ID}.txt"
        with open(output_filename, 'w') as f:
            f.write(str(result))
        print(f"결과를 '{output_filename}' 파일에 저장했습니다.")