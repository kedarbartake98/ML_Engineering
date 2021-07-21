FROM tensorflow/tensorflow:2.6.0rc1-gpu
RUN pip3 install flask gunicorn pillow
COPY . /api		
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "api.wsgi:app"]