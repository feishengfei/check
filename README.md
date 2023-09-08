
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                       | cn            | cc   | isp                                      | ip             | chatgpt          |
|---:|:---------------------|:---------------------------|:--------------|:-----|:-----------------------------------------|:---------------|:-----------------|
|  0 | [4](config/4.json)   | cloudqwq.cf                | France        | FR   | SYNLINQ                                  | 103.252.90.249 | Yes (Region: FR) |
|  1 | [6](config/6.json)   | 162.159.58.231             | France        | FR   | SYNLINQ                                  | 103.252.90.249 | Yes (Region: FR) |
|  2 | [8](config/8.json)   | cf-test.q5wrff7jtkdg23.top | Poland        | PL   | OVH SAS                                  | 54.36.174.181  | Yes (Region: FR) |
|  3 | [16](config/16.json) | 172.64.153.211             | Sweden        | SE   | Stark Industries Solutions Ltd           | 94.131.115.68  | Yes (Region: SE) |
|  4 | [22](config/22.json) | 188.114.97.203             | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 38.102.235.8   | Yes (Region: US) |
|  5 | [26](config/26.json) | 190.93.247.60              | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 38.102.234.249 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRFYXN5RE5TIEFueWNhc3RcdTgyODJcdTcwYjkoQ2xvdWRmbGFyZVx1ODI4Mlx1NzBiOSkgNCIsICJhZGQiOiAiY2xvdWRxd3EuY2YiLCAicG9ydCI6IDgwLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJubDEwZ2Jwcy42NTc3NjE3Lnh5eiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTYyLjE1OS41OC4yMzEiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDYiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLXRlc3QucTV3cmZmN2p0a2RnMjMudG9wIiwgInBvcnQiOiAiMjA4MiIsICJpZCI6ICI0NDQ2MDJkYi02OThjLTQ5YmQtYjNiMS1iMTcxZmIwNTQzYjkiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNnLXYzMy5xNXdyZmY3anRrZGcyMy50b3AiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzY2hlcmVzd2VkLnNvZnR3YXJlbmV3cy5zdG9yZSIsICJwYXRoIjogIi9hcGkwMSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVkZjRcdTg5N2ZcdTU3MjNcdTRmZGRcdTdmNTdDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIyIiwgImFkZCI6ICIxODguMTE0Ljk3LjIwMyIsICJwb3J0IjogIjIwOTUiLCAiaWQiOiAiMDE1MGVhYzEtNmU0OS00MzI5LTljMDYtNTAwMjdjMGI5YWQ3IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIzLnd5aGthYTAuZ3EiLCAicGF0aCI6ICIvVEc6QGhrYWEwIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI2IiwgImFkZCI6ICIxOTAuOTMuMjQ3LjYwIiwgInBvcnQiOiAiMjA5NSIsICJpZCI6ICIyYzRkYjBiMS01Y2Q5LTRiYWQtZTk1Ny0zM2MzNmUyNjE5ODciLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIjgud3loa2FhMC5ncSIsICJwYXRoIjogIi9URzpAaGthYTAiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

