
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                              | ip              | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:---------------------------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 38.63.0.93          | United States | US   | PEGTECHINC                       | 38.63.0.65      | Yes (Region: US) |
|  1 | [3](config/3.json)   | 23.225.117.35       | United States | US   | CNSERVERS                        | 172.247.194.6   | Yes (Region: US) |
|  2 | [4](config/4.json)   | 45.58.186.83        | United States | US   | SHARKTECH                        | 64.32.2.26      | Yes (Region: US) |
|  3 | [5](config/5.json)   | 64.32.24.210        | United States | US   | SHARKTECH                        | 170.178.189.58  | Yes (Region: US) |
|  4 | [8](config/8.json)   | 185.143.220.25      | United States | US   | AS-GLOBALTELEHOST                | 169.197.141.187 | Yes (Region: US) |
|  5 | [19](config/19.json) | cfcdn.sanfencdn.net | United States | US   | Eons Data Communications Limited | 65.75.221.195   | Yes (Region: US) |
|  6 | [24](config/24.json) | 8.v2-ray.cyou       | Japan         | JP   | AMAZON-02                        | 18.179.36.139   | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiMzguNjMuMC45MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NzAwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MzRlXHU3NmRiXHU5ODdmQ29nZW50XHU5MDFhXHU0ZmUxXHU1MTZjXHU1M2Y4IDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDZXJhTmV0d29ya3MgMyIsICJhZGQiOiAiMjMuMjI1LjExNy4zNSIsICJwb3J0IjogIjQ4ODI5IiwgImlkIjogImJiMjU4NTllLWY2ZGEtNDEwMS05ODlmLWI0ZGQ2N2EyMjY4MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNDUuNTguMTg2LjgzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDUxMTQwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjEwIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ4NjU5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmYzRcdTdmNTdcdTY1YWYgIDgiLCAiYWRkIjogIjE4NS4xNDMuMjIwLjI1IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImYyOGUzNTRlLWMyZDEtNDk4My05YjA3LTVhY2FmMWIzYjNlNSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLzZlOUV0WjJkTCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE5IiwgImFkZCI6ICJjZmNkbi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImRkODMxNGNjLTM3NTQtNDE2ZC05NDU2LTA5OTFmMmU3NDc1MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMyLnNhbmZlbmNkbi5uZXQiLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMjQiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

