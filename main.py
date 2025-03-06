import os
import sys
import asyncio
import time
import streamlit as st
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
load_dotenv()

# システムプロンプトを含むディレクトリまでパスを通す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# llm初期化
def init_llm(llm_model: str):
    if llm_model == 'gemini':
        return ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                      api_key=os.getenv('GOOGLE_API_KEY'),
                                      temperature=0,)

    else:
        st.error(f'サポートされてないLLMモデルです: {llm_model}',icon="✖")
        time.sleep(2)
        st.rerun()

# エージェント初期化
def init_agent(query: str, llm_model: str):
    llm = init_llm(llm_model)
    controller = Controller()
    browser = Browser(config=BrowserConfig())

    return Agent(
        task=query,
        llm=llm,
        controller=controller,
        browser=browser,
        use_vision=True,
        max_actions_per_step=1,
    ), browser

async def run_agent(max_steps):
    with st.spinner(text="エージェント実行中...",show_time=True):
        result = await agent.run(max_steps=max_steps)
        # 結果表示
        st.markdown(result.final_result(),) 
    st.success("タスク完了",icon="✔️")

# Streamlit UI
st.title("Browser Agent with LLMs")
llm_model = st.radio("LLMモデル選択:", ["gemini"], index=0)
query = st.text_area(label="クエリを入力してください:", placeholder="東京の明日の天気を日本語で教えて")


if st.button(label="エージェント実行",type="primary"):
    if query =="":
        st.error("クエリを入力してください",icon="✖")
        time.sleep(2)
        st.rerun()

    if llm_model == "":
        st.error("LLMモデルを選択してください",icon="✖")
        time.sleep(2)
        st.rerun()  

    # エージェント初期化
    agent, browser = init_agent(query, llm_model)
    # エージェント実行
    asyncio.run(run_agent(25))

    