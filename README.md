
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn              | cc   | isp                 | ip                                  | chatgpt          |
|---:|:---------------------|:---------------|:----------------|:-----|:--------------------|:------------------------------------|:-----------------|
|  0 | [5](config/5.json)   | 156.245.8.185  | The Netherlands | NL   | YISP B.V.           | 154.84.1.161                        | Yes (Region: NL) |
|  1 | [6](config/6.json)   | 156.249.18.64  | The Netherlands | NL   | YISP B.V.           | 154.84.1.122                        | Yes (Region: NL) |
|  2 | [7](config/7.json)   | 120.233.43.37  | Hong Kong       | HK   | CNSERVERS           | 172.247.18.66                       | Yes (Region: US) |
|  3 | [10](config/10.json) | 154.85.0.152   | The Netherlands | NL   | YISP B.V.           | 154.84.1.128                        | Yes (Region: NL) |
|  4 | [11](config/11.json) | 5.57.37.151    | Germany         | DE   | Hetzner Online GmbH | 142.132.186.228                     | Yes (Region: DE) |
|  5 | [12](config/12.json) | 148.135.33.93  | United States   | US   | MULTA-ASN1          | 2607:f130:109:0:d6ae:52ff:febb:b49f | Yes (Region: US) |
|  6 | [15](config/15.json) | 156.225.67.66  | The Netherlands | NL   | YISP B.V.           | 154.84.1.136                        | Yes (Region: NL) |
|  7 | [20](config/20.json) | 192.74.245.233 | United States   | US   | PEG-SV              | 198.2.201.171                       | Yes (Region: US) |
|  8 | [22](config/22.json) | 156.245.8.180  | The Netherlands | NL   | YISP B.V.           | 46.182.107.129                      | Yes (Region: NL) |
|  9 | [26](config/26.json) | 156.245.8.96   | The Netherlands | NL   | YISP B.V.           | 154.84.1.121                        | Yes (Region: NL) |
| 10 | [28](config/28.json) | 156.225.67.104 | The Netherlands | NL   | YISP B.V.           | 154.84.1.44                         | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAiYWRkIjogIjE1Ni4yNDUuOC4xODUiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICJkNzczNTA1OC0xZGFjLTQ2MTgtOTlmZi0wYWEwNDQxZWMyZDciLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMjAxNjMzMjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjgyMDEzNjYxMSIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTU2LjI0OS4xOC42NCIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjRlYzBhZTYyLWRlMDktNDAyOS05MDRhLTAzMTNkNDYyOGVjZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy43MjI4MTE0OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyODIwMTM2NjExIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggNyIsICJhZGQiOiAiMTIwLjIzMy40My4zNyIsICJwb3J0IjogIjUyNjI5IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTAiLCAiYWRkIjogIjE1NC44NS4wLjE1MiIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogImZlNWY2OWU3LWUxODMtNDM5Yi05NTBiLTk2NjFlZjA2NTFmMiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40Mzc0NzQxNC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyOTYxNzE2NzM4IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiNS41Ny4zNy4xNTEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImVhYTczZTMxLTlkOTAtNGQyMy04ZWM1LTgzNmJhZGZmNDM2ZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNTEyMTgiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDExIiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIm5vbmUiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTc0NWVcdTUxNzggIDEyIiwgImFkZCI6ICIxNDguMTM1LjMzLjkzIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4zMDk5NDEwNC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyNjUwOTkyNDkxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE1IiwgImFkZCI6ICIxNTYuMjI1LjY3LjY2IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiZWJlYzJhZGYtZTk0MC00NDZmLWJlZDQtZDhjOTExNDNiNTRhIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjkyMTI4Njc1Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyMCIsICJhZGQiOiAiMTkyLjc0LjI0NS4yMzMiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiYWM5ZDc1ZmEtY2RmOC00YWNlLTgwMTItM2ZjZDliYzk4OWI5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3Ljg3MjM4OTc1Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE3MDI4MjAxMzY2MTEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDIyIiwgImFkZCI6ICIxNTYuMjQ1LjguMTgwIiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiOTU0OWEyY2YtMTI5Yi00M2ExLTg4ZGItZWY3ZjY0OGRlNzRhIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjEzNTUzODMyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE3MDI5NjE3MTY3MzgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDI2IiwgImFkZCI6ICIxNTYuMjQ1LjguOTYiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICJiZDI0OWUzNy03MzU5LTQxZWUtODRhNy0wOWU0OWUwZWM1YzQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNDc1MjMzNzUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTcwMjk2MTcxNjczOCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDI4IiwgImFkZCI6ICIxNTYuMjI1LjY3LjEwNCIsICJwb3J0IjogIjQwMDAwIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4yNDQ0MzMyOC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNzAyOTYxNzE2NzM4IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

