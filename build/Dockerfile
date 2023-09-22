FROM python:3.7-buster

EXPOSE 8888

RUN apt-get install graphviz

RUN useradd -ms /bin/bash jupuser
USER jupuser

ENV PATH="/home/jupuser/.local/bin:${PATH}"

ADD ./build/requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN pip install jupyterlab

COPY --chown=jupuser:jupuser ./build/jupyter_notebook_config.json /home/jupuser/.jupyter/jupyter_notebook_config.json

WORKDIR /home/jupuser/

CMD ["bash", "-c", "jupyter lab --notebook-dir /home/jupuser/  --ip 0.0.0.0 --no-browser --allow-root"]
