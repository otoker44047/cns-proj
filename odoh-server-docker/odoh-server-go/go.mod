module github.com/cloudflare/odoh-server-go

// +heroku goVersion go1.14
// +scalingo goVersion go1.14
go 1.23.0

toolchain go1.24.2

require (
	cloud.google.com/go/logging v1.1.1
	github.com/cisco/go-hpke v0.0.0-20210215210317-01c430f1f302
	github.com/cloudflare/odoh-go v1.0.0
	github.com/elastic/go-elasticsearch/v8 v8.0.0-20201022194115-1af099fb3eca
	github.com/miekg/dns v1.1.35
)

require (
	cloud.google.com/go v0.70.0 // indirect
	git.schwanenlied.me/yawning/x448.git v0.0.0-20170617130356-01b048fb03d6 // indirect
	github.com/cisco/go-tls-syntax v0.0.0-20200617162716-46b0cfb76b9b // indirect
	github.com/cloudflare/circl v1.0.0 // indirect
	github.com/golang/groupcache v0.0.0-20200121045136-8c9f03a8e57e // indirect
	github.com/golang/protobuf v1.4.3 // indirect
	github.com/google/go-cmp v0.6.0 // indirect
	github.com/googleapis/gax-go/v2 v2.0.5 // indirect
	github.com/jstemmer/go-junit-report v0.9.1 // indirect
	go.opencensus.io v0.22.5 // indirect
	golang.org/x/crypto v0.38.0 // indirect
	golang.org/x/lint v0.0.0-20200302205851-738671d3881b // indirect
	golang.org/x/mod v0.17.0 // indirect
	golang.org/x/net v0.40.0 // indirect
	golang.org/x/oauth2 v0.0.0-20200902213428-5d25da1a8d43 // indirect
	golang.org/x/sync v0.14.0 // indirect
	golang.org/x/sys v0.33.0 // indirect
	golang.org/x/text v0.25.0 // indirect
	golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d // indirect
	google.golang.org/api v0.33.0 // indirect
	google.golang.org/appengine v1.6.6 // indirect
	google.golang.org/genproto v0.0.0-20201019141844-1ed22bb0c154 // indirect
	google.golang.org/grpc v1.32.0 // indirect
	google.golang.org/protobuf v1.25.0 // indirect
)
