
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp                                      | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------------------------------------|:---------------|:-----------------|
|  0 | [6](config/6.json)   | 38.75.137.27   | United States | US   | AS-GLOBALTELEHOST                        | 38.75.137.27   | Yes (Region: US) |
|  1 | [8](config/8.json)   | yd1.992688.xyz | Poland        | PL   | OVH SAS                                  | 54.36.174.181  | Yes (Region: FR) |
|  2 | [14](config/14.json) | cloudqwq.cf    | France        | FR   | SYNLINQ                                  | 103.252.90.249 | Yes (Region: FR) |
|  3 | [15](config/15.json) | 162.159.58.231 | France        | FR   | SYNLINQ                                  | 103.252.90.249 | Yes (Region: FR) |
|  4 | [16](config/16.json) | 172.64.153.211 | Sweden        | SE   | Stark Industries Solutions Ltd           | 94.131.115.68  | Yes (Region: SE) |
|  5 | [23](config/23.json) | 172.67.211.19  | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 45.137.97.241  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMzguNzUuMTM3LjI3IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwNDYyMWJhZS1hYjM2LTExZWMtYjkwOS0wMjQyYWMxMjAwMDIiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMjIzMjQsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTM0ZVx1NzZkYlx1OTg3ZkNvZ2VudFx1OTAxYVx1NGZlMVx1NTE2Y1x1NTNmOCA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInlkMS45OTI2ODgueHl6IiwgInBvcnQiOiAiODg4MCIsICJpZCI6ICIyZmMyNDhkNS03YzgxLTQ3MWQtYzJjZi1hMTRlN2Y1YWVkMmQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInZjZXUzLnZwbjY2LmV1Lm9yZyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRFYXN5RE5TIEFueWNhc3RcdTgyODJcdTcwYjkoQ2xvdWRmbGFyZVx1ODI4Mlx1NzBiOSkgMTQiLCAiYWRkIjogImNsb3VkcXdxLmNmIiwgInBvcnQiOiA4MCwgImlkIjogImNkMGM1NzBmLTc1N2MtNDhkMi1hMWI2LWMwOTQwNDMxY2M0NyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTYyLjE1OS41OC4yMzEiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzY2hlcmVzd2VkLnNvZnR3YXJlbmV3cy5zdG9yZSIsICJwYXRoIjogIi9hcGkwMSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIzIiwgImFkZCI6ICIxNzIuNjcuMjExLjE5IiwgInBvcnQiOiAiMjA5NSIsICJpZCI6ICIzMmFmNDAwNi0wNjk4LTQ5MTAtODA2Yy1iODEzMDc0ZjM2ZWIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIjEzLnd5aGthYTAuZ3EiLCAicGF0aCI6ICIvVEc6QGhrYWEwIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

