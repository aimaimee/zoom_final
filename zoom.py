import streamlit as st
import pandas as pd
from pyparsing import empty

st.set_page_config(
    page_title="줌인줌아웃",
    page_icon="📸",
    layout="wide"
)

empty1,con1,empty2 = st.columns([0.5,0.7,0.5])
empty1,con2,empty2 = st.columns([0.2,1.0,0.2])
empyt1,con3,empty2 = st.columns([0.1,1.0,0.1])
empyt1,con4,empty2 = st.columns([0.1,1.0,0.1])
empyt1,con5,con6,empty2 = st.columns([0.1,1.0,1.0,0.1])

# sidebar
with st.sidebar:
    st.markdown("## 📸줌인줌아웃📸")
    st.markdown("#### 실시간 웹캠 자리비움 탐지 보고서")

# 녹화본 파일 띄우기
def main():
    video_file = open("data/녹화_2023_01_03_14_06_34_960.mp4", "rb")
    st.video(video_file)

if __name__ == "__main__":
    main()