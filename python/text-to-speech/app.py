import io
import os
import streamlit as st
import openai

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Text to Speech")

client = OpenAI()


def stream_and_play(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    # OpenAI APIのレスポンスから直接バイナリコンテンツを使用
    audio_bytes = response.content
    return audio_bytes


# Streamlitウィジェットのセットアップ
if __name__ == "__main__":
    text = st.text_area("テキストを入力してください:", height=300)
    if st.button("再生"):
        audio_bytes = stream_and_play(text)
        st.audio(audio_bytes, format="audio/mp3")
