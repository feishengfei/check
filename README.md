
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp              | ip                        | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------------|:--------------------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.20.97    | United States | US   | SHARKTECH        | 64.32.0.58                | Yes (Region: US) |
|  1 | [4](config/4.json)   | 67.21.64.84    | United States | US   | SHARKTECH        | 67.21.72.34               | Yes (Region: US) |
|  2 | [5](config/5.json)   | 74.217.182.119 | United States | US   | DEDIPATH-LLC     | 45.15.147.130             | Yes (Region: US) |
|  3 | [21](config/21.json) | 219.76.13.183  | Singapore     | SG   | Datacamp Limited | 5.180.78.163              | Yes (Region: SG) |
|  4 | [27](config/27.json) | Shopify.com    | France        | FR   | CLOUDFLARENET    | 2a09:bac5:3264:be::13:266 | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMjAuOTciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJjMWJhZDlhNi0xNDgyLTQ5NDEtYTBjNC1lODVmM2NiYmNiNWEiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDAwMzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNlNoYXJrdGVjaFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiNjcuMjEuNjQuODQiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQzMTIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDUiLCAiYWRkIjogIjc0LjIxNy4xODIuMTE5IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy42Mjk3NjE3MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkxNzI4NDg1MjU0IiwgInRscyI6ICJ0bHMiLCAic25pIjogInd3dy42Mjk3NjE3MS54eXoifQ==
vmess://eyJhZGQiOiAiMjE5Ljc2LjEzLjE4MyIsICJhaWQiOiAxLCAiaG9zdCI6ICJhLmRiLWxpbmsuaW4iLCAiaWQiOiAiN2ZjYjRhMjctZjgxOC0zMzc3LWFmNTYtY2MwOGJjYjQyYjVkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9kYiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTc1MzVcdThiYWZcdTc2YzhcdTc5ZDFcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggMjEiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiU2hvcGlmeS5jb20iLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOShzaG9waWZ5KSAyNyIsICJwb3J0IjogMjA4NiwgImlkIjogIjI1MGY0MzMxLThjM2UtNGI4Ny1hODZiLTVjNWZiZjlkZGJhOCIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJGci5jbG91ZGZsYXJlLnF1ZXN0IiwgInBhdGgiOiAiL2FyaWVzIiwgInRscyI6ICIifQ==
```

