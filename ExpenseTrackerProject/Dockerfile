# pull official base image
FROM python:3.11.4-slim-buster AS build

# set work directory
WORKDIR /usr/src/ExpenseTrackerProject

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc


# lint
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
COPY . /usr/src/ExpenseTrackerProject
RUN flake8 --ignore=E501,F401 .

# copy python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/ExpenseTrackerProject/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.11.4-slim-buster AS run

# create directory for the app user
RUN mkdir -p /home/expensetracker

# create the app user
RUN addgroup --system expensetracker && adduser --system --group expensetracker

# create the appropriate directories
ENV HOME=/home/expensetracker
ENV APP_HOME=/home/expensetracker/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=build /usr/src/ExpenseTrackerProject/wheels /wheels
COPY --from=build /usr/src/ExpenseTrackerProject/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
COPY ./entrypoint.prod.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
RUN chmod +x  $APP_HOME/entrypoint.prod.sh

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R expensetracker:expensetracker $APP_HOME

# change to the app user
USER expensetracker

# run entrypoint.prod.sh
ENTRYPOINT ["/home/expensetracker/web/entrypoint.prod.sh"]