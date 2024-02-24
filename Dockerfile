FROM rasa/rasa:3.6.14-full 
USER root
RUN pip install --upgrade pip
RUN pip install pandas
