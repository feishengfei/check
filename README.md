
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn          | cc   | isp                    | ip             | chatgpt          |
|---:|:---------------------|:----------------------|:------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 156.245.8.25          | Netherlands | NL   | YISP B.V.              | 46.182.107.123 | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 154.85.0.159          | Netherlands | NL   | YISP B.V.              | 154.84.1.229   | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 146.190.94.141        | Singapore   | SG   | DIGITALOCEAN-ASN       | 146.190.94.141 | Yes (Region: SG) |
|  3 | [7](config/7.json)   | 45.199.138.146        | Netherlands | NL   | YISP B.V.              | 154.84.1.122   | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 154.84.1.120          | Netherlands | NL   | YISP B.V.              | 154.84.1.129   | Yes (Region: NL) |
|  5 | [9](config/9.json)   | 154.85.1.243          | Netherlands | NL   | YISP B.V.              | 154.84.1.216   | Yes (Region: NL) |
|  6 | [10](config/10.json) | cfcdn2.sanfencdn9.com | Singapore   | SG   | Akamai Connected Cloud | 139.144.117.95 | Yes (Region: US) |
|  7 | [11](config/11.json) | 156.249.18.195        | Netherlands | NL   | YISP B.V.              | 46.182.107.129 | Yes (Region: NL) |
|  8 | [12](config/12.json) | 156.225.67.106        | Netherlands | NL   | YISP B.V.              | 154.84.1.44    | Yes (Region: NL) |
|  9 | [13](config/13.json) | 154.84.1.245          | Netherlands | NL   | YISP B.V.              | 154.84.1.148   | Yes (Region: NL) |
| 10 | [19](config/19.json) | 154.85.0.35           | Netherlands | NL   | YISP B.V.              | 154.84.1.128   | Yes (Region: NL) |
| 11 | [20](config/20.json) | 156.245.8.166         | Netherlands | NL   | YISP B.V.              | 154.84.1.140   | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDIiLCAiYWRkIjogIjE1Ni4yNDUuOC4yNSIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogImY5ZmEzYTljLWY3ZDUtNDE0Zi04OGU2LTY5NzA1ODVkOTk0OSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4yMjI2Mjc2OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MDE3NTc1MzUxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU0Ljg1LjAuMTU5IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiZDMxMzM0ODQtZjJiZi00YjBjLThkMzgtZjhlNjQ1YjY1Njg3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3Ljc0OTcyODA0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkwMTc4MjExNDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTQ2LjE5MC45NC4xNDEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICA1IiwgInBvcnQiOiA0MjM1OCwgImlkIjogIjZlNGVkYmQ4LTc4NTQtNGVmNS1jOWM2LTQ5ZTk1ODIyZTRmYyIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJtZWRpYS1leHAxLmxpY2RuLmNvbSIsICJwYXRoIjogIi9AT05ISVRfRUhJIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjRlYzBhZTYyLWRlMDktNDAyOS05MDRhLTAzMTNkNDYyOGVjZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4OTMyNDAxNTc3IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiMTU0Ljg0LjEuMTIwIiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjBiMzA5MTYtZTIwMy00MTJlLThlYzAtOTAwZjNhY2Q1MTI4IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjY5NzA4MjcyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkwMTc4MjExNDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAiMTU0Ljg1LjEuMjQzIiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjI4MTE1MzYxLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkwMTc4MjExNDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICJjZmNkbjIuc2FuZmVuY2RuOS5jb20iLCAicG9ydCI6ICIyMDUyIiwgImlkIjogIjUwNmQ5M2VjLWZmZGItNDFjZC1iYmMzLTM2NzAzOWM0YjE4ZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAic2czNmM5OTc0ZTQucWNyeWVjaHZxdy54eXoiLCAicGF0aCI6ICIvdmlkZW8vYkZWRG5BeW4iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIiwgImZwIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAiYWRkIjogIjE1Ni4yNDkuMTguMTk1IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiOTU0OWEyY2YtMTI5Yi00M2ExLTg4ZGItZWY3ZjY0OGRlNzRhIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjEzNTUzODMyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkwMTc4MjExNDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMDYiLCAidiI6IDIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMTIiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICIyOWE1ZDQ4ZS0yNGYxLTQ4ZmQtYTVlMS05YTQ2Y2IzMTAzMmYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAidGxzIjogInRscyIsICJwYXRoIjogIi9wYXRoLzE2OTg2NzE2MDA5ODYifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogIjE1NC44NC4xLjI0NSIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjg0ZDFkZTExLWNlMTItNGExNS04MzEyLTEzMzgzNTZkNGFjNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy41NzQyNDM0OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MDE3NTc1MzUxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTkiLCAiYWRkIjogIjE1NC44NS4wLjM1IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiZmU1ZjY5ZTctZTE4My00MzliLTk1MGItOTY2MWVmMDY1MWYyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjUzNDY2MDk2Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkwMTc4MjExNDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDIwIiwgImFkZCI6ICIxNTYuMjQ1LjguMTY2IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiYjhkZjNlZjEtODg3Zi00ZWU0LTg1NWYtNGY4MDQxNmMyNDY0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjEyNDYwMTU4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkwMTc1NzUzNTEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
```

