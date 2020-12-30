FROM python:3.9.1-alpine AS builder

RUN apk add --update openssl-dev gcc musl-dev
RUN pip wheel --wheel-dir /whl scrypt==0.8.17

WORKDIR /build
COPY . .
RUN python3 setup.py bdist_wheel && cp dist/Type9-*.whl /whl/


FROM python:3.9.1-alpine

COPY --from=builder /whl/scrypt-*.whl /whl/Type9*.whl /whl/
RUN python3 -m pip install /whl/scrypt-*.whl /whl/Type9-*.whl
RUN rm -rf /whl

ENTRYPOINT ["type9"]
