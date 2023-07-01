
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp        | ip            | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------|:--------------|:-----------------|
|  0 | [3](config/3.json)   | 170.178.162.137 | United States | US   | SHARKTECH  | 107.167.22.10 | Yes (Region: US) |
|  1 | [4](config/4.json)   | 142.4.99.90     | China         | CN   | PEGTECHINC | 142.4.99.65   | Yes (Region: US) |
|  2 | [5](config/5.json)   | 45.199.138.11   | Netherlands   | NL   | YISP B.V.  | 154.84.1.230  | Yes (Region: NL) |
|  3 | [6](config/6.json)   | 156.225.67.234  | Netherlands   | NL   | YISP B.V.  | 154.84.1.178  | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 162.159.142.203 | United States | US   | CNSERVERS  | 23.225.9.234  | Yes (Region: US) |
|  5 | [18](config/18.json) | dl.v001sssv.pw  | France        | FR   | OVH SAS    | 51.77.213.73  | Yes (Region: FR) |
|  6 | [21](config/21.json) | dl8.v001sssv.pw | France        | FR   | OVH SAS    | 51.178.24.58  | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiMTcwLjE3OC4xNjIuMTM3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDUxMjE3LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTQyLjQuOTkuOTAiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMzNzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjY1ZWE2NzI3LTQ0NjEtNDdhNy1hNWM0LWZlZjJjNjdmMmY3OSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTEyMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjM0IiwgInBvcnQiOiAiNDgxMjMiLCAiaWQiOiAiOTM1MDNkZDUtMjQ1YS00ZWIxLWFlMmEtNTdhYjlmMmIzYzI5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmM1x1ZDgzY1x1ZGRmMU5MXHU4Mzc3XHU1MTcwKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTYyLjE1OS4xNDIuMjAzIiwgImFpZCI6IDAsICJob3N0IjogImRlMy5teWJlc3Rqai5jb20iLCAiaWQiOiAiNmUxZmRjMTItMjE0Yi00MjdmLTg4YmItNTk5YzUzNjQwN2VhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8xNjU0NDMxIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiZGwudjAwMXNzc3YucHciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxOCIsICJwb3J0IjogODAsICJpZCI6ICJhNGJiN2Y5My1jZWU2LTQzZDctYjJkZC1mYTljNzBiODgyMzMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiZGwudjAwMXNzc3YucHciLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIxIiwgImFkZCI6ICJkbDgudjAwMXNzc3YucHciLCAicG9ydCI6ICI4MCIsICJpZCI6ICIzZmVjNzE4Mi0wMmZiLTQ3MzAtOWI5Ny00YzlhZWU1NjNlZjYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImRsOC52MDAxc3Nzdi5wdyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

