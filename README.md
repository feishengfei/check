
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp        | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 142.4.99.91    | United States | US   | PEGTECHINC | 142.4.99.65    | Yes (Region: US) |
|  1 | [4](config/4.json)   | 64.32.4.39     | United States | US   | SHARKTECH  | 107.167.13.162 | Yes (Region: US) |
|  2 | [5](config/5.json)   | 45.199.138.121 | Netherlands   | NL   | YISP B.V.  | 46.182.107.129 | Yes (Region: US) |
|  3 | [8](config/8.json)   | 140.99.128.114 | United States | US   | CNSERVERS  | 23.225.9.234   | Yes (Region: US) |
|  4 | [16](config/16.json) | 156.225.67.105 | Netherlands   | NL   | YISP B.V.  | 154.84.1.44    | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuOTkuOTEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0ggMyIsICJwb3J0IjogNDMzNzksICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuNC4zOSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzE2NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEyMSIsICJwb3J0IjogIjUxMjA0IiwgImlkIjogIjk1NDlhMmNmLTEyOWItNDNhMS04OGRiLWVmN2Y2NDhkZTc0YSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTQwLjk5LjEyOC4xMTQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTg0NTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZERhdGFiaWxpdHkgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE2IiwgImFkZCI6ICIxNTYuMjI1LjY3LjEwNSIsICJwb3J0IjogIjQ5MTAxIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwMikiLCAicGF0aCI6ICIvaXNhaWZxYWFncGkiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
```

