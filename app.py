from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def main_page():
    return render_template('index.html')

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# /api 엔드포인트
@app.route('/api')
def get_color():
    hex = request.args.get('hex2rgb')
    rgb = hex_to_rgb(hex)
    return jsonify({"rgb": rgb})

# /health 엔드포인트
@app.route('/health')
def health_check():
    return jsonify({"msg": "healthy"})

# /ip 엔드포인트
@app.route('/ip')
def get_ip():
    req_ip = request.remote_addr
    return jsonify({"req_ip": req_ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
