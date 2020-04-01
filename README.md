## Simple Flask Template

A simple skeleton Flask template

### Local development

```sh
python -m venv env
source env/bin/activate
pip install -e .
export FLASK_ENV=development
flask run
```

- http://localhost:5000

### Running with uWSGI

Install `uwsgi` with `pip`  

```shell script
pip install uwsgi
```

Run

```sh
uwsgi app.ini
```

- http://localhost:8080

### Running with Docker

```sh
docker build -t flaskapp .
docker run -p 8080:8080 flaskapp
```

- http://localhost:8080