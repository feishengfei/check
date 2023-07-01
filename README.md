
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp              | ip                         | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------|:---------------------------|:-----------------|
|  0 | [3](config/3.json)   | 129.146.247.135 | United States | US   | CLOUDFLARENET    | 2a09:bac1:76c0:e18::26a:2f | Yes (Region: US) |
|  1 | [4](config/4.json)   | 64.32.10.118    | United States | US   | SHARKTECH        | 64.32.10.114               | Yes (Region: US) |
|  2 | [8](config/8.json)   | 156.225.67.234  | United States | US   | CNSERVERS        | 23.225.9.234               | Yes (Region: US) |
|  3 | [15](config/15.json) | dl8.v001sssv.pw | France        | FR   | OVH SAS          | 51.178.24.58               | Yes (Region: FR) |
|  4 | [16](config/16.json) | 104.24.169.238  | United States | US   | DIGITALOCEAN-ASN | 164.90.159.137             | Yes (Region: US) |
|  5 | [19](config/19.json) | dl.v001sssv.pw  | France        | FR   | OVH SAS          | 51.77.213.73               | Yes (Region: FR) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDMiLCAiYWRkIjogIjEyOS4xNDYuMjQ3LjEzNSIsICJwb3J0IjogIjMyNTU5IiwgImlkIjogImMyNGI2MTcwLWJhNTQtNGIyYi05MmE3LWMwNDc0MGJmYzdiZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuMTAuMTE4IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYzUyOGQ4ZDgtOTRkNi00OGE5LThkZDMtNTI4OTI1NThhNmFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQxMTY5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDgiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjM0IiwgInBvcnQiOiAiNDgxMjMiLCAiaWQiOiAiOTM1MDNkZDUtMjQ1YS00ZWIxLWFlMmEtNTdhYjlmMmIzYzI5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmM1x1ZDgzY1x1ZGRmMU5MXHU4Mzc3XHU1MTcwKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE1IiwgImFkZCI6ICJkbDgudjAwMXNzc3YucHciLCAicG9ydCI6ICI4MCIsICJpZCI6ICIzZmVjNzE4Mi0wMmZiLTQ3MzAtOWI5Ny00YzlhZWU1NjNlZjYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImRsOC52MDAxc3Nzdi5wdyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICIxMDQuMjQuMTY5LjIzOCIsICJwb3J0IjogNDQzLCAiaWQiOiAiMWEyNWRjZTQtOWQyNy00ZThkLWU0NmUtMTYxOTliZTU0ZjgxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzdGFyLW9uZS5jZmQiLCAicGF0aCI6ICIvcG9ydHMvNDUzMTQiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiZGwudjAwMXNzc3YucHciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxOSIsICJwb3J0IjogODAsICJpZCI6ICJhNGJiN2Y5My1jZWU2LTQzZDctYjJkZC1mYTljNzBiODgyMzMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiZGwudjAwMXNzc3YucHciLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
```

