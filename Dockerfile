FROM python:3 

RUN pip install --no-cache-dir dnslib
ADD dns.py ./

EXPOSE 53
ENV PYTHONUNBUFFERED 1

CMD ["python", "dns.py"]
