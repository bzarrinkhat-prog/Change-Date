from flask import Flask, request, render_template_string
import jdatetime

app = Flask(__name__)

HTML = '''
<!doctype html>
<html lang="fa">
<head>
  <meta charset="UTF-8">
  <title>تبدیل تاریخ شمسی به میلادی</title>
  <style>
    body {
      direction: rtl;
      font-family: Tahoma, sans-serif;
      text-align: center;
      margin-top: 50px;
    }
    form {
      margin-top: 30px;
    }
    input[type="text"] {
      padding: 5px 10px;
      font-size: 16px;
      text-align: center;
    }
    input[type="submit"] {
      padding: 5px 20px;
      font-size: 16px;
      margin-top: 10px;
      cursor: pointer;
    }
    h3 {
      color: green;
      margin-top: 30px;
    }
    .footer {
      margin-top: 40px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h2>تبدیل تاریخ شمسی به میلادی</h2>
  <form method="POST">
    <label>تاریخ شمسی (yyyy/mm/dd):</label><br>
    <input type="text" name="shamsi_date" placeholder="مثال: 1402/05/12" required><br>
    <input type="submit" value="تبدیل کن">
  </form>
  {% if miladi_date %}
    <h3>تاریخ میلادی معادل: {{ miladi_date }}</h3>
    <div class="footer">با تشکر از شما - بهنام زرین خط</div>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def convert():
    miladi_date = None
    if request.method == 'POST':
        shamsi_date_str = request.form.get('shamsi_date')
        try:
            year, month, day = map(int, shamsi_date_str.split('/'))
            shamsi_date = jdatetime.date(year, month, day)
            miladi_date = shamsi_date.togregorian()
        except Exception:
            miladi_date = "فرمت تاریخ صحیح نیست."
    return render_template_string(HTML, miladi_date=miladi_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
