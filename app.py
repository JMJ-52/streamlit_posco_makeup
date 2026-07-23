import streamlit as st
from openai import OpenAI


MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = "당신은 친절하고 정확한 한국어 AI 어시스턴트입니다. 필요한 경우 단계별로 설명하세요."


st.set_page_config(
    page_title="OpenAI 챗봇",
    page_icon="💬",
    layout="centered",
)

st.title("💬 OpenAI 챗봇")
st.caption(f"OpenAI API · {MODEL}")


def get_api_key() -> str | None:
    """Streamlit Community Cloud Secrets 또는 로컬 secrets에서 API 키를 읽습니다."""
    try:
        return st.secrets["OPENAI_API_KEY"]
    except (KeyError, FileNotFoundError):
        return None


api_key = get_api_key()
if not api_key:
    st.error("OPENAI_API_KEY가 설정되지 않았습니다.")
    st.info(
        "Streamlit Community Cloud의 Settings → Secrets에 "
        '`OPENAI_API_KEY = "sk-..."`를 추가한 뒤 앱을 다시 실행하세요.'
    )
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.subheader("설정")
    st.write(f"모델: `{MODEL}`")
    if st.button("대화 초기화", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    api_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *st.session_state.messages,
    ]

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        streamed_text = ""
        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=api_messages,
                temperature=0.7,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    streamed_text += delta
                    response_placeholder.markdown(streamed_text + "▌")
            response_placeholder.markdown(streamed_text)
        except Exception as error:
            response_placeholder.error(f"응답을 생성하지 못했습니다: {error}")
            streamed_text = "오류가 발생해 응답을 생성하지 못했습니다."

    st.session_state.messages.append(
        {"role": "assistant", "content": streamed_text}
    )
