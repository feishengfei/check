
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr          | cn            | cc   | isp        | ip            | chatgpt          |
|---:|:---------------------|:--------------|:--------------|:-----|:-----------|:--------------|:-----------------|
|  0 | [3](config/3.json)   | 142.4.99.93   | United States | US   | PEGTECHINC | 142.4.99.65   | Yes (Region: US) |
|  1 | [7](config/7.json)   | 149.28.94.183 | United States | US   | AS-CHOOPA  | 149.28.94.183 | Yes (Region: US) |
|  2 | [8](config/8.json)   | 172.67.59.101 | United States | US   | CNSERVERS  | 23.225.9.234  | Yes (Region: US) |
|  3 | [13](config/13.json) | 107.167.29.93 | United States | US   | SHARKTECH  | 107.167.9.234 | Yes (Region: US) |
|  4 | [14](config/14.json) | 107.167.7.12  | United States | US   | SHARKTECH  | 107.167.18.50 | Yes (Region: US) |
|  5 | [16](config/16.json) | 156.245.8.143 | Netherlands   | NL   | YISP B.V.  | 154.84.1.139  | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuOTkuOTMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMzNzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTQ5LjI4Ljk0LjE4MyIsICJwb3J0IjogIjEwMDAyIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJlMGI3MTVjZC00MDU4LTRjZjQtYjY3ZS1kMzcwNjMyOTRiNzUiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvaHVhd2VpIiwgImhvc3QiOiAiY2xvdWRmbGFyZS5waWFvbGUubWUiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjY3LjU5LjEwMSIsICJhaWQiOiAwLCAiaG9zdCI6ICJ0eHgudnRjc3MudG9wIiwgImlkIjogIjNjZDRmODU5LTEwNDgtNGZkZi1kOGQ4LTRkYmZhYTllOGE4MCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcXdlcjAiLCAicG9ydCI6IDIwNTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTA3LjE2Ny4yOS45MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQ2NWRlYzFhLWUwOWItNGJiNi05OTA1LTcwZjc1ZDYwMzVjOCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NTU4NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDEzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTA3LjE2Ny43LjEyIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJiZGVlMjAyYy04ZmFlLTQ0MWYtYTU4OC03YmM0ZDM4ODcwMTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0MTY1NCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlx1NWUwMlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxNCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTExMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAxNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

