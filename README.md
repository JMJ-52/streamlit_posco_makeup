# OpenAI Streamlit 챗봇

`gpt-4o-mini`를 사용하는 간단한 스트리밍 챗봇입니다.

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
