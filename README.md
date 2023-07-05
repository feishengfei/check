
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn   | cc   | isp   | ip              | chatgpt          |
|---:|:---------------------|:--------------------|:-----|:-----|:------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 154.85.1.245        |      |      |       | 154.84.1.206    | Yes (Region: NL) |
|  1 | [7](config/7.json)   | cfcdn.sanfencdn.net |      |      |       | 104.237.159.122 | Yes (Region: US) |
|  2 | [8](config/8.json)   | ns1.v2-vip.fun      |      |      |       | 23.225.9.234    | Yes (Region: US) |
|  3 | [13](config/13.json) | 107.148.194.238     |      |      |       | 107.148.194.225 | Yes (Region: US) |
|  4 | [15](config/15.json) | 149.28.94.183       |      |      |       | 149.28.94.183   | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ1IiwgInBvcnQiOiAiNDc3MzEiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiY2ZjZG4uc2FuZmVuY2RuLm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICJ1czQuc2FuZmVuY2RuMS5jb20iLCAiaWQiOiAiZjExNGU2ZDktMGNkYS00ZmU4LWI3NjktM2JjZWIzYmNhNDUzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi96aC1jbiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDciLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAibnMxLnYyLXZpcC5mdW4iLCAiYWlkIjogMCwgImhvc3QiOiAiZGUxNC5pcnRlaC5mdW4iLCAiaWQiOiAiNGY4NTkxNDktMmIyZi00YjkwLTlhMmMtOGMwZmUxNWM4YzRjIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9velg5YVVQaUpWdG9MYXZqVFciLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAxMyIsICJhZGQiOiAiMTA3LjE0OC4xOTQuMjM4IiwgInBvcnQiOiAiNTU1MDQiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIxNTIuNzAuNzQuNjYiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDaG9vcGFcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTUiLCAiYWRkIjogIjE0OS4yOC45NC4xODMiLCAicG9ydCI6ICIxMDAwMiIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiZTBiNzE1Y2QtNDA1OC00Y2Y0LWI2N2UtZDM3MDYzMjk0Yjc1IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL2h1YXdlaSIsICJob3N0IjogImNsb3VkZmxhcmUucGlhb2xlLm1lIiwgInRscyI6ICIifQ==
```

