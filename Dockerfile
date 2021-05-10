FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3","al_auto.py" ]

# CMD [ "python",  "main.py", "--config_tag",  "fwa",  "--base_record", "42",  "--max_records", "10000",  "--log_directory", "/tmp" ]
CMD [ "--config_tag",  "xl_auto"  ]