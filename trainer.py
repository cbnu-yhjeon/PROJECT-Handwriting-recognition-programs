import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np

# --- 1. 데이터 로드 및 전처리 ---
# 프로젝트 개요에 명시된 60,000장의 MNIST 필기 데이터셋을 사용합니다.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 이미지 데이터를 CNN 입력 형식에 맞게 변환 및 정규화
# (샘플 수, 높이, 너비, 채널 수)
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32') / 255

# 레이블을 원-핫 인코딩 방식으로 변환
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# --- 2. CNN 모델 구축 ---
model = Sequential([
    # 첫 번째 컨볼루션 레이어
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    # 두 번째 컨볼루션 레이어
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    # Fully Connected Layer를 위한 Flatten
    Flatten(),
    # Dense 레이어 및 Dropout (과적합 방지)
    Dense(128, activation='relu'),
    Dropout(0.5),
    # 출력 레이어 (0-9 숫자 판별)
    Dense(10, activation='softmax')
])

# --- 3. 모델 컴파일 ---
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 모델 구조 요약 출력
model.summary()

# --- 4. 모델 학습 ---
print("\n모델 학습을 시작합니다...")
model.fit(x_train, y_train,
          batch_size=128,
          epochs=10,
          verbose=1,
          validation_data=(x_test, y_test))

# --- 5. 학습된 모델 저장 ---
STUDENT_ID = "2025254002"
model_filename = f"{STUDENT_ID}.h5"
model.save(model_filename)

print(f"\n모델 학습 완료! '{model_filename}' 파일로 저장되었습니다.")