from string import Template

from flask import Flask, request, make_response


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
        form, input, .hello {
          font-family: monospace;
        }
        form, input, .hello {
          font-size: 40px;
        }
        input {
          border-style: solid;
          border-width: 2px;
          padding: 10px;
          border-radius: 5px;
        }
        .name {
          background-color: yellow;
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
    <div class="hello">
        Hello, <span class="name">$content</span>!
    </div>
''')

form = '''
        <form action="." method="post">
            Write your name: <input type="text" name="name">
        </form>
'''


@app.route('/', methods=('GET', 'POST'))
def hello():
    if request.method == 'GET':
        return base_template.substitute(content=form)
    else:
        name = request.form.get('name')
        return base_template.substitute(
            content=result_template.substitute(
                content=name
            )
        )
