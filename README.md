
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn             | cc   | isp                     | ip                                  | chatgpt          |
|---:|:---------------------|:-------------------------|:---------------|:-----|:------------------------|:------------------------------------|:-----------------|
|  0 | [5](config/5.json)   | 112.29.94.23             | United Kingdom | GB   | OVH SAS                 | 2001:41d0:700:2c84::                | Yes (Region: GB) |
|  1 | [6](config/6.json)   | 45.199.138.191           | Netherlands    | NL   | YISP B.V.               | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |
|  2 | [13](config/13.json) | 45.199.138.146           | Netherlands    | NL   | YISP B.V.               | 154.84.1.122                        | Yes (Region: NL) |
|  3 | [14](config/14.json) | 156.225.67.155           | Netherlands    | NL   | YISP B.V.               | 154.84.1.193                        | Yes (Region: NL) |
|  4 | [16](config/16.json) | tg_mfbpn_d4.52vpn.eu.org | Hong Kong      | HK   | Vertex Connectivity LLC | 23.158.104.201                      | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggNSIsICJhZGQiOiAiMTEyLjI5Ljk0LjIzIiwgInBvcnQiOiAiNDkwNTYiLCAiaWQiOiAiMjFhOWJmZjItNzJkZS00ZTYyLTkzZmYtOGIxNTlmNjZkODc1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA2IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE5MSIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNDIwNzcyMzAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTI4MDA5OTEzOCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMyIsICJhZGQiOiAiNDUuMTk5LjEzOC4xNDYiLCAicG9ydCI6ICIzMDAwMCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgImFpZCI6ICI2NCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcGF0aC8xNjk5MTkzMTAwMzg4IiwgImhvc3QiOiAid3d3LjE5MjI5MzYyLnh5eiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE0IiwgImFkZCI6ICIxNTYuMjI1LjY3LjE1NSIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xMTMwMjg1MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5NTM0ODc2MjgwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTYiLCAiYWRkIjogInRnX21mYnBuX2Q0LjUydnBuLmV1Lm9yZyIsICJwb3J0IjogIjExMDA1IiwgImlkIjogIjg1ZGI2NjUyLWE3NDctM2EwYS1hMTcwLTQyMjczNjA3NjQxMCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

