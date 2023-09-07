
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr              | cn            | cc   | isp                                      | ip                             | chatgpt          |
|---:|:---------------------|:------------------|:--------------|:-----|:-----------------------------------------|:-------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 19.kccic2pa.xyz   | Japan         | JP   | Akamai Connected Cloud                   | 2400:8902::f03c:93ff:fe8a:d61d | Yes (Region: JP) |
|  1 | [4](config/4.json)   | 39.kccic2pa.xyz   | United States | US   | OVH SAS                                  | 51.81.211.205                  | Yes (Region: US) |
|  2 | [5](config/5.json)   | fusion.mlinuu.top | Taiwan        | TW   | Data Communication Business Group        | 36.227.243.144                 | Yes (Region: TW) |
|  3 | [8](config/8.json)   | 104.31.16.14      | Poland        | PL   | OVH SAS                                  | 54.36.174.181                  | Yes (Region: FR) |
|  4 | [12](config/12.json) | 162.159.58.231    | France        | FR   | SYNLINQ                                  | 103.252.90.249                 | Yes (Region: FR) |
|  5 | [14](config/14.json) | cloudqwq.cf       | France        | FR   | SYNLINQ                                  | 103.252.90.249                 | Yes (Region: FR) |
|  6 | [20](config/20.json) | 172.64.153.211    | Sweden        | SE   | Stark Industries Solutions Ltd           | 94.131.115.68                  | Yes (Region: SE) |
|  7 | [24](config/24.json) | 190.93.247.60     | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 38.102.234.249                 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMiIsICJhZGQiOiAiMTkua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMTkiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJhZWZjMzg5LTcyYjEtNGYyMy1iYmFkLTNhODVjZjUxZmU4YSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsICJob3N0IjogIjE5LmtjY2ljMnBhLnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggNCIsICJhZGQiOiAiMzkua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMzkiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJhZWZjMzg5LTcyYjEtNGYyMy1iYmFkLTNhODVjZjUxZmU4YSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL2Rvbmd0YWl3YW5nLmNvbSIsICJob3N0IjogIjM5LmtjY2ljMnBhLnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTYzNzdcdTUxNGIgIDUiLCAiYWRkIjogImZ1c2lvbi5tbGludXUudG9wIiwgInBvcnQiOiAiMTAwMDgiLCAidHlwZSI6ICJub25lIiwgImlkIjogImNlNmMzZWUwLWUwYmQtMzlkMi04YjQ5LTk3YzZhZGQzMjVjNiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogInYydHczLmRvdWJsZWRvdS5pY3UiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTA0LjMxLjE2LjE0IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImdiMXZtLmNkbi0wMy5saXZlIiwgImlkIjogImRhOGE5MzJhLTczYmMtNDc4Mi05OTU4LTJjN2UwMThlMTA1NCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvQGhvcGV2MnJheVx1MDYwY0Bob3BldjJyYXkiLCAicG9ydCI6ICI0NDMiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAic2N5IjogImF1dG8iLCAic25pIjogImdiMXZtLmNkbi0wMy5saXZlIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTYyLjE1OS41OC4yMzEiLCAiYWlkIjogMCwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAiaWQiOiAiY2QwYzU3MGYtNzU3Yy00OGQyLWExYjYtYzA5NDA0MzFjYzQ3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRFYXN5RE5TIEFueWNhc3RcdTgyODJcdTcwYjkoQ2xvdWRmbGFyZVx1ODI4Mlx1NzBiOSkgMTQiLCAiYWRkIjogImNsb3VkcXdxLmNmIiwgInBvcnQiOiA4MCwgImlkIjogImNkMGM1NzBmLTc1N2MtNDhkMi1hMWI2LWMwOTQwNDMxY2M0NyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAibmwxMGdicHMuNjU3NzYxNy54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIwIiwgImFkZCI6ICIxNzIuNjQuMTUzLjIxMSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNmU3NTE3MTItOTU2OS01MTg3LTg2ZWEtOGY1ODVhZDk5MTA1IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJzY2hlcmVzd2VkLnNvZnR3YXJlbmV3cy5zdG9yZSIsICJwYXRoIjogIi9hcGkwMSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI0IiwgImFkZCI6ICIxOTAuOTMuMjQ3LjYwIiwgInBvcnQiOiAiMjA5NSIsICJpZCI6ICIyYzRkYjBiMS01Y2Q5LTRiYWQtZTk1Ny0zM2MzNmUyNjE5ODciLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIjgud3loa2FhMC5ncSIsICJwYXRoIjogIi9URzpAaGthYTAiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI1IiwgImFkZCI6ICIxNzIuNjcuMjExLjE5IiwgInBvcnQiOiAiMjA5NSIsICJpZCI6ICIzMmFmNDAwNi0wNjk4LTQ5MTAtODA2Yy1iODEzMDc0ZjM2ZWIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIjEzLnd5aGthYTAuZ3EiLCAicGF0aCI6ICIvVEc6QGhrYWEwIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

