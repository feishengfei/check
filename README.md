
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp           | ip                                 | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:--------------|:-----------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.24.213   | United States | US   | SHARKTECH     | 170.178.189.58                     | Yes (Region: US) |
|  1 | [3](config/3.json)   | 173.82.67.195  | United States | US   | MULTA-ASN1    | 23.234.230.34                      | Yes (Region: US) |
|  2 | [4](config/4.json)   | 23.225.211.21  | United States | US   | CNSERVERS     | 23.225.57.210                      | Yes (Region: US) |
|  3 | [5](config/5.json)   | 64.32.21.246   | United States | US   | SHARKTECH     | 107.167.24.162                     | Yes (Region: US) |
|  4 | [6](config/6.json)   | 23.224.15.180  | United States | US   | CNSERVERS     | 23.225.9.218                       | Yes (Region: US) |
|  5 | [8](config/8.json)   | 45.199.138.160 | Netherlands   | NL   | YISP B.V.     | 154.84.1.230                       | Yes (Region: NL) |
|  6 | [9](config/9.json)   | 156.225.67.48  | Netherlands   | NL   | YISP B.V.     | 154.84.1.164                       | Yes (Region: NL) |
|  7 | [16](config/16.json) | 156.245.8.143  | Netherlands   | NL   | YISP B.V.     | 154.84.1.139                       | Yes (Region: NL) |
|  8 | [18](config/18.json) | 173.82.55.92   | United States | US   | MULTA-ASN1    | 23.234.230.34                      | Yes (Region: US) |
|  9 | [19](config/19.json) | Shopify.com    | France        | FR   | CLOUDFLARENET | 2a09:bac5:3264:be::13:298          | Yes (Region: FR) |
| 10 | [26](config/26.json) | 46.182.107.183 | Netherlands   | NL   | YISP B.V.     | 154.84.1.19                        | Yes (Region: NL) |
| 11 | [35](config/35.json) | 23.234.198.83  |               |      |               | 2607:f130:109:0:225:90ff:fe79:7d34 | Yes (Region: US) |
| 12 | [39](config/39.json) | vau1.0bad.com  |               |      |               | 172.105.254.156                    | Yes (Region: AU) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjEzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ4NjU5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAzIiwgImFkZCI6ICIxNzMuODIuNjcuMTk1IiwgInBvcnQiOiAiMzQ0MTIiLCAiaWQiOiAiODI2MjBhNmUtZGJmZC00ZDU3LThhNTktOTAwNGE0YmI5ZTkyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVzMi5zYW5mZW5jZG4xLmNvbSIsICJwYXRoIjogIi96aC1jbiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDZXJhTmV0d29ya3NcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMjMuMjI1LjIxMS4yMSIsICJwb3J0IjogIjQyOTQxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgInBvcnQiOiAiNDQzMTMiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjU3ZjkzZTkyLWViYjktNGYxNi05YmRjLTgyMjVkMjAxMDk5NSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9wYXRoLzE2ODk1ODg0OTc3NjUiLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMjMuMjI0LjE1LjE4MCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MDAwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyQ29wZXJhdGlvbiBDb2xvY3Rpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjAiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI5NTQ5YTJjZi0xMjliLTQzYTEtODhkYi1lZjdmNjQ4ZGU3NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTEyMDQsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny40OCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0ODEyMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogNDkxNTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZiAgMTYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTczLjgyLjU1LjkyIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDE4IiwgInBvcnQiOiAzNDQxMiwgImlkIjogIjgyNjIwYTZlLWRiZmQtNGQ1Ny04YTU5LTkwMDRhNGJiOWU5MiIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiU2hvcGlmeS5jb20iLCAiYWlkIjogMCwgImhvc3QiOiAiRnIuY2xvdWRmbGFyZS5xdWVzdCIsICJpZCI6ICIyNTBmNDMzMS04YzNlLTRiODctYTg2Yi01YzVmYmY5ZGRiYTgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FyaWVzIiwgInBvcnQiOiAyMDg2LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDE5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzAgIDI2IiwgImFkZCI6ICI0Ni4xODIuMTA3LjE4MyIsICJwb3J0IjogIjU2MTAzIiwgImlkIjogIjIxMTU1ZWZkLThlMjktNDNkMi05NWJjLWZlMzE5MGVjYjFjNiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44MyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAzNSIsICJwb3J0IjogMzQ4ODgsICJpZCI6ICJhOWFiZjNlNy04N2Y0LTQ3M2QtOGQwMy0yZjI2Y2E0YjM1ODMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAidmF1MS4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJ2YXUxLjBiYWQuY29tIiwgImlkIjogIjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvY2hhdCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNMaW5vZGVcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMzkiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

