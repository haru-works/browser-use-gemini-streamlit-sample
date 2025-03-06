# browser-use-gemini-streamlit-sample
browser-useをgeminiとstreamlitで動かすサンプル

## 環境設定
- windowsの場合は、wsl2をインストールし、wsl2のubuntuで動かして下さい
- wsl2 に google chormeをインストール
```bash
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo apt update
sudo apt install google-chrome-stable
```
- wsl2 に google chormeの文字化け対応
```bash
sudo apt install language-pack-ja
sudo apt install fonts-ipafont
sudo apt install fonts-ipaexfont
fc-cache -fv
```

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

## 動作デモ
https://github.com/user-attachments/assets/81f9ffaf-fd36-4d0a-a721-066a1e957902

