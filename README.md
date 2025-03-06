# browser-use-gemini-streamlit-sample
browser-useをgeminiとstreamlitで動かすサンプル

## 環境設定
- windowsの場合は、wsl2をインストールし、wsl2のubuntuで動かして下さい

- githubからbrowser-use-gemini-streamlit-sampleをコピー
```bash
git clone https://github.com/haru-works/browser-use-gemini-streamlit-sample.git
```
- フォルダ移動
```bash
cd browser-use-gemini-streamlit-sample
```
- pythonの仮想環境作る(python 3.11.xx以上)
  
- pip で browser-useを入れる
```bash
pip install browser-use
```
- install playwright:
```bash
playwright install
```
- ライブラリインストール
```bash
pip install -r requirements.txt
```
- .env_sampleをコピーして.env作る
```bash
cp .env_sample .env
```
- .envを開いて環境変数の編集
```bash
GOOGLE_API_KEY=ここにGeminiのAPIキーセット
```
※Geminiの設定方法は、[こちら](https://ai.google.dev/gemini-api/docs?hl=ja)からやってね

- アプリ起動
```bash
streamlit run main.py
```

  
