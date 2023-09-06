
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp              | ip                    | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------|:----------------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.162  | Netherlands   | NL   | YISP B.V.        | 154.84.1.230          | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 164.90.233.192  | Germany       | DE   | DIGITALOCEAN-ASN | 164.90.233.192        | Yes (Region: DE) |
|  2 | [4](config/4.json)   | 45.199.138.148  | Netherlands   | NL   | YISP B.V.        | 46.182.107.123        | Yes (Region: NL) |
|  3 | [6](config/6.json)   | 23.224.11.147   | United States | US   | CNSERVERS        | 23.225.9.194          | Yes (Region: US) |
|  4 | [7](config/7.json)   | 39.kccic2pa.xyz | United States | US   | OVH SAS          | 51.81.211.205         | Yes (Region: US) |
|  5 | [8](config/8.json)   | 104.20.27.27    | Poland        | PL   | OVH SAS          | 54.36.174.181         | Yes (Region: FR) |
|  6 | [10](config/10.json) | 07.kccic2pa.xyz | Austria       | AT   | Hohl IT e.U.     | 2a0d:f302:109:1cbe::1 | Yes (Region: AT) |
|  7 | [23](config/23.json) | cloudqwq.cf     | France        | FR   | SYNLINQ          | 103.252.90.249        | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNjIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI2NWVhNjcyNy00NDYxLTQ3YTctYTVjNC1mZWYyYzY3ZjJmNzkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTQ4NzEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDMiLCAiYWRkIjogIjE2NC45MC4yMzMuMTkyIiwgInBvcnQiOiAiNDQ1ODkiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjcyYzI4YzQ5LWVhMmItNDhjNC04ZDQwLTNkN2FjOWRmYTQ1ZiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL2hvc3RvZG8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNDgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmOWZhM2E5Yy1mN2Q1LTQxNGYtODhlNi02OTcwNTg1ZDk5NDkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDk5NTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMjMuMjI0LjExLjE0NyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MTAwOSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyQ29wZXJhdGlvbiBDb2xvY3Rpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggNyIsICJhZGQiOiAiMzkua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMzkiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJhZWZjMzg5LTcyYjEtNGYyMy1iYmFkLTNhODVjZjUxZmU4YSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIjM5LmtjY2ljMnBhLnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTA0LjIwLjI3LjI3IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOCIsICJwb3J0IjogODAsICJpZCI6ICIyMWI1NGI4MC00OGI1LTExZWUtYjMzOC0yMDVjNmQ1ZjVkNzgiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiZXUtMi4wcmQubmV0IiwgInBhdGgiOiAiL295MG5zNngzIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMTAiLCAiYWRkIjogIjA3LmtjY2ljMnBhLnh5eiIsICJwb3J0IjogIjUwMDA3IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICJiYWVmYzM4OS03MmIxLTRmMjMtYmJhZC0zYTg1Y2Y1MWZlOGEiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi9kb25ndGFpd2FuZy5jb20iLCAiaG9zdCI6ICIwNy5rY2NpYzJwYS54eXoiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiY2xvdWRxd3EuY2YiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRFYXN5RE5TIEFueWNhc3RcdTgyODJcdTcwYjkoQ2xvdWRmbGFyZVx1ODI4Mlx1NzBiOSkgMjMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

