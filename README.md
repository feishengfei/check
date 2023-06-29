
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn   | cc   | isp   | ip             | chatgpt          |
|---:|:---------------------|:---------------|:-----|:-----|:------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.99.91    |      |      |       | 142.4.99.65    | Yes (Region: US) |
|  1 | [3](config/3.json)   | 107.167.16.91  |      |      |       | 170.178.189.50 | Yes (Region: US) |
|  2 | [4](config/4.json)   | 156.249.18.159 |      |      |       | 154.84.1.134   | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 104.24.159.57  |      |      |       | 23.225.9.234   | Yes (Region: US) |
|  4 | [10](config/10.json) | dl.v001sssv.pw |      |      |       | 51.77.213.73   | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuOTkuOTEiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMzNzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTA3LjE2Ny4xNi45MSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjc2NDBhMWU3LTk3MDEtNDI4ZS1hNGIyLTE5YjNlN2RkNmY5ZiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NTY4OSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4xNTkiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlXHU4YzZhXHU3NjdiXHU3NzAxXHU3ZWE2XHU3ZmYwXHU1MTg1XHU2NWFmXHU1ODIxQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAicG9ydCI6IDQ4MTIzLCAiaWQiOiAiNjNiNGI4MjktN2YwMS00ZTI2LWIwMzctZjA0YjFmMDk4NzY1IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTA0LjI0LjE1OS41NyIsICJhaWQiOiAiMCIsICJlbmNyeXB0aW9uIjogImF1dG8iLCAiaG9zdCI6ICJ0eHgudnRjc3MudG9wIiwgImlkIjogIjk1NzJkNjkxLWUyN2EtNGY1NC1lZjRkLTU3NjAwYTc4NWI1NSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvcXdlcjAiLCAicG9ydCI6ICI4MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOCIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiBmYWxzZSwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidXJsX2dyb3VwIjogInYycmF5IiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICJkbC52MDAxc3Nzdi5wdyIsICJwb3J0IjogIjgwIiwgImlkIjogImE0YmI3ZjkzLWNlZTYtNDNkNy1iMmRkLWZhOWM3MGI4ODIzMyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGwudjAwMXNzc3YucHciLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

