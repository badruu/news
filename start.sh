export NEWS_API_KEY='d2b77818e9674bfd91dc2114b7540de0'
# export SECRET_KEY='badar110'

gunicorn --timeout 120 --workers 3
python3.7 manage.py server


