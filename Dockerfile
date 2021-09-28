FROM python:3.8-slim
RUN apt-get update && apt-get install -y apache2 apache2-utils libapache2-mod-wsgi-py3 && pip install virtualenv

ADD ./config-ser.conf /etc/apache2/sites-available/000-default.conf
COPY ./walkover /root/walkover

WORKDIR /root/
RUN chown root:www-data walkover && chmod 777 walkover
WORKDIR /root/walkover
RUN mkdir error && virtualenv env && . env/bin/activate && pip install -r requirements.txt && deactivate
RUN chmod 755 /root/walkover/quiz_app && chmod 755 /root/walkover/error
EXPOSE 80 
CMD ["apache2ctl", "-D", "FOREGROUND"]