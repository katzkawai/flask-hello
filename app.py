from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

def get_time_period():
    """現在の時間帯を判定する関数"""
    jst = pytz.timezone('Asia/Tokyo')
    current_hour = datetime.now(jst).hour
    
    if 5 <= current_hour < 8:
        return {
            'period': 'morning',
            'period_ja': '朝',
            'icon': 'sunrise.svg',
            'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            'greeting': 'おはようございます'
        }
    elif 8 <= current_hour < 12:
        return {
            'period': 'late_morning',
            'period_ja': '午前',
            'icon': 'sun.svg',
            'background': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
            'greeting': 'おはようございます'
        }
    elif 12 <= current_hour < 17:
        return {
            'period': 'afternoon',
            'period_ja': '午後',
            'icon': 'sun-bright.svg',
            'background': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
            'greeting': 'こんにちは'
        }
    elif 17 <= current_hour < 20:
        return {
            'period': 'evening',
            'period_ja': '夕方',
            'icon': 'sunset.svg',
            'background': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
            'greeting': 'こんばんは'
        }
    else:
        return {
            'period': 'night',
            'period_ja': '夜',
            'icon': 'moon.svg',
            'background': 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',
            'greeting': 'こんばんは'
        }

@app.route('/')
def index():
    time_info = get_time_period()
    jst = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(jst).strftime('%Y年%m月%d日 %H:%M:%S')
    
    return render_template('index.html', 
                         time_info=time_info,
                         current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)