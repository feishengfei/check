
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn             | cc   | isp                    | ip             | chatgpt          |
|---:|:---------------------|:--------------------|:---------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 45.58.186.90        | United States  | US   | SHARKTECH              | 64.32.2.26     | Yes (Region: US) |
|  1 | [3](config/3.json)   | 156.225.67.73       | Netherlands    | NL   | YISP B.V.              | 154.84.1.19    | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.245.8.128       | Netherlands    | NL   | YISP B.V.              | 154.84.1.164   | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 154.85.1.245        | Netherlands    | NL   | YISP B.V.              | 154.84.1.206   | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 64.32.4.41          | United States  | US   | SHARKTECH              | 107.167.13.162 | Yes (Region: US) |
|  5 | [7](config/7.json)   | 45.199.138.95       | Netherlands    | NL   | YISP B.V.              | 154.84.1.229   | Yes (Region: NL) |
|  6 | [8](config/8.json)   | 154.84.1.113        | United States  | US   | CNSERVERS              | 23.225.9.234   | Yes (Region: US) |
|  7 | [9](config/9.json)   | 45.199.138.114      | Netherlands    | NL   | YISP B.V.              | 154.84.1.232   | Yes (Region: NL) |
|  8 | [10](config/10.json) | cfcdn.sanfencdn.net | United States  | US   | Akamai Connected Cloud | 45.33.45.177   | Yes (Region: US) |
|  9 | [11](config/11.json) | 183.249.207.247     | United Kingdom | GB   | OVH SAS                | 51.89.40.141   | Yes (Region: GB) |
| 10 | [18](config/18.json) | dl8.v001sssv.pw     | France         | FR   | OVH SAS                | 51.178.24.58   | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiNDUuNTguMTg2LjkwIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDUxMTQwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1MzEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDQiLCAiYWRkIjogIjE1Ni4yNDUuOC4xMjgiLCAicG9ydCI6ICI0ODEyMCIsICJpZCI6ICIzY2E5MTJkYS02YWMyLTQxOGYtYjljZi00NWI2ZjY5NDU3OWIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ1IiwgInBvcnQiOiAiNDc3MzEiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuNC40MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzE2NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA3IiwgImFkZCI6ICI0NS4xOTkuMTM4Ljk1IiwgInBvcnQiOiAiNDk5MjEiLCAiaWQiOiAiZDMxMzM0ODQtZjJiZi00YjBjLThkMzgtZjhlNjQ1YjY1Njg3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiMTU0Ljg0LjEuMTEzIiwgInBvcnQiOiAiNDc4NTIiLCAiaWQiOiAiNWE0ZDY5YWQtMjBhOS00OTQxLWIyMjMtODdiYmQwOWY1ZjUyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA5IiwgImFkZCI6ICI0NS4xOTkuMTM4LjExNCIsICJwb3J0IjogIjQxMjk4IiwgImlkIjogIjEzMGM5ZjJlLTQyYjEtNGViZi1iMzQ1LWUyNjQ1NmEwNjFmOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICJjZmNkbi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImYxMTRlNmQ5LTBjZGEtNGZlOC1iNzY5LTNiY2ViM2JjYTQ1MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXM0LnNhbmZlbmNkbjEuY29tIiwgInBhdGgiOiAiL3poLWNuIiwgInRscyI6ICJ0bHMiLCAic25pIjogInVzMS5zYW5mZW5jZG4xLmNvbSJ9
vmess://eyJhZGQiOiAiMTgzLjI0OS4yMDcuMjQ3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiODNhNDI0ZDgtNGJjYi00Y2VlLWIwMTYtMmM4ZjFkYjRhOTIxIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3MDA5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTRlM2RcdTZjMzRcdTVlMDJcdTc5ZmJcdTUyYTggMTEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE4IiwgImFkZCI6ICJkbDgudjAwMXNzc3YucHciLCAicG9ydCI6ICI4MCIsICJpZCI6ICIzZmVjNzE4Mi0wMmZiLTQ3MzAtOWI5Ny00YzlhZWU1NjNlZjYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImRsOC52MDAxc3Nzdi5wdyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

