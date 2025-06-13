# 必要なライブラリをインポート
from flask import Flask, render_template  # FlaskフレームワークとHTMLテンプレート機能
from datetime import datetime  # 日時を扱うためのライブラリ
import pytz  # タイムゾーンを扱うためのライブラリ

# Flaskアプリケーションのインスタンスを作成
# __name__は現在のPythonファイルの名前を表す特殊変数
app = Flask(__name__)

def get_time_period():
    """
    現在の時間帯を判定して、対応する情報を返す関数
    
    戻り値:
        dict: 時間帯に関する情報を含む辞書
            - period: 時間帯の英語名
            - period_ja: 時間帯の日本語名
            - icon: アイコンファイル名（実際は絵文字を使用）
            - background: CSS用のグラデーション背景色
            - greeting: 時間帯に応じた挨拶
    """
    # 日本標準時（JST）のタイムゾーンオブジェクトを作成
    jst = pytz.timezone('Asia/Tokyo')
    
    # 現在の日本時間を取得し、時間（0-23）の部分だけを取り出す
    current_hour = datetime.now(jst).hour
    
    # 時間帯を判定して対応する情報を返す
    # 5時から8時未満は「朝」
    if 5 <= current_hour < 8:
        return {
            'period': 'morning',
            'period_ja': '朝',
            'icon': 'sunrise.svg',  # 実際のアプリでは絵文字を使用
            'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',  # 紫のグラデーション
            'greeting': 'おはようございます'
        }
    # 8時から12時未満は「午前」
    elif 8 <= current_hour < 12:
        return {
            'period': 'late_morning',
            'period_ja': '午前',
            'icon': 'sun.svg',
            'background': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',  # ピンクのグラデーション
            'greeting': 'おはようございます'
        }
    # 12時から17時未満は「午後」
    elif 12 <= current_hour < 17:
        return {
            'period': 'afternoon',
            'period_ja': '午後',
            'icon': 'sun-bright.svg',
            'background': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',  # 青のグラデーション
            'greeting': 'こんにちは'
        }
    # 17時から20時未満は「夕方」
    elif 17 <= current_hour < 20:
        return {
            'period': 'evening',
            'period_ja': '夕方',
            'icon': 'sunset.svg',
            'background': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',  # オレンジのグラデーション
            'greeting': 'こんばんは'
        }
    # それ以外（20時から翌5時まで）は「夜」
    else:
        return {
            'period': 'night',
            'period_ja': '夜',
            'icon': 'moon.svg',
            'background': 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',  # 淡い色のグラデーション
            'greeting': 'こんばんは'
        }

# ルート（URL）の設定
# @app.route('/') は、ブラウザで http://localhost:5000/ にアクセスしたときの処理を定義
@app.route('/')
def index():
    """
    メインページを表示する関数
    この関数は '/' にアクセスされたときに自動的に呼ばれる
    """
    # 現在の時間帯情報を取得
    time_info = get_time_period()
    
    # 日本標準時のタイムゾーンを再度取得
    jst = pytz.timezone('Asia/Tokyo')
    
    # 現在の日時を日本語形式の文字列に変換
    # strftime()は日時を指定したフォーマットの文字列に変換する関数
    # %Y=年(4桁), %m=月, %d=日, %H=時(24時間), %M=分, %S=秒
    current_time = datetime.now(jst).strftime('%Y年%m月%d日 %H:%M:%S')
    
    # HTMLテンプレートを描画して返す
    # render_template()は指定したHTMLファイルに変数を渡して描画する関数
    # time_info=time_info で、HTMLファイル内で time_info という変数名で使える
    return render_template('index.html', 
                         time_info=time_info,
                         current_time=current_time)

# Pythonファイルが直接実行されたときのみ、開発用サーバーを起動
# 他のファイルからインポートされた場合は実行されない
if __name__ == '__main__':
    # debug=True にすると、ファイルを変更したときに自動的にサーバーが再起動する
    # 本番環境では debug=False にする必要がある
    app.run(debug=True)