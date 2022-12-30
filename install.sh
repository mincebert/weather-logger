# install.sh
#
# run as root

for pkg in postgresql libglib2.0-dev python3-pip python3-psycopg2; do
  apt install -y $pkg
done

for pypkg in btleWeatherStation; do
  pip3 install $pkg
done

cat <<EOF -
you also need to:

1. create the database:

   $ sudo -u postgres psql
   postgres=# \i sql/postgres.sql

   $ psql weather
   weather=> \i sql/weather.sql

2. copy bin/log-weather to ~

3. install the crontab
EOF
