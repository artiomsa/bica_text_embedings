FROM python:3.8
WORKDIR /code
RUN pip install --upgrade pip==22.3.1
RUN pip install -U sentence-transformers && pip install fastapi && pip install pydantic && pip install uvicorn && pip install numpy
COPY ./main.py /code/
# RUN uvicorn main:app --port 8888 --reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]
