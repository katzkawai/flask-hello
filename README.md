# 時間帯で変化するFlaskアプリ

このアプリは、現在の時間帯に応じて背景色とアイコンが自動的に変化するWebアプリケーションです。

## 機能

- **時間帯の自動検出**: 日本時間（JST）で現在の時間を確認し、適切な時間帯を判定します
- **動的な背景変更**: 時間帯ごとに美しいグラデーション背景が表示されます
- **時間帯別の挨拶**: 朝は「おはようございます」、午後は「こんにちは」など、時間に応じた挨拶を表示
- **自動更新**: 60秒ごとにページが自動更新され、常に最新の時間が表示されます

### 時間帯の設定

| 時間帯 | 時間 | 背景色 | アイコン | 挨拶 |
|--------|------|--------|----------|------|
| 朝 | 5:00 - 7:59 | 紫のグラデーション | 🌅 | おはようございます |
| 午前 | 8:00 - 11:59 | ピンクのグラデーション | ☀️ | おはようございます |
| 午後 | 12:00 - 16:59 | 青のグラデーション | 🌞 | こんにちは |
| 夕方 | 17:00 - 19:59 | オレンジのグラデーション | 🌆 | こんばんは |
| 夜 | 20:00 - 4:59 | 淡い色のグラデーション | 🌙 | こんばんは |

## 必要な環境

- Python 3.7以上
- pip（Pythonパッケージ管理ツール）

## インストール方法

### 1. リポジトリのクローン（またはダウンロード）

```bash
git clone [リポジトリのURL]
cd flask-hello
```

### 2. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

このコマンドで以下のパッケージがインストールされます：
- Flask: Webアプリケーションフレームワーク
- pytz: タイムゾーン処理ライブラリ

## 起動方法

### 1. アプリケーションの起動

```bash
python app.py
```

### 2. ブラウザでアクセス

起動後、以下のメッセージが表示されます：
```
* Running on http://127.0.0.1:5000
```

ブラウザを開いて `http://localhost:5000` にアクセスしてください。

## 使い方

1. ブラウザでアプリにアクセスすると、現在の時間帯に応じた画面が表示されます
2. 画面には以下の情報が表示されます：
   - 時間帯を表すアイコン（絵文字）
   - 時間に応じた挨拶メッセージ
   - 現在の時間帯（日本語）
   - 現在の日時
3. ページは60秒ごとに自動更新されるので、時間帯が変わると画面も自動的に切り替わります

## ファイル構成

```
flask-hello/
├── app.py              # メインのアプリケーションファイル
├── requirements.txt    # 必要なパッケージのリスト
├── README.md          # このファイル
└── templates/
    └── index.html     # HTMLテンプレート
```

## トラブルシューティング

### ポート5000が使用中の場合

他のアプリケーションがポート5000を使用している場合は、`app.py`の最後の行を以下のように変更してください：

```python
app.run(debug=True, port=8000)  # 8000番ポートで起動
```

### パッケージのインストールでエラーが出る場合

仮想環境を使用することをお勧めします：

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化（Windows）
venv\Scripts\activate

# 仮想環境の有効化（Mac/Linux）
source venv/bin/activate

# パッケージのインストール
pip install -r requirements.txt
```

## カスタマイズ・改造のヒント

### 1. 時間帯の変更

`app.py`の`get_time_period()`関数内で時間帯の設定を変更できます。

**例1: 時間帯を細かく分ける**
```python
elif 6 <= current_hour < 7:
    return {
        'period': 'dawn',
        'period_ja': '夜明け',
        'icon': '🌄',
        'background': 'linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%)',
        'greeting': 'おはようございます'
    }
```

**例2: 季節に応じた時間帯設定**
```python
from datetime import date

def get_season():
    month = date.today().month
    if month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    # ... 以下略
```

### 2. デザインの変更

`templates/index.html`のCSSセクションで、色やアニメーションなどのデザインを変更できます。

**例1: アニメーションの変更**
```css
@keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.time-icon {
    animation: rotate 10s linear infinite;
}
```

**例2: レスポンシブデザインの改善**
```css
@media (max-width: 600px) {
    .greeting {
        font-size: 1.8rem;
    }
    .container {
        padding: 2rem;
    }
}
```

### 3. 新機能の追加アイデア

#### A. 天気情報の表示
```python
# OpenWeatherMap APIなどを使用
import requests

def get_weather():
    api_key = "YOUR_API_KEY"
    city = "Tokyo"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    # ... 天気データの処理
```

#### B. BGM機能の追加
```html
<!-- index.html に追加 -->
<audio id="bgm" loop>
    <source src="{{ url_for('static', filename='music/' + time_info.period + '.mp3') }}" type="audio/mpeg">
</audio>

<button onclick="document.getElementById('bgm').play()">🎵 BGMを再生</button>
```

#### C. ユーザーの位置情報に基づく日の出・日没時刻の取得
```javascript
// JavaScriptで位置情報を取得
navigator.geolocation.getCurrentPosition(function(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    // サーバーに送信して日の出・日没時刻を計算
});
```

### 4. データベース連携

#### A. 訪問履歴の記録
```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visits.db'
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    time_period = db.Column(db.String(50))
```

#### B. メッセージボード機能
```python
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    time_period = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

### 5. 多言語対応

```python
# 言語設定の追加
LANGUAGES = {
    'ja': {
        'morning': {'greeting': 'おはようございます', 'period': '朝'},
        'afternoon': {'greeting': 'こんにちは', 'period': '午後'},
        # ...
    },
    'en': {
        'morning': {'greeting': 'Good morning', 'period': 'Morning'},
        'afternoon': {'greeting': 'Good afternoon', 'period': 'Afternoon'},
        # ...
    }
}

@app.route('/<lang>')
def index_with_lang(lang='ja'):
    # 言語に応じた表示
```

### 6. パフォーマンスの改善

#### A. キャッシュの実装
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.cached(timeout=60)  # 60秒間キャッシュ
def get_time_period():
    # ...
```

#### B. 非同期更新
```javascript
// 自動更新をAjaxに変更
setInterval(async () => {
    const response = await fetch('/api/time-info');
    const data = await response.json();
    updateUI(data);
}, 60000);
```

### 7. セキュリティの強化

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
```

### 8. テーマ機能の実装

```javascript
// ローカルストレージを使用したテーマ保存
function setTheme(theme) {
    localStorage.setItem('theme', theme);
    document.body.className = theme;
}

// ダークモード対応
const darkModeBtn = document.createElement('button');
darkModeBtn.textContent = '🌓';
darkModeBtn.onclick = () => toggleDarkMode();
```

これらの改造を組み合わせることで、より高機能で魅力的なアプリケーションに発展させることができます。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。