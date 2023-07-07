
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 67.21.84.217   | United States | US   | SHARKTECH         | 67.21.85.2     | Yes (Region: US) |
|  1 | [4](config/4.json)   | 156.225.67.225 | Netherlands   | NL   | YISP B.V.         | 154.84.1.136   | Yes (Region: NL) |
|  2 | [8](config/8.json)   | 156.245.8.129  | United States | US   | CNSERVERS         | 23.225.9.234   | Yes (Region: US) |
|  3 | [9](config/9.json)   | 139.99.245.164 | Australia     | AU   | OVH SAS           | 139.99.130.144 | Yes (Region: AU) |
|  4 | [12](config/12.json) | 104.24.226.79  | United States | US   | DIGITALOCEAN-ASN  | 164.90.159.137 | Yes (Region: US) |
|  5 | [23](config/23.json) | 202.79.174.157 | South Korea   | KR   | BGPNET Global ASN | 202.79.174.146 | Yes (Region: SG) |

## Valid
```
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYjlhMzA1YTktMWZmMi00ZWMxLWIzMzgtOTMzNTU1ODMzYmFhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3MDg4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yMjUiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJlYmVjMmFkZi1lOTQwLTQ0NmYtYmVkNC1kOGM5MTE0M2I1NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQ4MDI1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA0IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDgiLCAiYWRkIjogIjE1Ni4yNDUuOC4xMjkiLCAicG9ydCI6ICI0ODEyMCIsICJpZCI6ICIzY2E5MTJkYS02YWMyLTQxOGYtYjljZi00NWI2ZjY5NDU3OWIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2NPVkggOSIsICJhZGQiOiAiMTM5Ljk5LjI0NS4xNjQiLCAicG9ydCI6ICI0OTkyMSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiXHVkODNjXHVkZGU2XHVkODNjXHVkZGZhQVVcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWEoeW91dHViZVx1OTYzZlx1NGYxZlx1NzlkMVx1NjI4MCkiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICIxMDQuMjQuMjI2Ljc5IiwgInBvcnQiOiA0NDMsICJpZCI6ICI5ZmZiYjgxNi1iNGJiLTQ5M2YtYjU1OC1kZjUyN2I3Njc0NTYiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInN0YXItb25lLmNmZCIsICJwYXRoIjogIi9wb3J0cy8xMDE3OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMjAyLjc5LjE3NC4xNTciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmQkdQLk5FVCBDTjJcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjMiLCAicG9ydCI6IDU1MjY0LCAiaWQiOiAiMTIxYzljODktN2QxMS00ZjQ5LTkxMTItZGMxZTg1MzYzZjZmIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
```

