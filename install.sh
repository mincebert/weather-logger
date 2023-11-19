# install.sh
#
# run as root

for pkg in postgresql libglib2.0-dev python3-pip python3-psycopg2; do
  apt install -y $pkg
done

for pypkg in btleWeatherStation; do
  pip3 install $pypkg
done

cat <<EOF -
you also need to:

1. create the database:

   $ sudo -u postgres psql
   postgres=# \i database/postgres.sql

   $ psql -h localhost weather weather_admin
   weather=> \i database/weather.sql

2. copy weather-log to ~/bin

3. install the crontab
EOF
