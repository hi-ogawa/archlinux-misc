# curl-quiche

```
$ curl-quiche -V
curl 7.84.0-DEV (x86_64-pc-linux-gnu) libcurl/7.84.0-DEV BoringSSL zlib/1.2.12 brotli/1.0.9 zstd/1.5.2 libidn2/2.3.2 libpsl/0.21.1 (+libidn2/2.3.0) libssh2/1.10.0 nghttp2/1.47.0 quiche/0.14.0 librtmp/2.3
Release-Date: [unreleased]
Protocols: dict file ftp ftps gopher gophers http https imap imaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTP3 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM NTLM_WB PSL SPNEGO SSL UnixSockets zstd

$ curl-quiche --http3 -Iv https://cloudflare-quic.com
*   Trying 2606:4700:10::6816:826:443...
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: none
* Connect socket 5 over QUIC to 2606:4700:10::6816:826:443
* Sent QUIC client Initial, ALPN: h3,h3-29,h3-28,h3-27
*  subjectAltName: host "cloudflare-quic.com" matched cert's "cloudflare-quic.com"
* Verified certificate just fine
* Connected to cloudflare-quic.com () port 443 (#0)
* h2h3 [:method: HEAD]
* h2h3 [:path: /]
* h2h3 [:scheme: https]
* h2h3 [:authority: cloudflare-quic.com]
* h2h3 [user-agent: curl/7.84.0-DEV]
* h2h3 [accept: */*]
* Using HTTP/3 Stream ID: 0 (easy handle 0x563304484900)
> HEAD / HTTP/3
> Host: cloudflare-quic.com
> user-agent: curl/7.84.0-DEV
> accept: */*
>
< HTTP/3 200
HTTP/3 200
< date: Sun, 05 Jun 2022 04:56:18 GMT
date: Sun, 05 Jun 2022 04:56:18 GMT
< content-type: text/html
content-type: text/html
< content-length: 109425
content-length: 109425
< expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
< server: cloudflare
server: cloudflare
< cf-ray: 7166522afe1ab015-NRT
cf-ray: 7166522afe1ab015-NRT
< alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
* Connection #0 to host cloudflare-quic.com left intact
```

## references

- https://github.com/curl/curl/blob/2bd75e5686b2e6ff3824c4dfb2b6ec86b60f454c/docs/HTTP3.md
- https://archlinux.org/packages/core/x86_64/curl/
- https://aur.archlinux.org/packages/curl-http3-msquic
