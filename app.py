from flask import Flask, render_template
import pandas as pd

# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     # 读取CSV文件
#     df = pd.read_csv('data.csv')
#     # 将DataFrame转换为HTML表格
#     table = df.to_html(index=False)
#     return render_template('index.html', table=table)


from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# 假设你的数据文件是CSV格式
df = pd.read_excel('predict_week7_new_20241005.xlsx')

@app.route('/')
def index():
    return render_template('index.html', data=df.to_json(orient='records'))

@app.route('/data')
def data():
    selected_date = request.args.get('date')
    if selected_date:
        # 过滤数据
        filtered_df = df[df['预测日期'] == selected_date]
        return jsonify(filtered_df.to_dict(orient='records'))
    else:
        return jsonify(df.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)