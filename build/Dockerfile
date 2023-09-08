FROM python:3.7-buster

ADD ./build/requirements.txt /requirements.txt
ADD ./build/snippets_nbextensions.json /snippets_nbextensions.json
RUN pip install -r requirements.txt
RUN pip install jupyter jupyter-http-over-ws bokeh

EXPOSE 8888

RUN useradd -ms /bin/bash jupuser
USER jupuser

# copy notebook config
COPY --chown=jupuser:jupuser ./build/jupyter_notebook_config.json /home/jupuser/.jupyter/jupyter_notebook_config.json

ENV PATH="/home/jupuser/.local/bin:${PATH}"

# install nbextensions
RUN pip install jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user

# enable nbextensions
RUN jupyter nbextension enable contrib_nbextensions_help_item/main
RUN jupyter nbextension enable autosavetime/main
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable code_font_size/code_font_size
RUN jupyter nbextension enable code_prettify/code_prettify
RUN jupyter nbextension enable collapsible_headings/main
RUN jupyter nbextension enable comment-uncomment/main
RUN jupyter nbextension enable equation-numbering/main
RUN jupyter nbextension enable execute_time/ExecuteTime
RUN jupyter nbextension enable spellchecker/main
RUN jupyter nbextension enable toggle_all_line_numbers/main
RUN jupyter nbextension enable table_beautifier/main
RUN jupyter nbextension enable toc2/main
RUN jupyter nbextension enable snippets/main

RUN cp /snippets_nbextensions.json $(jupyter --data-dir)/nbextensions/snippets/snippets.json

WORKDIR /home/jupuser/

CMD ["bash", "-c", "jupyter notebook --notebook-dir /home/jupuser/  --ip 0.0.0.0 --no-browser --allow-root"]
