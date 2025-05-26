FROM golang:alpine


RUN apk add --no-cache git nss-tools make build-base ca-certificates

COPY ./odoh-server-go/mylocal.pem /usr/local/share/ca-certificates/mylocal.pem
# COPY $(mkcert -CAROOT)/mylocal.pem /usr/local/share/ca-certificates/mylocal.pem

RUN update-ca-certificates

WORKDIR /workspace

RUN git clone https://github.com/FiloSottile/mkcert.git mkcert

# RUN git clone https://github.com/cloudflarearchive/odoh-server-go.git odoh-server
COPY ./odoh-server-go odoh-server

WORKDIR /workspace/mkcert

RUN go build -ldflags "-X main.Version=$(git describe --tags)" -o /usr/local/bin/mkcert

WORKDIR /workspace/odoh-server

RUN mkcert -key-file key.pem -cert-file cert.pem 127.0.0.1 localhost
RUN make all

CMD CERT=cert.pem KEY=key.pem PORT=4567 ./odoh-server
# CMD ["/bin/sh"]

