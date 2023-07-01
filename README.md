
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp              | ip             | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | dl8.v001sssv.pw | France        | FR   | OVH SAS          | 51.178.24.58   | Yes (Region: FR) |
|  1 | [4](config/4.json)   | 156.225.67.234  | Netherlands   | NL   | YISP B.V.        | 154.84.1.178   | Yes (Region: NL) |
|  2 | [8](config/8.json)   | ns1.v2-vip.fun  | United States | US   | CNSERVERS        | 23.225.9.234   | Yes (Region: US) |
|  3 | [11](config/11.json) | dl.v001sssv.pw  | France        | FR   | OVH SAS          | 51.77.213.73   | Yes (Region: FR) |
|  4 | [12](config/12.json) | 104.24.169.238  | United States | US   | DIGITALOCEAN-ASN | 164.90.159.137 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDIiLCAiYWRkIjogImRsOC52MDAxc3Nzdi5wdyIsICJwb3J0IjogIjgwIiwgImlkIjogIjNmZWM3MTgyLTAyZmItNDczMC05Yjk3LTRjOWFlZTU2M2VmNiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGw4LnYwMDFzc3N2LnB3IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDQiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjM0IiwgInBvcnQiOiAiNDgxMjMiLCAiaWQiOiAiOTM1MDNkZDUtMjQ1YS00ZWIxLWFlMmEtNTdhYjlmMmIzYzI5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmM1x1ZDgzY1x1ZGRmMU5MXHU4Mzc3XHU1MTcwKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAibnMxLnYyLXZpcC5mdW4iLCAiYWlkIjogMCwgImhvc3QiOiAiZGUxNC5pcnRlaC5mdW4iLCAiaWQiOiAiNGY4NTkxNDktMmIyZi00YjkwLTlhMmMtOGMwZmUxNWM4YzRjIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9velg5YVVQaUpWdG9MYXZqVFciLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiZGwudjAwMXNzc3YucHciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMSIsICJwb3J0IjogODAsICJpZCI6ICJhNGJiN2Y5My1jZWU2LTQzZDctYjJkZC1mYTljNzBiODgyMzMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiZGwudjAwMXNzc3YucHciLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICIxMDQuMjQuMTY5LjIzOCIsICJwb3J0IjogNDQzLCAiaWQiOiAiMWEyNWRjZTQtOWQyNy00ZThkLWU0NmUtMTYxOTliZTU0ZjgxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzdGFyLW9uZS5jZmQiLCAicGF0aCI6ICIvcG9ydHMvNDUzMTQiLCAidGxzIjogInRscyJ9
```

