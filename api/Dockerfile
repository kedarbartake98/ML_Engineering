FROM tensorflow/tensorflow:2.2.3-py3
RUN pip3 install flask gunicorn pillow
COPY . /api
COPY ../model/mnist_cnn.h5 /model/
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "api.wsgi:app"]