from flask import Flask, request, redirect, session,
 render_template_string

app 
= Flask(__name__)

@app.route('/')
def index():
    return "考试演示：Flask项目运行成功！"

if __name__ == '__main__':
    app
.run(host="0.0.0.0", port=5000, debug=True)
