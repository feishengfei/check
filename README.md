
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp                              | ip                                  | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:---------------------------------|:------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 23.234.198.83        | United States | US   | MULTA-ASN1                       | 2607:f130:109:0:225:90ff:fe79:7d34  | Yes (Region: US) |
|  1 | [3](config/3.json)   | 173.82.55.92         | United States | US   | MULTA-ASN1                       | 23.234.230.34                       | Yes (Region: US) |
|  2 | [4](config/4.json)   | 23.225.211.21        | United States | US   | CNSERVERS                        | 23.225.57.210                       | Yes (Region: US) |
|  3 | [6](config/6.json)   | 156.249.18.36        | Netherlands   | NL   | YISP B.V.                        | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: US) |
|  4 | [8](config/8.json)   | bluehost.com         | Netherlands   | NL   | YISP B.V.                        | 154.84.1.230                        | Yes (Region: NL) |
|  5 | [13](config/13.json) | cfcdn5.sanfencdn.net | Japan         | JP   | Eons Data Communications Limited | 38.207.152.105                      | Yes (Region: US) |
|  6 | [15](config/15.json) | 64.32.21.246         | United States | US   | SHARKTECH                        | 107.167.24.162                      | Yes (Region: US) |
|  7 | [19](config/19.json) | 156.245.8.143        | Netherlands   | NL   | YISP B.V.                        | 154.84.1.139                        | Yes (Region: NL) |
|  8 | [24](config/24.json) | 104.20.18.54         | United States | US   | 24.hk global BGP                 | 163.197.245.87                      | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44MyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInBvcnQiOiAzNDg4OCwgImlkIjogImE5YWJmM2U3LTg3ZjQtNDczZC04ZDAzLTJmMjZjYTRiMzU4MyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTczLjgyLjU1LjkyIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAicG9ydCI6IDM0NDEyLCAiaWQiOiAiODI2MjBhNmUtZGJmZC00ZDU3LThhNTktOTAwNGE0YmI5ZTkyIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDZXJhTmV0d29ya3NcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMjMuMjI1LjIxMS4yMSIsICJwb3J0IjogIjQyOTQxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTU2LjI0OS4xOC4zNiIsICJwb3J0IjogIjQ4MjIyIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIva3BseHZ3cyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiYmx1ZWhvc3QuY29tIiwgImFpZCI6IDAsICJob3N0IjogImNkbmNhMS5kaWdpc3BvcnQuc2hvcCIsICJpZCI6ICJiZTc0Y2EwMy02YTdjLTRjODgtZWRjMi1jNjQzNGVhZDBjZmEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLzE2NTc1IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEzIiwgImFkZCI6ICJjZmNkbjUuc2FuZmVuY2RuLm5ldCIsICJwb3J0IjogIjIwNTIiLCAiaWQiOiAiODVjMzU5YmMtMjI0Ny00ZDgzLWEyOTQtNWQ3NzUyZGI1NjdmIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJqcDYuc2FuZmVuY2RuMi5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTUiLCAiYWRkIjogIjY0LjMyLjIxLjI0NiIsICJwb3J0IjogIjQ0MzEzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI1N2Y5M2U5Mi1lYmI5LTRmMTYtOWJkYy04MjI1ZDIwMTA5OTUiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvcGF0aC8xNjg5NTg4NDk3NzY1IiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogNDkxNTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZiAgMTkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI0IiwgImFkZCI6ICIxMDQuMjAuMTguNTQiLCAicG9ydCI6ICIyMDk1IiwgImlkIjogIjhjNGU1ZTgzLThiZTItNDYzOC1lM2Y2LWEwOThlZTQ4NDE5MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiaGsud3loa2FhMC50ayIsICJwYXRoIjogIi9AaGthYTAiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

