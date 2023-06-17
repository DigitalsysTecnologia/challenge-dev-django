FROM python:3.8
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
RUN apt-get update && apt-get install -y \
    wget \
    sudo  \
    curl  \
    gnupg2 -y \
    nano \
    && rm -rf /var/lib/apt/lists/* \

ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000

