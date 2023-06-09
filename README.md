
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn          | cc   | isp               | ip                   | chatgpt          |
|---:|:---------------------|:---------------|:------------|:-----|:------------------|:---------------------|:-----------------|
|  0 | [2](config/2.json)   | 156.225.67.71  | Netherlands | NL   | YISP B.V.         | 154.84.1.19          | Yes (Region: NL) |
|  1 | [8](config/8.json)   | 104.31.16.28   | Germany     | DE   | AS-GLOBALTELEHOST | 193.108.118.34       | Yes (Region: DE) |
|  2 | [14](config/14.json) | 139.99.180.115 | Australia   | AU   | OVH SAS           | 2402:1f00:8100:371:: | Yes (Region: AU) |
|  3 | [15](config/15.json) | 8.v2-ray.cyou  | Japan       | JP   | AMAZON-02         | 18.179.36.139        | Yes (Region: JP) |
|  4 | [17](config/17.json) | 120.241.117.55 | Singapore   | SG   | G-Core Labs S.A.  | 91.243.81.99         | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzEiLCAicG9ydCI6ICI0OTg1MiIsICJpZCI6ICIyMTE1NWVmZC04ZTI5LTQzZDItOTViYy1mZTMxOTBlY2IxYzYiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjEwNC4zMS4xNi4yOCIsICJwb3J0IjogIjgwIiwgImlkIjogIjU4ZmUxNTQyLTUyOTAtNDBhZC04MTVhLTc3NzA3YTgxYWZlNSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiY2E0LnRlaG1lMi5mdW4iLCAicGF0aCI6ICIvSU9lYmhMTWhsMUNUYkZIYkw5NW15ZlJYMiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2NPVkggMTQiLCAiYWRkIjogIjEzOS45OS4xODAuMTE1IiwgInBvcnQiOiAiNDk5MjEiLCAiaWQiOiAiNmMwNGEyNzMtNzMwMi00ZTA5LTljZWQtYWVkYWFhNzQ2MWFmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTUiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTIwLjI0MS4xMTcuNTUiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjc4OGU2NTc3LWVlOTktM2IyNy1iOGUzLTgxMTQxMWFlMzJhOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAzNzExMywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1ZTdmXHU0ZTFjXHU3NzAxXHU3OWZiXHU1MmE4IDE3IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

