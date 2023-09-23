
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp       | ip                                   | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:----------|:-------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 142.4.126.34   | United States | US   | PEG-SV    | 107.148.198.209                      | Yes (Region: US) |
|  1 | [4](config/4.json)   | 46.182.107.217 | Netherlands   | NL   | YISP B.V. | 46.182.107.216                       | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 156.245.8.170  | Netherlands   | NL   | YISP B.V. | 154.84.1.158                         | Yes (Region: NL) |
|  3 | [12](config/12.json) | 45.199.138.209 | Netherlands   | NL   | YISP B.V. | 2a02:2a38:1:2796:ae1f:6bff:fe24:8940 | Yes (Region: NL) |
|  4 | [13](config/13.json) | 156.249.18.2   | Netherlands   | NL   | YISP B.V. | 154.84.1.148                         | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAzIiwgImFkZCI6ICIxNDIuNC4xMjYuMzQiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yOTEzNTAxOS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk1MzgwMzUxNzUxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzAgIDQiLCAiYWRkIjogIjQ2LjE4Mi4xMDcuMjE3IiwgInBvcnQiOiA0NDMsICJpZCI6ICIzZTAxNmM0ZC05ODZlLTQyZGYtODM4Yy02MDQ2ZjNkODllY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNTY0Mjc5OTQueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NTM4MDM1MTc1MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAiYWRkIjogIjE1Ni4yNDUuOC4xNzAiLCAicG9ydCI6IDQ0MywgImlkIjogIjNhM2M4YTljLTMzNGUtNDM2MC1hZGI4LWE4MGE1N2RkY2JiZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4xNjA0NjYyNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk1MzgwMzUxNzUxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4yMDkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhNDY5MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTA0NDcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDEyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogIjE1Ni4yNDkuMTguMiIsICJwb3J0IjogNDQzLCAiaWQiOiAiODRkMWRlMTEtY2UxMi00YTE1LTgzMTItMTMzODM1NmQ0YWM0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjU3NDI0MzQ5Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTUzODAzNTE3NTEiLCAidGxzIjogInRscyJ9
```

