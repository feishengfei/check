
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn             | cc   | isp                           | ip                         | chatgpt          |
|---:|:---------------------|:------------------------|:---------------|:-----|:------------------------------|:---------------------------|:-----------------|
|  0 | [2](config/2.json)   | 156.225.67.223          |                |      |                               | 154.84.1.136               | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 45.199.138.4            |                |      |                               | 46.182.107.123             | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 129.146.247.135         | United States  | US   | CLOUDFLARENET                 | 2a09:bac1:76c0:e18::26a:2f | Yes (Region: US) |
|  3 | [5](config/5.json)   | 156.245.8.142           | Netherlands    | NL   | YISP B.V.                     | 154.84.1.139               | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 156.225.67.151          | Netherlands    | NL   | YISP B.V.                     | 154.84.1.194               | Yes (Region: NL) |
|  5 | [7](config/7.json)   | 83.142.225.32           | United Kingdom | GB   | Iomart Cloud Services Limited | 83.142.225.28              | Yes (Region: GB) |
|  6 | [10](config/10.json) | cn-to-hk-443.db-link.in | United States  | US   | PONYNET                       | 205.185.118.164            | Yes (Region: US) |
|  7 | [13](config/13.json) | dl.v001sssv.pw          | France         | FR   | OVH SAS                       | 51.77.213.73               | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4yMjMiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJlYmVjMmFkZi1lOTQwLTQ0NmYtYmVkNC1kOGM5MTE0M2I1NGEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDgwMjEsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC40IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiZjlmYTNhOWMtZjdkNS00MTRmLTg4ZTYtNjk3MDU4NWQ5OTQ5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3NzkzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTI5LjE0Ni4yNDcuMTM1IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJjMjRiNjE3MC1iYTU0LTRiMmItOTJhNy1jMDQ3NDBiZmM3YmYiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjMyNTU4IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkICA0IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0MiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTExMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTUxIiwgInBvcnQiOiAiNDUzMTQiLCAidHlwZSI6ICJub25lIiwgImlkIjogImE3ZmE4ZjE0LTRmYjYtNDI4MC05MDA1LWQ2YmJlOTljNWRhOSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgyZjFcdTU2ZmQgIDciLCAiYWRkIjogIjgzLjE0Mi4yMjUuMzIiLCAicG9ydCI6ICI0OTkyMCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNTI2N2NhNzEtOTdlNi00NGM4LThmYjUtOWZlNGFmZTA5NTRlIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMmRcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgMTAiLCAiYWRkIjogImNuLXRvLWhrLTQ0My5kYi1saW5rLmluIiwgInBvcnQiOiA0NDMsICJpZCI6ICI0MGNiYzc1MC1hMTgyLTNmZTItODgzMi05ZmE2MDA2MzU0Y2YiLCAiYWlkIjogMSwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImZyZWUtdG8tdXMtMDEuZGItbGluay5pbiIsICJwYXRoIjogIi9kYiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEzIiwgImFkZCI6ICJkbC52MDAxc3Nzdi5wdyIsICJwb3J0IjogIjgwIiwgImlkIjogImE0YmI3ZjkzLWNlZTYtNDNkNy1iMmRkLWZhOWM3MGI4ODIzMyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGwudjAwMXNzc3YucHciLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

