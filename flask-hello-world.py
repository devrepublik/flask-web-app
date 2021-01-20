from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello-students')
def hello_world_students():
    return 'Hello, World, Sudentes!'


@app.route('/sqr/<x>')
def hello_world_params(x):
    x = int(x)
    return f'sqr({x}) = {x**2}'


@app.route('/sum')
def sum_args():
    args = [int(v) for v in request.args.values()]
    sum_str = " + ".join([str(v) for v in args])
    return f"{sum_str} = {sum(args)}"


if __name__ == "__main__":
    app.run()
