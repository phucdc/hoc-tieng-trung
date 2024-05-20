# Hoc tieng trung web

Install pip requirements:

```bash
$ pip3 install -r requirements.txt
```

Run with python flask:

```bash
$ python3 app.py
```

Or run with `gunicorn`:

```
$ gunicorn -b <ip_host>:<port> app:app
```

Or run with docker:

```bash
$ docker build -t <tag> .
$ docker run -dit --name <container_name> -p <port>:8000 <tag>
```
