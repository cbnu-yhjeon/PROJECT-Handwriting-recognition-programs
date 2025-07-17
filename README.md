# ✍️ 손글씨 숫자 인식 프로그램 (Handwriting Digit Recognition)

<p align="center">
  <img src="https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge" alt="Status: Completed"/>
  <img src="https://img.shields.io/badge/python-3.9+-blue?style=for-the-badge&logo=python" alt="Python 3.9+"/>
  <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License: MIT"/>
</p>

TensorFlow/Keras를 사용하여 직접 구축한 CNN(Convolutional Neural Network) 모델로 손글씨 숫자를 인식하는 커맨드 라인 기반 프로그램입니다. `trainer.py`로 MNIST 데이터셋을 학습하고, `recognizer.py`에 직접 그린 숫자 이미지를 입력하여 인식 결과를 텍스트 파일로 출력합니다.

<br>

## 📸 실행 과정 (Execution Flow)

이 프로그램은 별도의 그래픽 UI 없이 커맨드 라인을 통해 실행됩니다.

1.  **입력 이미지 준비**: 그림판 등을 이용해 흰 배경에 검은색으로 숫자를 그린 이미지를 준비합니다. (예: `my_digit.png`)
    ![입력 이미지 예시](https://i.imgur.com/O91m2s9.png)

2.  **명령어 실행**: 터미널에서 `recognizer.py`를 실행하여 모델에 이미지를 입력합니다.
    ```bash
    python recognizer.py 2025254002.h5 my_digit.png
    ```

3.  **결과 확인**: 터미널과 텍스트 파일로 저장된 인식 결과를 확인합니다.
    ```
    인식된 숫자: 7
    결과를 '2025254002.txt' 파일에 저장했습니다.
    ```

## ✨ 주요 기능 (Key Features)

- **맞춤형 CNN 모델**: 두 개의 컨볼루션 레이어로 구성된 간단하고 효율적인 CNN 모델을 직접 설계하여 사용합니다.
- **커맨드 라인 인터페이스(CLI)**: GUI 없이 터미널에서 직접 모델과 이미지 경로를 인자로 받아 실행됩니다.
- **이미지 전처리**: 사용자가 직접 그린 이미지(흰 배경, 검은 글씨)를 MNIST 데이터셋 형식(검은 배경, 흰 글씨)에 맞게 자동으로 변환합니다.
- **결과 파일 출력**: 최종 인식 결과를 `<학번>.txt` 파일로 저장하여 제출 및 평가에 용이하도록 했습니다.

## 💻 기술 스택 (Tech Stack)

- **언어**: `Python`
- **핵심 라이브러리**: `TensorFlow`, `Keras`, `OpenCV-Python`, `NumPy`
- **학습 데이터셋**: `MNIST`

## 🗂️ 주요 파일 설명

- **`trainer.py`**: MNIST 데이터셋을 자동으로 불러와 CNN 모델을 학습시키고, 학습된 가중치를 `<학번>.h5` 파일로 저장합니다.
- **`recognizer.py`**: 커맨드 라인 인자로 모델 파일과 이미지 파일을 받아, 이미지를 전처리하고 숫자를 인식한 후, 결과를 터미널과 `<학번>.txt` 파일로 출력합니다.
- **`<학번>.h5`**: `trainer.py`를 통해 학습이 완료된 Keras 모델 파일입니다.
- **`<학번>.txt`**: `recognizer.py`가 생성하는 최종 숫자 인식 결과 파일입니다.

## 🛠️ 설치 및 실행 방법 (Installation & Usage)

### 1. 환경 설정

```bash
# 1. 프로젝트 저장소를 복제합니다.
git clone [https://github.com/cbnu-yhjeon/PROJECT-Handwriting-recognition-programs.git](https://github.com/cbnu-yhjeon/PROJECT-Handwriting-recognition-programs.git)

# 2. 프로젝트 디렉터리로 이동합니다.
cd PROJECT-Handwriting-recognition-programs

# 3. 필요한 라이브러리를 설치합니다.
pip install -r requirements.txt
```
> **`requirements.txt` 내용:**
> ```txt
> tensorflow
> opencv-python
> numpy
> ```

### 2. 모델 학습 (Training)

아래 명령어를 실행하면 MNIST 데이터셋을 자동으로 다운로드하여 모델 학습을 시작합니다.
```bash
python trainer.py
```
학습이 완료되면 `2025254002.h5` 모델 파일이 생성됩니다.

### 3. 숫자 인식 (Recognition)

인식할 숫자 이미지를 준비한 뒤 (예: `my_digit.png`), 아래와 같이 커맨드 라인에 모델 파일명과 이미지 파일명을 인자로 전달하여 실행합니다.
```bash
python recognizer.py 2025254002.h5 my_digit.png
```
실행이 완료되면 터미널에 인식된 숫자가 출력되고, `2025254002.txt` 파일이 생성됩니다.

## 🚀 모델 아키텍처 및 학습 과정

- **모델 구조**: `Keras Sequential` API를 사용하여 아래와 같은 순서의 간단한 CNN 모델을 구축했습니다.
    1.  `Conv2D` (32 filters, 3x3 kernel, a_relu)
    2.  `MaxPooling2D` (2x2)
    3.  `Conv2D` (64 filters, 3x3 kernel, relu)
    4.  `MaxPooling2D` (2x2)
    5.  `Flatten`
    6.  `Dense` (128 units, relu)
    7.  `Dropout` (0.5)
    8.  `Dense` (10 units, softmax) - 최종 출력층

- **학습 상세**:
  - **데이터셋**: MNIST (학습 60,000장, 테스트 10,000장)
  - **최적화기(Optimizer)**: `Adam`
  - **손실 함수(Loss Function)**: `categorical_crossentropy`
  - **배치 크기(Batch Size)**: 128
  - **에포크(Epochs)**: 10

## 📜 라이선스 (License)

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.

---
*Made by **전양호***
