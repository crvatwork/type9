FROM python:3.9.0-alpine AS scrypt

RUN apk add --update openssl-dev gcc musl-dev
RUN pip wheel --wheel-dir /whl scrypt==0.8.17


FROM python:3.9.0-alpine

COPY --from=scrypt /whl/scrypt-*.whl /whl/
COPY ./dist/Type9-*.whl /whl/
RUN python3 -m pip install /whl/scrypt-*.whl /whl/Type9-*.whl

ENTRYPOINT ["type9"]
