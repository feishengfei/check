
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp        | ip            | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:-----------|:--------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.126.70             | China         | CN   | PEGTECHINC | 142.4.101.146 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 156.225.67.234           | Netherlands   | NL   | YISP B.V.  | 154.84.1.178  | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.225.67.111           | Netherlands   | NL   | YISP B.V.  | 154.84.1.140  | Yes (Region: NL) |
|  3 | [6](config/6.json)   | 198.2.204.244            | United States | US   | PEGTECHINC | 142.0.133.253 | Yes (Region: US) |
|  4 | [8](config/8.json)   | cf-lt.sharecentre.online | United States | US   | CNSERVERS  | 23.225.9.234  | Yes (Region: US) |
|  5 | [18](config/18.json) | dl.v001sssv.pw           | France        | FR   | OVH SAS    | 51.77.213.73  | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuMTI2LjcwIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDUyMjEyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjM0IiwgInBvcnQiOiAiNDgxMjMiLCAiaWQiOiAiOTM1MDNkZDUtMjQ1YS00ZWIxLWFlMmEtNTdhYjlmMmIzYzI5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmM1x1ZDgzY1x1ZGRmMU5MXHU4Mzc3XHU1MTcwKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTExIiwgInBvcnQiOiAiNDMxMjYiLCAiaWQiOiAiYjhkZjNlZjEtODg3Zi00ZWU0LTg1NWYtNGY4MDQxNmMyNDY0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjA0LjI0NCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NjkwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogODAsICJpZCI6ICI1Zjc1MWM2ZS01MGIxLTQ3OTctYmE4ZS02ZmZlMzI0YTBiY2UiLCAiYWlkIjogMCwgInNjeSI6ICJhZXMtMTI4LWdjbSIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJjYS5pbG92ZXNjcC5jb20iLCAicGF0aCI6ICIvc2hpcmtlciIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICIxMDQuMjQuMTY5LjIzOCIsICJwb3J0IjogNDQzLCAiaWQiOiAiMWEyNWRjZTQtOWQyNy00ZThkLWU0NmUtMTYxOTliZTU0ZjgxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzdGFyLW9uZS5jZmQiLCAicGF0aCI6ICIvcG9ydHMvNDUzMTQiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiZGwudjAwMXNzc3YucHciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAxOCIsICJwb3J0IjogODAsICJpZCI6ICJhNGJiN2Y5My1jZWU2LTQzZDctYjJkZC1mYTljNzBiODgyMzMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiZGwudjAwMXNzc3YucHciLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
```

