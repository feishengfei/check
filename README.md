
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp        | ip                                 | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:-----------|:-----------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 173.82.55.92             | United States | US   | MULTA-ASN1 | 23.234.230.34                      | Yes (Region: US) |
|  1 | [4](config/4.json)   | 64.32.24.210             | United States | US   | SHARKTECH  | 170.178.189.58                     | Yes (Region: US) |
|  2 | [5](config/5.json)   | 23.225.211.21            | United States | US   | CNSERVERS  | 23.225.57.210                      | Yes (Region: US) |
|  3 | [8](config/8.json)   | cf-lt.sharecentre.online | Netherlands   | NL   | YISP B.V.  | 154.84.1.230                       | Yes (Region: NL) |
|  4 | [9](config/9.json)   | 23.234.198.83            | United States | US   | MULTA-ASN1 | 2607:f130:109:0:225:90ff:fe79:7d34 | Yes (Region: US) |
|  5 | [11](config/11.json) | 172.247.67.46            | United States | US   | CNSERVERS  | 23.225.9.234                       | Yes (Region: US) |
|  6 | [12](config/12.json) | 173.82.67.195            | United States | US   | MULTA-ASN1 | 23.234.230.34                      | Yes (Region: US) |
|  7 | [14](config/14.json) | 64.32.21.246             | United States | US   | SHARKTECH  | 107.167.24.162                     | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTczLjgyLjU1LjkyIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAicG9ydCI6IDM0NDEyLCAiaWQiOiAiODI2MjBhNmUtZGJmZC00ZDU3LThhNTktOTAwNGE0YmI5ZTkyIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjEwIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ4NjU5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDZXJhTmV0d29ya3NcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiMjMuMjI1LjIxMS4yMSIsICJwb3J0IjogIjQyOTQxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjVmNzUxYzZlLTUwYjEtNDc5Ny1iYThlLTZmZmUzMjRhMGJjZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZHAzLnNjcHJveHkudG9wIiwgInBhdGgiOiAiL3NoaXJrZXIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44MyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA5IiwgInBvcnQiOiAzNDg4OCwgImlkIjogImE5YWJmM2U3LTg3ZjQtNDczZC04ZDAzLTJmMjZjYTRiMzU4MyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjI0Ny42Ny40NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjIyNzhlZmU0LWFkMGMtNDdjZS05NDgwLTA2ODYwODM2OGQ3NiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MDAzNSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2Q29wZXJhdGlvbiBDb2xvY3Rpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZNVUxUQUNPTVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxMiIsICJhZGQiOiAiMTczLjgyLjY3LjE5NSIsICJwb3J0IjogIjM0NDEyIiwgImlkIjogIjgyNjIwYTZlLWRiZmQtNGQ1Ny04YTU5LTkwMDRhNGJiOWU5MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1czIuc2FuZmVuY2RuMS5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAiYWRkIjogIjY0LjMyLjIxLjI0NiIsICJwb3J0IjogIjQ0MzEzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI1N2Y5M2U5Mi1lYmI5LTRmMTYtOWJkYy04MjI1ZDIwMTA5OTUiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvcGF0aC8xNjg5NTg4NDk3NzY1IiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
```

