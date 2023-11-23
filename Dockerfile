# NOTE this is expected to be behind a proxy server

# TODO try other bases, e.g. even Alpine as this needs no dependencies

# ~1Gb Intel x64
#FROM python:3.11

# ~130Mb
FROM python:3.11-slim

# ~56Mb
#FROM alpine:3.17
#RUN apk add --no-cache python3


# no other dependencies, so no pip
# TODO consider alternative python web/wsgi server

# COPY instead of ADD for files and folders
# Only use ADD for tarballs/zips
COPY wsgidemo.py .
# TODO chmod a+x wsgidemo.py
# may need dos2unix


# TODO PORT environment variable, defaults to 8000
# Allow external connections
EXPOSE 8000

# TODO ENTRYPOINT
# TODO env PORT
# TODO use gunicorn
CMD ["python", "wsgidemo.py"]

# TODO healthcheck
