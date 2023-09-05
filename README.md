
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                 | cn             | cc   | isp                                      | ip             | chatgpt          |
|---:|:---------------------|:-------------------------------------|:---------------|:-----|:-----------------------------------------|:---------------|:-----------------|
|  0 | [4](config/4.json)   | gamespeed-gateway-1.numastergame.com | Taiwan         | TW   | Data Communication Business Group        | 61.219.15.82   | Yes (Region: TW) |
|  1 | [5](config/5.json)   | 104.17.199.183                       | United States  | US   | Zhejiang Aiyun Network Technology Co Ltd | 45.137.97.140  | Yes (Region: US) |
|  2 | [8](config/8.json)   | 216.24.57.1                          | Poland         | PL   | OVH SAS                                  | 54.36.174.181  | Yes (Region: FR) |
|  3 | [14](config/14.json) | cloudqwq.cf                          | France         | FR   | SYNLINQ                                  | 103.252.90.249 | Yes (Region: FR) |
|  4 | [18](config/18.json) | odelia.autos                         | United Kingdom | GB   | AS-GLOBALTELEHOST                        | 149.7.16.88    | Yes (Region: GB) |
|  5 | [31](config/31.json) | 172.64.153.211                       | Sweden         | SE   | Stark Industries Solutions Ltd           | 94.131.115.68  | Yes (Region: SE) |
|  6 | [35](config/35.json) | 3.wyhkaa0.gq                         | United States  | US   | Zhejiang Aiyun Network Technology Co Ltd | 38.102.235.8   | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwOTEzYjFhYy0xZjZjLTQzNmItOTliNC1hNWQ2ZTM0M2QwMjUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTE4NzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSA0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDUiLCAiYWRkIjogIjEwNC4xNy4xOTkuMTgzIiwgInBvcnQiOiAyMDk1LCAiaWQiOiAiYTA0ZTI5MjMtMWE5Ni00OTk4LWVjODktMjYzNGY3MTk3ZWJmIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICIxMi53eWhrYWEwLmdxIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMjE2LjI0LjU3LjEiLCAiYWlkIjogMCwgImhvc3QiOiAiZGQyLjE4MDguY2YiLCAiaWQiOiAiYTdlZTg1ZjQtMjUyOC00MTJlLTk5NGYtY2U2NWY1NDc1NGU0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogImE3ZWU4NWY0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NWRkZSA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2xvdWRxd3EuY2YiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRFYXN5RE5TIEFueWNhc3RcdTgyODJcdTcwYjkoQ2xvdWRmbGFyZVx1ODI4Mlx1NzBiOSkgMTQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAib2RlbGlhLmF1dG9zIiwgImFpZCI6IDEsICJob3N0IjogIiIsICJpZCI6ICIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCAibmV0IjogIndzIiwgInBhdGgiOiAibGlua3Z3cyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhZXMtMTI4LWdjbSIsICJzZWN1cml0eSI6ICJhZXMtMTI4LWdjbSIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDMxIiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI2ZTc1MTcxMi05NTY5LTUxODctODZlYS04ZjU4NWFkOTkxMDUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNjaGVyZXN3ZWQuc29mdHdhcmVuZXdzLnN0b3JlIiwgInBhdGgiOiAiL2FwaTAxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDM1IiwgImFkZCI6ICIzLnd5aGthYTAuZ3EiLCAicG9ydCI6ICIyMDk1IiwgImlkIjogIjAxNTBlYWMxLTZlNDktNDMyOS05YzA2LTUwMDI3YzBiOWFkNyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiMy53eWhrYWEwLmdxIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

