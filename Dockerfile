FROM python:3.6.7
ENV JOBNAME='powershell-scheduler'
WORKDIR /opt/power-scheduler
COPY ./power-scheduler ./power-scheduler
COPY ./requirements.txt ./
COPY ./app.py ./
COPY ./Script_ProcessTabularModel.ps1 ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pyinstaller && \
    pip install pex

RUN python app.py
RUN pex setuptools ./power-scheduler -e power_scheduler -o ${JOBNAME}.pex
RUN pyinstaller power-scheduler/power_scheduler/__main__.py -F -n powershell-scheduler.exe