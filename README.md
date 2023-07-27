
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn   | cc   | isp   | ip                                  | chatgpt          |
|---:|:---------------------|:----------------------|:-----|:-----|:------|:------------------------------------|:-----------------|
|  0 | [4](config/4.json)   | 156.245.8.129         |      |      |       | 154.84.1.164                        | Yes (Region: NL) |
|  1 | [6](config/6.json)   | 156.249.18.36         |      |      |       | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: US) |
|  2 | [8](config/8.json)   | 156.245.8.143         |      |      |       | 154.84.1.230                        | Yes (Region: NL) |
|  3 | [15](config/15.json) | sw-94.131.10.5.nip.io |      |      |       | 94.131.10.5                         | Yes (Region: PT) |
|  4 | [19](config/19.json) | 173.82.55.92          |      |      |       | 23.234.230.34                       | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjEyOSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0ODEyMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTU2LjI0OS4xOC4zNiIsICJwb3J0IjogIjQ4MjIyIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIva3BseHZ3cyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE0MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogNDkxNTUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZiAgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAic3ctOTQuMTMxLjEwLjUubmlwLmlvIiwgImFpZCI6ICIwIiwgImVuY3J5cHRpb24iOiAiYXV0byIsICJob3N0IjogImludGVybmV0LmxpZmUuY29tLmJ5IiwgImlkIjogIjg4ZDQ3NmMxLTQ4ZjctNGQzZC1hMGU2LWFjY2NiZmYwMmRiNiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDQzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZTRjXHU1MTRiXHU1MTcwICAxNSIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiBmYWxzZSwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidXJsX2dyb3VwIjogInYycmF5IiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTczLjgyLjU1LjkyIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDE5IiwgInBvcnQiOiAzNDQxMiwgImlkIjogIjgyNjIwYTZlLWRiZmQtNGQ1Ny04YTU5LTkwMDRhNGJiOWU5MiIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

