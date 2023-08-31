
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp                            | ip                                  | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:-------------------------------|:------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 45.82.253.110    | United States | US   | DEDIPATH-LLC                   | 45.12.131.218                       | Yes (Region: US) |
|  1 | [2](config/2.json)   | 45.199.138.196   | Netherlands   | NL   | YISP B.V.                      | 154.84.1.128                        | Yes (Region: NL) |
|  2 | [3](config/3.json)   | 156.249.18.24    | Netherlands   | NL   | YISP B.V.                      | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: NL) |
|  3 | [4](config/4.json)   | 156.225.67.73    | Netherlands   | NL   | YISP B.V.                      | 154.84.1.19                         | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 156.225.67.47    | Netherlands   | NL   | YISP B.V.                      | 154.84.1.164                        | Yes (Region: NL) |
|  5 | [8](config/8.json)   | dongtaiwang3.com | Poland        | PL   | OVH SAS                        | 54.36.174.181                       | Yes (Region: FR) |
|  6 | [9](config/9.json)   | 45.199.138.186   | Netherlands   | NL   | YISP B.V.                      | 154.84.1.122                        | Yes (Region: NL) |
|  7 | [16](config/16.json) | 172.64.153.211   | Sweden        | SE   | Stark Industries Solutions Ltd | 94.131.115.68                       | Yes (Region: SE) |
|  8 | [26](config/26.json) | 111.6.86.76      | Japan         | JP   | Akamai Connected Cloud         | 172.104.76.30                       | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuODIuMjUzLjExMCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTc2MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2YjI3XHU3NmRmICAxIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTYiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmZTVmNjllNy1lMTgzLTQzOWItOTUwYi05NjYxZWYwNjUxZjIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDcxNTgsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTU2LjI0OS4xOC4yNCIsICJwb3J0IjogIjQ0MjY1IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIiwgImZwIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1OTEwOSIsICJpZCI6ICIyMTE1NWVmZC04ZTI5LTQzZDItOTViYy1mZTMxOTBlY2IxYzYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiIsICJmcCI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNDciLCAicG9ydCI6ICI0OTQxNCIsICJpZCI6ICIzY2E5MTJkYS02YWMyLTQxOGYtYjljZi00NWI2ZjY5NDU3OWIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiIsICJmcCI6ICIifQ==
vmess://eyJhZGQiOiAiZG9uZ3RhaXdhbmczLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJkLmZyZWVoMS54eXoiLCAiaWQiOiAiNmRlZGRiN2YtZTU1Ny00MmRiLWJmYTAtY2Y0MGIzNmIyN2UyIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOShzaG9waWZ5KSA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA5IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4NiIsICJwb3J0IjogIjM0NTM4IiwgImlkIjogIjRlYzBhZTYyLWRlMDktNDAyOS05MDRhLTAzMTNkNDYyOGVjZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIiwgImZwIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4yMTEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAic2NoZXJlc3dlZC5zb2Z0d2FyZW5ld3Muc3RvcmUiLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkwMSIsICJwb3J0IjogIjQ0MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTYiLCAic2N5IjogImF1dG8iLCAic25pIjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTExLjYuODYuNzYiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjRhYWM5ZGMxLTQyODUtMzRiOS1iNDg2LTMwOTlkYTkxN2VhYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAyMTUxMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2Y2IzXHU1MzU3XHU3NzAxXHU2ZDFiXHU5NjMzXHU1ZTAyXHU3OWZiXHU1MmE4IDI2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

