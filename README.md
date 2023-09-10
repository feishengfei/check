
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                 | cn            | cc   | isp                              | ip             | chatgpt          |
|---:|:---------------------|:-------------------------------------|:--------------|:-----|:---------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.4.56                           |               |      |                                  | 107.167.13.162 | Yes (Region: US) |
|  1 | [3](config/3.json)   | cfcdn2.sanfencdn.net                 | United States | US   | Akamai Connected Cloud           | 143.42.167.67  | Yes (Region: TW) |
|  2 | [5](config/5.json)   | 36.kccic2pa.xyz                      |               |      |                                  | 51.81.211.205  | Yes (Region: US) |
|  3 | [6](config/6.json)   | 39.kccic2pa.xyz                      |               |      |                                  | 51.81.211.205  | Yes (Region: US) |
|  4 | [8](config/8.json)   | 142.4.111.76                         |               |      |                                  | 54.36.174.181  | Yes (Region: FR) |
|  5 | [14](config/14.json) | gamespeed-gateway-1.numastergame.com |               |      |                                  | 61.219.15.82   | Yes (Region: TW) |
|  6 | [17](config/17.json) | cfcdn5.sanfencdn.net                 | Japan         | JP   | Eons Data Communications Limited | 38.207.152.110 | Yes (Region: US) |
|  7 | [20](config/20.json) | 172.64.153.211                       | Sweden        | SE   | Stark Industries Solutions Ltd   | 94.131.115.68  | Yes (Region: SE) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuNC41NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzU1NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDMiLCAiYWRkIjogImNmY2RuMi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiMjA1MiIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiY2ZkNDNmNjgtYTViZS00YzY3LWIxZTktNjg2ZTJlMTMxNWEyIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi96aC1jbiIsICJob3N0IjogInR3MS5zYW5mZW5jZG4yLmNvbSIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMzYua2NjaWMycGEueHl6IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIzYzFkZTU4ZC0wZGFjLTQwMDAtOWNjMy00MzMwZTFlNzM1NzgiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjUwMDM2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzE3XHU0ZWFjXHU1ZTAyXHU3OWZiXHU1MmE4IDUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMzkua2NjaWMycGEueHl6IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIzYzFkZTU4ZC0wZGFjLTQwMDAtOWNjMy00MzMwZTFlNzM1NzgiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjUwMDM5IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzE3XHU0ZWFjXHU1ZTAyXHU3OWZiXHU1MmE4IDYiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA4IiwgImFkZCI6ICIxNDIuNC4xMTEuNzYiLCAicG9ydCI6ICI0MjAwOSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwOTEzYjFhYy0xZjZjLTQzNmItOTliNC1hNWQ2ZTM0M2QwMjUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTE4NzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSAxNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE3IiwgImFkZCI6ICJjZmNkbjUuc2FuZmVuY2RuLm5ldCIsICJwb3J0IjogIjgwIiwgImlkIjogIjkwYmNlMDgxLTY0ZWMtNGVhZC1iMzFhLTFjYjMzZWFiYzhmOCIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAianAxLnNhbmZlbmNkbjIuY29tIiwgInBhdGgiOiAiL3poLWNuIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIwIiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI2ZTc1MTcxMi05NTY5LTUxODctODZlYS04ZjU4NWFkOTkxMDUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInBhdGgiOiAiL2FwaTAxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

