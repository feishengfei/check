
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp            | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:---------------|:---------------|:-----------------|
|  0 | [5](config/5.json)   | 45.199.138.176 | United States | US   | NovoServe B.V. | 45.199.138.43  | Yes (Region: US) |
|  1 | [6](config/6.json)   | 199.180.102.11 | China         | CN   | PEG-SV         | 142.4.99.65    | Yes (Region: US) |
|  2 | [8](config/8.json)   | 172.64.198.131 | Poland        | PL   | OVH SAS        | 54.36.174.181  | Yes (Region: FR) |
|  3 | [21](config/21.json) | 64.32.21.246   | United States | US   | SHARKTECH      | 107.167.24.162 | Yes (Region: US) |
|  4 | [26](config/26.json) | 156.245.8.241  | Netherlands   | NL   | YISP B.V.      | 154.84.1.44    | Yes (Region: NL) |
|  5 | [30](config/30.json) | 45.199.138.195 | Netherlands   | NL   | YISP B.V.      | 154.84.1.128   | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3NiIsICJwb3J0IjogIjQ5ODUyIiwgImlkIjogIjZmYTU2MGQ0LTM1YzUtNDk2OC1hZGZjLTgxMmM1Mjg3OGI4NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDYiLCAiYWRkIjogIjE5OS4xODAuMTAyLjExIiwgInBvcnQiOiAiNDQzIiwgImlkIjogImI2NWRhNGFmLWExMmEtNGE1OS05MzE2LTQ1NDllMTJiYTYyYyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy43MzMzMjQ2My54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkyMjU2OTAyNDMwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjE3Mi42NC4xOTguMTMxIiwgInBvcnQiOiAiODA4MCIsICJpZCI6ICI3NGE4OTBhYi01YzRiLTRmMzUtYWVhNC01ZmMyNDU5YmViZDIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImVjYy52dGNzcy50b3AiLCAicGF0aCI6ICIvYmx1ZTAzIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuMjEuMjQ2IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNTdmOTNlOTItZWJiOS00ZjE2LTliZGMtODIyNWQyMDEwOTk1IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0MzEzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDI2IiwgImFkZCI6ICIxNTYuMjQ1LjguMjQxIiwgInBvcnQiOiAiMzQ4NDYiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTUiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmZTVmNjllNy1lMTgzLTQzOWItOTUwYi05NjYxZWYwNjUxZjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzAzNTgsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDMwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

