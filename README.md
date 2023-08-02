
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                       | cn            | cc   | isp                               | ip             | chatgpt          |
|---:|:---------------------|:---------------------------|:--------------|:-----|:----------------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 107.167.29.93              | United States | US   | SHARKTECH                         | 107.167.9.234  | Yes (Region: US) |
|  1 | [5](config/5.json)   | 67.21.84.216               | United States | US   | SHARKTECH                         | 67.21.85.2     | Yes (Region: US) |
|  2 | [7](config/7.json)   | 45.58.186.81               | United States | US   | SHARKTECH                         | 64.32.2.26     | Yes (Region: US) |
|  3 | [8](config/8.json)   | dj.shabijichang.com        | Hong Kong     | HK   | CNSERVERS                         | 172.247.175.42 | Yes (Region: US) |
|  4 | [10](config/10.json) | tw98-1g-hinet.mytls888.com | Taiwan        | TW   | Data Communication Business Group | 61.224.87.162  | Yes (Region: TW) |
|  5 | [12](config/12.json) | tw99-hinet.mynodes001.one  | Taiwan        | TW   | Data Communication Business Group | 61.224.86.92   | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTA3LjE2Ny4yOS45MyIsICJwb3J0IjogIjQ1NTg1IiwgImlkIjogIjQ2NWRlYzFhLWUwOWItNGJiNi05OTA1LTcwZjc1ZDYwMzVjOCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE2IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrVGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA1IiwgInBvcnQiOiA0NzA4OCwgImlkIjogImI5YTMwNWE5LTFmZjItNGVjMS1iMzM4LTkzMzU1NTgzM2JhYSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiNDUuNTguMTg2LjgxIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDUxMTQwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiZGouc2hhYmlqaWNoYW5nLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJkai5zaGFiaWppY2hhbmcuY29tIiwgImlkIjogIjQ5ZDkxOTI4LTI3NWMtNDk2Yy1iOWYzLTBmMjA0YTkxMjUzYyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAidHc5OC0xZy1oaW5ldC5teXRsczg4OC5jb20iLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1M2YwXHU2ZTdlXHU3NzAxXHU1M2YwXHU0ZTJkXHU1ZTAyXHU0ZTJkXHU1MzRlXHU3NTM1XHU0ZmUxIDEwIiwgInBvcnQiOiA1NTQsICJpZCI6ICIyMGU4YjU4MC0zYzExLTMwMTctYTg0MC1lYjYyNGI0ODMzMjQiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTUzZjBcdTRlMmRcdTVlMDJcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMTIiLCAiYWRkIjogInR3OTktaGluZXQubXlub2RlczAwMS5vbmUiLCAicG9ydCI6ICI1NTQiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjIwZThiNTgwLTNjMTEtMzAxNy1hODQwLWViNjI0YjQ4MzMyNCIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogInR3OTktaGluZXQubXlub2RlczAwMS5vbmUiLCAidGxzIjogIiJ9
```

