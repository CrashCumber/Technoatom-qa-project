FROM python:3.6

COPY ./vk_api /vk_api
RUN pip install -r /vk_api/requirements.txt

COPY ./vk_api/vk_api_mock.py ./vk_api

CMD ["python", "vk_api/vk_api_mock.py"]

