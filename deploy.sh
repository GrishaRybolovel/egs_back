#!bin/bash
set -e

cd /home/django/egs_back

echo "Deployment started"
git pull origin master

source /home/django/egs_back/env/bin/activate

pip install -r requirements.txt

python manage.py collectstatic --noinput

python manage.py makemigrations
python manage.py migrate

deactivate

sudo systemctl restart gunicorn

