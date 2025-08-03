from flask import Flask, request, render_template_string
import jdatetime

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>تبدیل تاریخ شمسی به میلادی</title>
<h2>تبدیل تاریخ شمسی به میلادی</h2>
<form method="POST">
  <label>تاریخ شمسی (yyyy/mm/dd):</label>
  <input type="text" name="shamsi_date" placeholder="مثال: 1402/05/12" required>
  <input type="submit" value="تبدیل کن">
</form>
{% if miladi_date %}
  <h3>تاریخ میلادی معادل: {{ miladi_date }}</h3>
{% endif %}
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
        except Exception as e:
            miladi_date = "فرمت تاریخ صحیح نیست."
    return render_template_string(HTML, miladi_date=miladi_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
