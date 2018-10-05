
uwsgi --http :8000 --wsgi-file api/app.py --callable api
python api/models.py