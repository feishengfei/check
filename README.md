
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn            | cc   | isp                              | ip                                   | chatgpt          |
|---:|:---------------------|:---------------------|:--------------|:-----|:---------------------------------|:-------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 156.245.8.247        | Netherlands   | NL   | YISP B.V.                        | 154.84.1.137                         | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 45.199.138.135       | Netherlands   | NL   | YISP B.V.                        | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  2 | [8](config/8.json)   | 173.245.49.236       | Poland        | PL   | OVH SAS                          | 54.36.174.181                        | Yes (Region: FR) |
|  3 | [17](config/17.json) | cfcdn2.sanfencdn.net | United States | US   | Eons Data Communications Limited | 38.207.156.104                       | Yes (Region: US) |
|  4 | [19](config/19.json) | 172.64.153.211       | Sweden        | SE   | Stark Industries Solutions Ltd   | 94.131.115.68                        | Yes (Region: SE) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjI0NyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjk2NGJmNDk5LTllYzAtNDM3OC05MmI2LTg3ZDhkODYxYjJkMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzOTMxNywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xMzUiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICI3NDNiZGM4Ny0xZGVhLTQxYmYtYWEwYi01MWRmYmJmZWM4YWEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjUxMTE5IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlTVVMVEFDT01cdTY3M2FcdTYyM2YgNCIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTVmMTdcdTU0MDlcdTVjM2NcdTRlOWFcdTVkZGVcdTk2M2ZcdTRlYzBcdTY3MmNOViBORVhUXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDgiLCAiYWRkIjogIjE3My4yNDUuNDkuMjM2IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiNWY3NTFjNmUtNTBiMS00Nzk3LWJhOGUtNmZmZTMyNGEwYmNlIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJjYS5pbG92ZXNjcC5jb20iLCAicGF0aCI6ICIvc2hpcmtlciIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiY2ZjZG4yLnNhbmZlbmNkbi5uZXQiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAxNyIsICJwb3J0IjogNDQzLCAiaWQiOiAiNDg4NDMyMzItNThlNy00MjlmLTkwZmItMzgwOTA3NGNjMGJiIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogInVzNC5zYW5mZW5jZG4xLmNvbSIsICJwYXRoIjogIi96aC1jbiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4yMTEiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAic2NoZXJlc3dlZC5zb2Z0d2FyZW5ld3Muc3RvcmUiLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkwMSIsICJwb3J0IjogIjQ0MyIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTkiLCAic2N5IjogImF1dG8iLCAic25pIjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
```

