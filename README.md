
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn            | cc   | isp                              | ip             | chatgpt          |
|---:|:---------------------|:-----------------------|:--------------|:-----|:---------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 45.199.138.182         | Netherlands   | NL   | YISP B.V.                        | 154.84.1.229   | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 46.182.107.22          | Netherlands   | NL   | YISP B.V.                        | 154.84.1.16    | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.249.18.218         | Netherlands   | NL   | YISP B.V.                        | 154.84.1.138   | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 0001.sg.genzpn.com     | Poland        | PL   | OVH SAS                          | 54.36.174.181  | Yes (Region: FR) |
|  4 | [18](config/18.json) | 172.64.153.211         | Sweden        | SE   | Stark Industries Solutions Ltd   | 94.131.115.68  | Yes (Region: SE) |
|  5 | [27](config/27.json) | cfcdn2.sanfencdn.net   | United States | US   | Eons Data Communications Limited | 38.207.156.104 | Yes (Region: US) |
|  6 | [28](config/28.json) | 9524.outline-vpn.cloud | Sweden        | SE   | M247 Europe SRL                  | 37.120.209.122 | Yes (Region: SE) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAyIiwgImFkZCI6ICI0NS4xOTkuMTM4LjE4MiIsICJwb3J0IjogIjMxMjg1IiwgImlkIjogImQzMTMzNDg0LWYyYmYtNGIwYy04ZDM4LWY4ZTY0NWI2NTY4NyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNDYuMTgyLjEwNy4yMiIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3Ljg2MTM5MzE3Lnh5eiIsICJpZCI6ICJkZTQ5MTgwMi0yMzNlLTQ3ZjItOGM2Yy1kMTliY2Y1YmQ1NmIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTY5MzIwMDE5ODA4NyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzAgIDMiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4yMTgiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy4xMTY0OTc2OS54eXoiLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTM0ODAyMzI3ODQiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlXHU4YzZhXHU3NjdiXHU3NzAxXHU3ZWE2XHU3ZmYwXHU1MTg1XHU2NWFmXHU1ODIxQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMDAwMS5zZy5nZW56cG4uY29tIiwgImFpZCI6IDAsICJob3N0IjogIjAwMDEuc2cuZ2VuenBuLmNvbSIsICJpZCI6ICJjNzgyMzczMy1kZmM5LTQzMGQtYTdjZi1jMzMwMmY5NjI3ZDYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4yMTEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAic2NoZXJlc3dlZC5zb2Z0d2FyZW5ld3Muc3RvcmUiLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkwMSIsICJwb3J0IjogIjQ0MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTgiLCAic2N5IjogImF1dG8iLCAic25pIjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiY2ZjZG4yLnNhbmZlbmNkbi5uZXQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyNyIsICJwb3J0IjogNDQzLCAiaWQiOiAiNDg4NDMyMzItNThlNy00MjlmLTkwZmItMzgwOTA3NGNjMGJiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogInVzNC5zYW5mZW5jZG4xLmNvbSIsICJwYXRoIjogIi96aC1jbiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiOTUyNC5vdXRsaW5lLXZwbi5jbG91ZCIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogImRjMGNmMjJkLWUzNWMtNGI3Ny04OTI0LTk3N2Y2ODQ0OTA5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNDk5ODIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmNTdcdTlhNmNcdTVjM2NcdTRlOWEgIDI4IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIm5vbmUiLCAidiI6ICIyIn0=
```

