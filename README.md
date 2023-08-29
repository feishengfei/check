
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp       | ip              | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:----------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 107.167.30.132      | United States | US   | SHARKTECH | 170.178.185.146 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 156.245.8.240       | Netherlands   | NL   | YISP B.V. | 154.84.1.44     | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 156.225.67.38       | Netherlands   | NL   | YISP B.V. | 154.84.1.16     | Yes (Region: NL) |
|  3 | [8](config/8.json)   | stock.hostmonit.com | Poland        | PL   | OVH SAS   | 54.36.174.181   | Yes (Region: FR) |
|  4 | [17](config/17.json) | 156.249.18.217      | Netherlands   | NL   | YISP B.V. | 154.84.1.138    | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTA3LjE2Ny4zMC4xMzIiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAicG9ydCI6IDQzOTAwLCAiaWQiOiAiNThlNTYwYjQtYmJhNi00ODQzLWJlNWYtODMzMjEwMjJmYTBkIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0MCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MTI0NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4zOCIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3Ljg2MTM5MzE3Lnh5eiIsICJpZCI6ICJkZTQ5MTgwMi0yMzNlLTQ3ZjItOGM2Yy1kMTliY2Y1YmQ1NmIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MjI1NjkwMjQzMCIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInN0b2NrLmhvc3Rtb25pdC5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiY2Q3ZjZhODktZTg2YS00N2FlLTg3ZDMtMDI3N2QyMDUyODZmIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1czIuaWN1MnJpcC5ldS5vcmciLCAicGF0aCI6ICIvbmlzaGlrYXRhIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4yMTciLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xMTY0OTc2OS54eXoiLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTMwMTg3NDQ1MTIiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlXHU4YzZhXHU3NjdiXHU3NzAxXHU3ZWE2XHU3ZmYwXHU1MTg1XHU2NWFmXHU1ODIxQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDE3IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

