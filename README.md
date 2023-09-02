
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                              | cn            | cc   | isp                               | ip                          | chatgpt          |
|---:|:---------------------|:----------------------------------------------------------------------------------|:--------------|:-----|:----------------------------------|:----------------------------|:-----------------|
|  0 | [3](config/3.json)   | 45.199.138.162                                                                    | Netherlands   | NL   | YISP B.V.                         | 154.84.1.230                | Yes (Region: NL) |
|  1 | [4](config/4.json)   | gamespeed-gateway-1.numastergame.com                                              | Taiwan        | TW   | Data Communication Business Group | 61.219.15.82                | Yes (Region: TW) |
|  2 | [8](config/8.json)   | s1225.v2line.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland        | PL   | OVH SAS                           | 54.36.174.181               | Yes (Region: FR) |
|  3 | [10](config/10.json) | 172.64.153.211                                                                    | Sweden        | SE   | Stark Industries Solutions Ltd    | 94.131.115.68               | Yes (Region: SE) |
|  4 | [14](config/14.json) | 45.92.161.173                                                                     | United States | US   | DEDIPATH-LLC                      | 45.83.117.170               | Yes (Region: US) |
|  5 | [16](config/16.json) | pzl.p237875155.buzz                                                               | United States | US   | CLOUDFLARENET                     | 2a09:bac5:80cd:1246::1d2:95 | Yes (Region: US) |
|  6 | [18](config/18.json) | ci.outline-vpn.cloud                                                              | United States | US   | SHARKTECH                         | 67.21.72.34                 | Yes (Region: US) |
|  7 | [19](config/19.json) | scw-fr.iiio.wiki                                                                  | France        | FR   | CLOUDFLARENET                     | 2a09:bac5:3264:be::13:288   | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI2NWVhNjcyNy00NDYxLTQ3YTctYTVjNC1mZWYyYzY3ZjJmNzkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzI2NjEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwOTEzYjFhYy0xZjZjLTQzNmItOTliNC1hNWQ2ZTM0M2QwMjUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTE4NzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInMxMjI1LnYybGluZS5mcjg2Nzg4MjUzMjQyNDdiODE3NmQ1OWY4M2MzMGJkOTRkMjNkMmUzYWM1Y2Q0YTc0M2Jrd3FlaWt2ZHl1ZnIuY3lvdSIsICJwb3J0IjogODAsICJpZCI6ICIwYmFhZjAxNC1hZjA0LTQwMjgtYmU1My1mNWM3NWJiMjc2YWUiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInMxMjI1LnYybGluZS5mcjg2Nzg4MjUzMjQyNDdiODE3NmQ1OWY4M2MzMGJkOTRkMjNkMmUzYWM1Y2Q0YTc0M2Jrd3FlaWt2ZHl1ZnIuY3lvdSIsICJwYXRoIjogIi92bWVzcyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4yMTEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAic2NoZXJlc3dlZC5zb2Z0d2FyZW5ld3Muc3RvcmUiLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkwMSIsICJwb3J0IjogIjQ0MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTAiLCAic2N5IjogImF1dG8iLCAic25pIjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiNDUuOTIuMTYxLjE3MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNDQ2OSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2YjI3XHU3NmRmICAxNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICJwemwucDIzNzg3NTE1NS5idXp6IiwgInBvcnQiOiAiNDQzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5Yjc4YjdmZS00N2EzLTQxZWItZDY5NS0yMjY5MmFjODM1YTAiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3B6bDIzNzg3NTE1NSIsICJob3N0IjogInB6bC5wMjM3ODc1MTU1LmJ1enoiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiY2kub3V0bGluZS12cG4uY2xvdWQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDE4IiwgInBvcnQiOiA0MzEyMywgImlkIjogIjI1NjZkMDBmLTIxOGMtNDhmNy05YTM2LTEzZDNkNmYxYTcyNCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE5IiwgImFkZCI6ICJzY3ctZnIuaWlpby53aWtpIiwgInBvcnQiOiAiMjA4MiIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjUwZjQzMzEtOGMzZS00Yjg3LWE4NmItNWM1ZmJmOWRkYmE4IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgImhvc3QiOiAic2N3LWZyLmlpaW8ud2lraSIsICJ0bHMiOiAiIn0=
```

