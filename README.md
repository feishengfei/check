
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp                               | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:----------------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 107.167.30.87  | United States | US   | SHARKTECH                         | 107.167.24.162 | Yes (Region: US) |
|  1 | [4](config/4.json)   | 64.68.192.77   | Canada        | CA   | AS-GLOBALTELEHOST                 | 158.51.121.194 | Yes (Region: CA) |
|  2 | [5](config/5.json)   | 156.249.18.195 | Netherlands   | NL   | YISP B.V.                         | 46.182.107.129 | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 142.4.108.28   | China         | CN   | PEG-SV                            | 142.4.108.17   | Yes (Region: US) |
|  4 | [9](config/9.json)   | 45.199.138.146 | Netherlands   | NL   | YISP B.V.                         | 154.84.1.122   | Yes (Region: NL) |
|  5 | [10](config/10.json) | 156.249.18.157 | Netherlands   | NL   | YISP B.V.                         | 154.84.1.232   | Yes (Region: NL) |
|  6 | [15](config/15.json) | 120.233.43.47  | Taiwan        | TW   | Data Communication Business Group | 211.20.157.212 | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTA3LjE2Ny4zMC44NyIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI1N2Y5M2U5Mi1lYmI5LTRmMTYtOWJkYy04MjI1ZDIwMTA5OTUiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMzI5MzI2NzEueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRFYXN5RE5TIEFueWNhc3RcdTgyODJcdTcwYjkoQ2xvdWRmbGFyZVx1ODI4Mlx1NzBiOSkgNCIsICJhZGQiOiAiNjQuNjguMTkyLjc3IiwgInBvcnQiOiA0NDMsICJpZCI6ICIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCAiYWlkIjogMSwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogIm9waGVsaWEubW9tIiwgInBhdGgiOiAibGlua3Z3cyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiMTU2LjI0OS4xOC4xOTUiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiOTU0OWEyY2YtMTI5Yi00M2ExLTg4ZGItZWY3ZjY0OGRlNzRhIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjEzNTUzODMyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkxOTMxMDAzODgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA4IiwgImFkZCI6ICIxNDIuNC4xMDguMjgiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40MjQzODc3OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MjgwMDk5MTM4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA5IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjE1Ni4yNDkuMTguMTU3IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjEzMGM5ZjJlLTQyYjEtNGViZi1iMzQ1LWUyNjQ1NmEwNjFmOSIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41MzQ4OTc2MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MjgwMDk5MTM4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTUiLCAiYWRkIjogIjEyMC4yMzMuNDMuNDciLCAicG9ydCI6ICIxMTAxMyIsICJpZCI6ICI4NWRiNjY1Mi1hNzQ3LTNhMGEtYTE3MC00MjI3MzYwNzY0MTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

