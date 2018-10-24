from string import Template
from subprocess import check_output

from flask import Flask, request


app = Flask(__name__)

base_template = Template('''
<!doctype html>
<head>
    <style>
        html, body {
          height: 100%;
        }
        .flex-container {
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        form, input, textarea {
          font-family: monospace;
        }
        form, input {
          font-size: 40px;
        }
        input, textarea {
          border-style: solid;
          border-width: 2px;
          padding: 10px;
          border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="flex-container">
        $content
    </div>
</body>
''')

result_template = Template('''
    <textarea rows="40" cols="80">
        $content
    <textarea>
''')

form = '''
        <form action="." method="post">
            $ dig <input type="text" name="dig">
        </form>
'''

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return base_template.substitute(content=form)
    else:
        cli = 'dig ' + request.form.get('dig')
        result = check_output(cli.split())
        return base_template.substitute(
            content=result_template.substitute(
                content=result.decode('utf-8')
            )
        )

