
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp            | ip              | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:---------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 46.182.107.102 | Netherlands   | NL   | YISP B.V.      | 154.84.1.137    | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.225.67.78  | Netherlands   | NL   | YISP B.V.      | 46.182.107.216  | Yes (Region: US) |
|  2 | [4](config/4.json)   | 156.245.8.241  | Netherlands   | NL   | YISP B.V.      | 154.84.1.44     | Yes (Region: NL) |
|  3 | [6](config/6.json)   | 107.167.30.132 | United States | US   | SHARKTECH      | 170.178.185.146 | Yes (Region: US) |
|  4 | [7](config/7.json)   | 45.199.138.176 | United States | US   | NovoServe B.V. | 45.199.138.43   | Yes (Region: US) |
|  5 | [8](config/8.json)   | 45.199.138.158 | Poland        | PL   | OVH SAS        | 54.36.174.181   | Yes (Region: FR) |
|  6 | [10](config/10.json) | 45.199.138.195 | Netherlands   | NL   | YISP B.V.      | 154.84.1.128    | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzAgIDIiLCAiYWRkIjogIjQ2LjE4Mi4xMDcuMTAyIiwgInBvcnQiOiAiMzg2NTEiLCAiaWQiOiAiOTY0YmY0OTktOWVjMC00Mzc4LTkyYjYtODdkOGQ4NjFiMmQwIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzgiLCAicG9ydCI6ICI0MjIzOSIsICJpZCI6ICIzZTAxNmM0ZC05ODZlLTQyZGYtODM4Yy02MDQ2ZjNkODllY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC4yNDEiLCAicG9ydCI6ICIzNDg0NiIsICJpZCI6ICIyOWE1ZDQ4ZS0yNGYxLTQ4ZmQtYTVlMS05YTQ2Y2IzMTAzMmYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTA3LjE2Ny4zMC4xMzIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI1OGU1NjBiNC1iYmE2LTQ4NDMtYmU1Zi04MzMyMTAyMmZhMGQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDM5MDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlx1NWUwMlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE3NiIsICJwb3J0IjogIjQ5ODUyIiwgImlkIjogIjZmYTU2MGQ0LTM1YzUtNDk2OC1hZGZjLTgxMmM1Mjg3OGI4NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA4IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE1OCIsICJwb3J0IjogIjMyMTQ0IiwgImlkIjogImY1MjUwYzRlLWY4NTUtNGVmZi1iNzNjLWEwMjIyNmQ0MmZlNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTUiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmZTVmNjllNy1lMTgzLTQzOWItOTUwYi05NjYxZWYwNjUxZjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMzAzNTgsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDEwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2NPVkggMzAiLCAiYWRkIjogIjEzOS45OS4yNDUuMTY0IiwgInBvcnQiOiAiNDk5MjEiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
```

