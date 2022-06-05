# curl-quiche

```
curl-quiche --http3 -Iv https://cloudflare-quic.com
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

- https://archlinux.org/packages/core/x86_64/curl/
- https://aur.archlinux.org/packages/curl-http3-msquic
