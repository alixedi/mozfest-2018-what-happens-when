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
        .message {
          padding: 50px;
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
    <div class="message">
        Here are some ads for that bag you have been eyeing ;)
    </div>
''')


@app.route('/')
def hello():
    name = request.cookies.get('name')
    if name:
        return base_template.substitute(
                content=result_template.substitute(
                    content=name
                )
            )
    return base_template.substitute(
            content=result_template.substitute(
                content="Anonymous"
            )
        )

