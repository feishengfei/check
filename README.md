
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp                 | ip                                 | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:--------------------|:-----------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 23.234.198.86    | United States | US   | MULTA-ASN1          | 2607:f130:109:0:225:90ff:fe79:7d34 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 107.167.7.19     | United States | US   | SHARKTECH           | 107.167.18.50                      | Yes (Region: US) |
|  2 | [4](config/4.json)   | 156.245.8.187    | Netherlands   | NL   | YISP B.V.           | 154.84.1.40                        | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 154.85.1.41      | Netherlands   | NL   | YISP B.V.           | 154.84.1.229                       | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 156.225.67.158   | Netherlands   | NL   | YISP B.V.           | 154.84.1.197                       | Yes (Region: NL) |
|  5 | [8](config/8.json)   | cf.yxjnode.com   | United States | US   | AS-GLOBALTELEHOST   | 169.197.141.187                    | Yes (Region: US) |
|  6 | [25](config/25.json) | hd.mamadcucu.com | Germany       | DE   | Hetzner Online GmbH | 2a01:4f8:c010:7495::1              | Yes (Region: DE) |

## Valid
```
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImE5YWJmM2U3LTg3ZjQtNDczZC04ZDAzLTJmMjZjYTRiMzU4MyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNDg4OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTA3LjE2Ny43LjE5IiwgInBvcnQiOiAiNDE2NTQiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJkZWUyMDJjLThmYWUtNDQxZi1hNTg4LTdiYzRkMzg4NzAxOSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC4xODciLCAicG9ydCI6ICI1MDMwOSIsICJpZCI6ICI1YTRkNjlhZC0yMGE5LTQ5NDEtYjIyMy04N2JiZDA5ZjVmNTIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuNDEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUiLCAicG9ydCI6IDQ0MTg3LCAiaWQiOiAiZDMxMzM0ODQtZjJiZi00YjBjLThkMzgtZjhlNjQ1YjY1Njg3IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTU4IiwgInBvcnQiOiAiNDAzNDgiLCAiaWQiOiAiOWMwMjZlZmUtNmFmMC00NjVmLWI4YzAtM2Y1OGM4YzJkNGM1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLnl4am5vZGUuY29tIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMDljMWQzMmQtNDQ1OC00ZWJmLWIzNmQtNGRkNzMyYmFlM2FhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJidXl2bTIueXhqbm9kZS5jb20iLCAicGF0aCI6ICIveXh6YnAiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiaGQubWFtYWRjdWN1LmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJoNC5tYW1hZGN1Y3UuY29tIiwgImlkIjogIjhlZDlhZWMyLWUwMmUtNGEyNy1mZTAyLWMzZTIwNDUyZTRjNyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAyMDUyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDI1IiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIn0=
```

