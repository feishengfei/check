
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp                               | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:----------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 167.88.63.59   | United States | US   | AS-GLOBALTELEHOST                 | 167.88.63.59   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 167.88.63.59   | United States | US   | AS-GLOBALTELEHOST                 | 167.88.63.59   | Yes (Region: US) |
|  2 | [5](config/5.json)   | 142.4.98.232   | China         | CN   | PEG-SV                            | 142.0.129.201  | Yes (Region: US) |
|  3 | [6](config/6.json)   | 64.68.192.77   | Canada        | CA   | AS-GLOBALTELEHOST                 | 158.51.121.194 | Yes (Region: CA) |
|  4 | [7](config/7.json)   | 156.249.18.157 | Netherlands   | NL   | YISP B.V.                         | 154.84.1.232   | Yes (Region: NL) |
|  5 | [8](config/8.json)   | 45.199.138.146 | Netherlands   | NL   | YISP B.V.                         | 154.84.1.122   | Yes (Region: NL) |
|  6 | [19](config/19.json) | 120.233.43.47  | Taiwan        | TW   | Data Communication Business Group | 211.20.157.212 | Yes (Region: TW) |

## Valid
```
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@167.88.63.59:7306#github.com/freefq%20-%20%E7%91%9E%E5%85%B8%20%202
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@167.88.63.59:443#github.com/freefq%20-%20%E7%91%9E%E5%85%B8%20%203
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA1IiwgImFkZCI6ICIxNDIuNC45OC4yMzIiLCAicG9ydCI6IDQ0MywgImlkIjogIjA1MWI4NDRmLWVmZTMtNDg0Ny05MmFhLTY2YjVkZTBiNmQ0ZSIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4xMjk3MTQ3NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MTkzMTAwMzg4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRFYXN5RE5TIEFueWNhc3RcdTgyODJcdTcwYjkoQ2xvdWRmbGFyZVx1ODI4Mlx1NzBiOSkgNiIsICJhZGQiOiAiNjQuNjguMTkyLjc3IiwgInBvcnQiOiA0NDMsICJpZCI6ICIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCAiYWlkIjogMSwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogIm9waGVsaWEubW9tIiwgInBhdGgiOiAibGlua3Z3cyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTU2LjI0OS4xOC4xNTciLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiMTMwYzlmMmUtNDJiMS00ZWJmLWIzNDUtZTI2NDU2YTA2MWY5IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjUzNDg5NzYxLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkyODAwOTkxMzgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA4IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogMzAwMDAsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTkyMjkzNjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5OTE5MzEwMDM4OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTkiLCAiYWRkIjogIjEyMC4yMzMuNDMuNDciLCAicG9ydCI6ICIxMTAxMyIsICJpZCI6ICI4NWRiNjY1Mi1hNzQ3LTNhMGEtYTE3MC00MjI3MzYwNzY0MTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

