
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn             | cc   | isp                               | ip                                   | chatgpt          |
|---:|:---------------------|:-------------------------|:---------------|:-----|:----------------------------------|:-------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 112.29.94.23             | United Kingdom | GB   | OVH SAS                           | 2001:41d0:700:2c84::                 | Yes (Region: GB) |
|  1 | [2](config/2.json)   | 142.4.98.232             | China          | CN   | PEG-SV                            | 142.0.129.201                        | Yes (Region: US) |
|  2 | [3](config/3.json)   | 45.199.138.191           | Netherlands    | NL   | YISP B.V.                         | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba  | Yes (Region: NL) |
|  3 | [4](config/4.json)   | 45.199.138.146           | Netherlands    | NL   | YISP B.V.                         | 154.84.1.122                         | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 183.233.187.214          | Hong Kong      | HK   | CNSERVERS                         | 172.247.18.74                        | Yes (Region: US) |
|  5 | [9](config/9.json)   | bjcu.xzyunjiasu.icu      | United States  | US   | PONYNET                           | 209.141.58.10                        | Yes (Region: US) |
|  6 | [11](config/11.json) | 45.58.152.70             | Netherlands    | NL   | SHARKTECH                         | 2610:150:4000:1da:225:90ff:fea7:7db4 | Yes (Region: US) |
|  7 | [19](config/19.json) | 120.233.43.47            | Taiwan         | TW   | Data Communication Business Group | 211.20.157.213                       | Yes (Region: TW) |
|  8 | [24](config/24.json) | tg_mfbpn_d4.52vpn.eu.org | Taiwan         | TW   | Data Communication Business Group | 211.20.157.213                       | Yes (Region: TW) |

## Valid
```
vmess://eyJhZGQiOiAiMTEyLjI5Ljk0LjIzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMjFhOWJmZjItNzJkZS00ZTYyLTkzZmYtOGIxNTlmNjZkODc1IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ5MDA2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC45OC4yMzIiLCAicG9ydCI6IDQ0MywgImlkIjogIjA1MWI4NDRmLWVmZTMtNDg0Ny05MmFhLTY2YjVkZTBiNmQ0ZSIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4xMjk3MTQ3NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MTkzMTAwMzg4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE5MSIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNDIwNzcyMzAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTI4MDA5OTEzOCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNzcwZWU3MzAtMjQ1MC00ZTNjLWE2YzYtMzkzMmJkMzJhZmJkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM4MjYyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206NWM4YjIxMGEtMmYwMC00MjkyLTk2NGItMDUyODFjN2FkNWQx@bjcu.xzyunjiasu.icu:33952#github.com/freefq%20-%20%E6%B9%96%E5%8D%97%E7%9C%81%E8%81%94%E9%80%9A%209
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAiYWRkIjogIjQ1LjU4LjE1Mi43MCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNTQ5NjQ3NDUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTkiLCAiYWRkIjogIjEyMC4yMzMuNDMuNDciLCAicG9ydCI6ICIxMTAxMyIsICJpZCI6ICI4NWRiNjY1Mi1hNzQ3LTNhMGEtYTE3MC00MjI3MzYwNzY0MTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAicHpsLnAyMzc4NzUxNTUuYnV6eiIsICJhaWQiOiAwLCAiaG9zdCI6ICJwemwucDIzNzg3NTE1NS5idXp6IiwgImlkIjogIjliNzhiN2ZlLTQ3YTMtNDFlYi1kNjk1LTIyNjkyYWM4MzVhMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcHpsMjM3ODc1MTU1IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMjEiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICJwemwucDIzNzg3NTE1NS5idXp6In0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjQiLCAiYWRkIjogInRnX21mYnBuX2Q0LjUydnBuLmV1Lm9yZyIsICJwb3J0IjogIjExMDEzIiwgImlkIjogIjg1ZGI2NjUyLWE3NDctM2EwYS1hMTcwLTQyMjczNjA3NjQxMCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

