
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr            | cn            | cc   | isp                    | ip             | chatgpt          |
|---:|:-------------------|:----------------|:--------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [2](config/2.json) | 156.225.67.229  | Netherlands   | NL   | YISP B.V.              | 154.84.1.219   | Yes (Region: NL) |
|  1 | [3](config/3.json) | 45.199.138.158  | Netherlands   | NL   | YISP B.V.              | 154.84.1.231   | Yes (Region: NL) |
|  2 | [4](config/4.json) | 45.199.138.149  | Netherlands   | NL   | YISP B.V.              | 46.182.107.123 | Yes (Region: US) |
|  3 | [6](config/6.json) | 139.59.1.39     | India         | IN   | DIGITALOCEAN-ASN       | 139.59.1.39    | Yes (Region: IN) |
|  4 | [7](config/7.json) | 108.166.203.183 | United States | US   | MULTA-ASN1             | 173.82.156.42  | Yes (Region: US) |
|  5 | [8](config/8.json) | www.codepen.io  | Singapore     | SG   | Akamai Connected Cloud | 139.162.58.23  | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjI5IiwgInBvcnQiOiAiNTA4ODEiLCAiaWQiOiAiNTE1YmNiNGQtMGJhMS00Y2FlLTg3Y2YtYTA0NzAwN2VlYzU0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE1OCIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImY1MjUwYzRlLWY4NTUtNGVmZi1iNzNjLWEwMjIyNmQ0MmZlNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0OSIsICJwb3J0IjogIjQ3NDkzIiwgImlkIjogImY5ZmEzYTljLWY3ZDUtNDE0Zi04OGU2LTY5NzA1ODVkOTk0OSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpNV2lJVllDeU84RmZ5YktXaGp0OVN6@139.59.1.39:443#github.com/freefq%20-%20%E5%8D%B0%E5%BA%A6%E5%8D%A1%E7%BA%B3%E5%A1%94%E5%85%8B%E9%82%A6%E7%8F%AD%E5%8A%A0%E7%BD%97%E5%B0%94DigitalOcean%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%206
vmess://eyJhZGQiOiAiMTA4LjE2Ni4yMDMuMTgzIiwgImFpZCI6ICI2NCIsICJhbHBuIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNjhhNDkxYi03NjRjLTQ0ZDEtODFhNC0zMGRlMTYxMzA4NjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI0NDk0NSIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDciLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInd3dy5jb2RlcGVuLmlvIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjJjZDM5MTAyLTA3OTktNGM2MS1hYmI2LTJlN2EyNThmMDM5NyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMtdi5zc2htYXgueHl6IiwgInBhdGgiOiAiL3ZtZXNzIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

