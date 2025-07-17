# ✍️ 손글씨 숫자 인식 프로그램 (Handwriting Digit Recognition)

<p align="center">
  <img src="https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge" alt="Status: Completed"/>
  <img src="https://img.shields.io/badge/python-3.9+-blue?style=for-the-badge&logo=python" alt="Python 3.9+"/>
  <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License: MIT"/>
</p>

간단한 CNN(Convolutional Neural Network) 모델을 기반으로, 사용자가 직접 캔버스에 그린 손글씨 숫자를 실시간으로 인식하는 프로그램입니다. 고전적인 머신러닝 데이터셋인 MNIST로 학습된 모델을 사용하며, 사용자는 웹 UI를 통해 직접 숫자를 그리고 인식 결과를 확인할 수 있습니다.

<br>

## 📸 데모 (Screenshots)

<p align="center">
  <img src="<./demo_handwriting.gif>" alt="프로그램 실행 데모" width="700"/>
  <em><p align="center">사용자가 '7'을 그리자 모델이 실시간으로 예측하는 화면</p></em>
</p>

## ✨ 주요 기능 (Key Features)

- **실시간 숫자 인식**: 사용자가 캔버스에 숫자를 그리는 동안 모델이 예측 결과를 실시간으로 업데이트합니다.
- **인터랙티브 캔버스**: 사용자가 자유롭게 숫자를 그리고, 'Clear' 버튼으로 쉽게 캔버스를 지울 수 있습니다.
- **확률 분포 시각화**: 0부터 9까지 각 숫자에 대한 모델의 예측 확률을 막대그래프로 보여줍니다.
- **직관적인 UI**: 별도 설치 없이 웹 브라우저만으로 쉽게 프로그램을 사용할 수 있습니다.

## 💻 기술 스택 (Tech Stack)

- **언어**: `Python 3.9`
- **핵심 라이브러리**: `PyTorch`, `NumPy`
- **웹 UI 및 캔버스**: `Streamlit`, `streamlit-drawable-canvas`
- **데이터 처리**: `Pillow`
- **학습 데이터셋**: `MNIST`

## 🚀 모델링 및 학습 과정 (Modeling & Training Process)

- **모델 구조**: 두 개의 합성곱 층(Convolutional Layers)과 두 개의 완전 연결 층(Fully Connected Layers)으로 구성된 간단한 CNN 모델을 직접 설계했습니다. 이미지의 공간적 특징을 효과적으로 학습하기에 적합한 구조입니다.
- **학습 데이터**: 28x28 픽셀 크기의 흑백 손글씨 숫자 이미지 7만 개(학습 6만, 테스트 1만)로 구성된 `MNIST` 데이터셋을 사용했습니다.
- **주요 하이퍼파라미터**:
  - `Epochs`: 10
  - `Batch Size`: 64
  - `Optimizer`: Adam
  - `Learning Rate`: 0.001

## 📊 성능 평가 (Performance)

MNIST 테스트 데이터셋(10,000개 이미지)으로 모델의 성능을 평가한 결과, 약 **99.2%**의 매우 높은 분류 정확도(Accuracy)를 달성했습니다.

## 🛠️ 설치 및 실행 방법 (Installation & Usage)

### 1. 사전 요구사항

- Python 3.9 이상
- Git

### 2. 설치 과정

```bash
# 1. 프로젝트 저장소를 복제합니다.
git clone [https://github.com/cbnu-yhjeon/PROJECT-Handwriting-recognition-programs.git](https://github.com/cbnu-yhjeon/PROJECT-Handwriting-recognition-programs.git)

# 2. 프로젝트 디렉터리로 이동합니다.
cd PROJECT-Handwriting-recognition-programs

# 3. 필요한 라이브러리를 설치합니다.
pip install -r requirements.txt
```
> **`requirements.txt` 예시:**
> ```txt
> torch
> numpy
> streamlit
> streamlit-drawable-canvas
> pillow
> ```

### 3. 프로그램 실행

아래 명령어를 터미널에 입력하여 웹 애플리케이션을 실행합니다.

```bash
streamlit run app.py
```

명령어 실행 후, 터미널에 나타나는 `Local URL` (예: http://localhost:8501)을 웹 브라우저에서 열어주세요.

## 📂 프로젝트 구조 (Project Structure)

```
PROJECT-Handwriting-recognition-programs/
├── 📄 app.py              # Streamlit 웹 애플리케이션 실행 파일
├── 📄 model.py             # CNN 모델 구조 정의 파일
├── 📄 train.py             # 모델 학습 스크립트
├── 📦 models/
│   └── 📄 mnist_cnn.pth    # 학습된 모델 가중치 파일
├── 📄 requirements.txt    # 필요한 파이썬 라이브러리 목록
├── 📄 .gitignore
└── 📄 README.md           # 바로 이 파일!
```

## 🤔 프로젝트 후기 (What I Learned)

CNN 모델의 기본 구조와 동작 원리를 직접 코드로 구현하며 깊이 있게 이해할 수 있었습니다. 특히, MNIST 데이터셋의 이미지(28x28)와 사용자가 캔버스에 그린 이미지의 형태(크기, 굵기 등)가 달라 발생하는 불일치를 해결하는 전처리 과정의 중요성을 깨달았습니다.

## 💡 향후 개선 계획 (Future Work)

- **알파벳 및 한글 인식**: MNIST 숫자를 넘어 EMNIST(알파벳), 나아가 직접 구축한 한글 데이터셋으로 모델을 확장하고 싶습니다.
- **모델 경량화**: 더 빠른 반응 속도를 위해 학습된 모델을 최적화하고 경량화하는 작업을 진행할 계획입니다.
- **온디바이스 AI 구현**: 학습된 모델을 `CoreML`이나 `TFLite` 형식으로 변환하여 모바일에서 직접 동작하는 애플리케이션을 개발하고 싶습니다.

## 📜 라이선스 (License)

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.

---
*이 프로젝트가 마음에 드셨다면, ⭐(Star)를 눌러주세요!*
*Made by **전양호***
