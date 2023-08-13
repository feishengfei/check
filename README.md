
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                 | cn            | cc   | isp                               | ip            | chatgpt          |
|---:|:---------------------|:-------------------------------------|:--------------|:-----|:----------------------------------|:--------------|:-----------------|
|  0 | [4](config/4.json)   | 67.21.64.84                          | United States | US   | SHARKTECH                         | 67.21.72.34   | Yes (Region: US) |
|  1 | [7](config/7.json)   | 74.217.182.119                       | United States | US   | DEDIPATH-LLC                      | 45.15.147.130 | Yes (Region: US) |
|  2 | [9](config/9.json)   | gamespeed-gateway-1.numastergame.com | Taiwan        | TW   | Data Communication Business Group | 61.219.15.82  | Yes (Region: TW) |
|  3 | [16](config/16.json) | 156.245.8.145                        | Netherlands   | NL   | YISP B.V.                         | 154.84.1.134  | Yes (Region: NL) |
|  4 | [26](config/26.json) | 219.76.13.183                        | Singapore     | SG   | Datacamp Limited                  | 5.180.78.163  | Yes (Region: SG) |

## Valid
```
vmess://eyJhZGQiOiAiNjcuMjEuNjQuODQiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICIyNTY2ZDAwZi0yMThjLTQ4ZjctOWEzNi0xM2QzZDZmMWE3MjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQzMTIzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDQiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAibm9uZSIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDciLCAiYWRkIjogIjc0LjIxNy4xODIuMTE5IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy42Mjk3NjE3MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkxNzI4NDg1MjU0IiwgInRscyI6ICJ0bHMiLCAic25pIjogInd3dy42Mjk3NjE3MS54eXoifQ==
vmess://eyJhZGQiOiAiZ2FtZXNwZWVkLWdhdGV3YXktMS5udW1hc3RlcmdhbWUuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIwOTEzYjFhYy0xZjZjLTQzNmItOTliNC1hNWQ2ZTM0M2QwMjUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMTE4NzIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSA5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE2IiwgImFkZCI6ICIxNTYuMjQ1LjguMTQ1IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjYzYjRiODI5LTdmMDEtNGUyNi1iMDM3LWYwNGIxZjA5ODc2NSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4zMjE1OTg3Ny54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkxNzUwMjU5MDEyIiwgInRscyI6ICJ0bHMiLCAic25pIjogInd3dy4zMjE1OTg3Ny54eXoifQ==
vmess://eyJhZGQiOiAiMjE5Ljc2LjEzLjE4MyIsICJhaWQiOiAxLCAiaG9zdCI6ICJhLmRiLWxpbmsuaW4iLCAiaWQiOiAiN2ZjYjRhMjctZjgxOC0zMzc3LWFmNTYtY2MwOGJjYjQyYjVkIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9kYiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTc1MzVcdThiYWZcdTc2YzhcdTc5ZDFcdTY3MDlcdTk2NTBcdTUxNmNcdTUzZjggMjYiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

