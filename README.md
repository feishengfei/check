
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                       | cn            | cc   | isp                    | ip                                 | chatgpt          |
|---:|:---------------------|:---------------------------|:--------------|:-----|:-----------------------|:-----------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 67.21.95.78                | United States | US   | SHARKTECH              | 2610:150:c011:1:225:90ff:fe56:4c9a | Yes (Region: US) |
|  1 | [2](config/2.json)   | 1496join.outline-vpn.cloud | United States | US   | MULTA-ASN1             | 173.82.156.42                      | Yes (Region: US) |
|  2 | [3](config/3.json)   | 156.225.67.74              | Netherlands   | NL   | YISP B.V.              | 154.84.1.19                        | Yes (Region: NL) |
|  3 | [4](config/4.json)   | 192.74.239.77              | United States | US   | PEG-SV                 | 38.63.0.65                         | Yes (Region: US) |
|  4 | [9](config/9.json)   | 19.kccic2pa.xyz            | Japan         | JP   | Akamai Connected Cloud | 2400:8902::f03c:93ff:fe8a:d61d     | Yes (Region: JP) |
|  5 | [11](config/11.json) | 39.kccic2pa.xyz            | United States | US   | OVH SAS                | 51.81.211.205                      | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJhZGQiOiAiNjcuMjEuOTUuNzgiLCAicG9ydCI6ICI1MzMxNCIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTQ5NmpvaW4ub3V0bGluZS12cG4uY2xvdWQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIyNjhhNDkxYi03NjRjLTQ0ZDEtODFhNC0zMGRlMTYxMzA4NjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDQ5NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny43NCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjIxMTU1ZWZkLThlMjktNDNkMi05NWJjLWZlMzE5MGVjYjFjNiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NTEwOSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgImFkZCI6ICIxOTIuNzQuMjM5Ljc3IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xOTQ1ODE2Mi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0MDgzMjg0ODY2IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggOSIsICJhZGQiOiAiMTkua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMTkiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJhZWZjMzg5LTcyYjEtNGYyMy1iYmFkLTNhODVjZjUxZmU4YSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIjE5LmtjY2ljMnBhLnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMTEiLCAiYWRkIjogIjM5LmtjY2ljMnBhLnh5eiIsICJwb3J0IjogIjUwMDM5IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJiYWVmYzM4OS03MmIxLTRmMjMtYmJhZC0zYTg1Y2Y1MWZlOGEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIzOS5rY2NpYzJwYS54eXoiLCAidGxzIjogIiJ9
```

