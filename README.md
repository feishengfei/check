
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp        | ip              | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 64.32.4.41     | United States | US   | SHARKTECH  | 107.167.13.162  | Yes (Region: US) |
|  1 | [4](config/4.json)   | 156.245.8.158  | Netherlands   | NL   | YISP B.V.  | 154.84.1.138    | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 137.175.1.13   | United States | US   | PEGTECHINC | 107.148.193.115 | Yes (Region: US) |
|  3 | [7](config/7.json)   | 137.175.52.18  | United States | US   | PEGTECHINC | 38.53.92.161    | Yes (Region: US) |
|  4 | [8](config/8.json)   | 104.20.184.232 | United States | US   | CNSERVERS  | 23.225.9.234    | Yes (Region: US) |
|  5 | [18](config/18.json) | 67.21.84.214   | United States | US   | SHARKTECH  | 67.21.85.2      | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuNC40MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzE2NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE1OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAicG9ydCI6IDQ4MTIzLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDYiLCAiYWRkIjogIjEzNy4xNzUuMS4xMyIsICJwb3J0IjogIjUzNDAzIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTM3LjE3NS41Mi4xOCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzMzAwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICA3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTA0LjIwLjE4NC4yMzIiLCAiYWlkIjogMCwgImhvc3QiOiAidXh4LnZ0Y3NzLnRvcCIsICJpZCI6ICJlYjk0M2M1Yi1hYzU1LTQ2ZjktODcxMC1kMDY0MWMzOGFlOWIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3F3ZXIiLCAicG9ydCI6IDIwODYsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYjlhMzA1YTktMWZmMi00ZWMxLWIzMzgtOTMzNTU1ODMzYmFhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3MDg4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

