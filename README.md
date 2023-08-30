
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp                                      | ip                                 | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------------------------------------|:-----------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 23.234.198.86  | United States | US   | MULTA-ASN1                               | 2607:f130:109:0:225:90ff:fe79:7d34 | Yes (Region: US) |
|  1 | [5](config/5.json)   | 111.6.86.76    | Japan         | JP   | Akamai Connected Cloud                   | 172.104.76.30                      | Yes (Region: JP) |
|  2 | [6](config/6.json)   | 45.199.138.182 | Netherlands   | NL   | YISP B.V.                                | 154.84.1.229                       | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 104.17.61.17   | Poland        | PL   | OVH SAS                                  | 54.36.174.181                      | Yes (Region: FR) |
|  4 | [10](config/10.json) | 156.225.67.78  | Netherlands   | NL   | YISP B.V.                                | 46.182.107.216                     | Yes (Region: NL) |
|  5 | [26](config/26.json) | 13.wyhkaa0.gq  | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 45.137.97.241                      | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImE5YWJmM2U3LTg3ZjQtNDczZC04ZDAzLTJmMjZjYTRiMzU4MyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNDg4OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZjYjNcdTUzNTdcdTc3MDFcdTZkMWJcdTk2MzNcdTVlMDJcdTc5ZmJcdTUyYTggNSIsICJhZGQiOiAiMTExLjYuODYuNzYiLCAicG9ydCI6ICIyMTUxMCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNGFhYzlkYzEtNDI4NS0zNGI5LWI0ODYtMzA5OWRhOTE3ZWFiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAidWswMS5ja2Nsb3VkLmluZm8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xODIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJkMzEzMzQ4NC1mMmJmLTRiMGMtOGQzOC1mOGU2NDViNjU2ODciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzEzOTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTA0LjE3LjYxLjE3IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogInVzLW1pYW1pLmJpcWliYW8uc2l0ZSIsICJpZCI6ICJhN2NhM2U5ZC0zNzYxLTQyN2EtOWJiNi1mZWQzZWVlN2JjOTMiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3B1YmxpYz9lZD00MDk2IiwgInBvcnQiOiAiMjA1MiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny43OCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNlMDE2YzRkLTk4NmUtNDJkZi04MzhjLTYwNDZmM2Q4OWVjZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Mzg1MSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAxMCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI2IiwgImFkZCI6ICIxMy53eWhrYWEwLmdxIiwgInBvcnQiOiAiMjA5NSIsICJpZCI6ICIzMmFmNDAwNi0wNjk4LTQ5MTAtODA2Yy1iODEzMDc0ZjM2ZWIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIjEzLnd5aGthYTAuZ3EiLCAicGF0aCI6ICIvVEc6QGhrYWEwIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

