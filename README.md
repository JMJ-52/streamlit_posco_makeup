# 화장품 영업 데이터 분석 Streamlit 앱

챗봇 모델은 `gpt-4o-mini`로 고정되어 있습니다.

## Streamlit Community Cloud Secrets

앱의 Settings → Secrets에 다음 내용을 등록하세요.

```toml
OPENAI_API_KEY = "sk-..."
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = "587"
SMTP_USER = "보내는메일@gmail.com"
SMTP_PASSWORD = "앱비밀번호"
```

## 로컬 실행

1. 가상환경을 만들고 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

2. `.streamlit/secrets.toml.example`을 `.streamlit/secrets.toml`로 복사하고 API 키를 입력합니다.

3. 앱을 실행합니다.

```bash
streamlit run app.py
```

## Streamlit Community Cloud 배포

앱의 **Settings → Secrets**에 아래 내용을 등록하세요.

```toml
OPENAI_API_KEY = "sk-..."
```

API 키는 소스 코드나 GitHub 저장소에 직접 넣지 않습니다.
