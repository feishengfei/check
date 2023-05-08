
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr           | cn            | cc   | isp               | ip              | chatgpt          |
|---:|:-------------------|:---------------|:--------------|:-----|:------------------|:----------------|:-----------------|
|  0 | [2](config/2.json) | 154.85.1.18    | Netherlands   | NL   | YISP B.V.         | 154.84.1.232    | Yes (Region: NL) |
|  1 | [4](config/4.json) | 156.249.18.49  | Netherlands   | NL   | YISP B.V.         | 154.84.1.6      | Yes (Region: NL) |
|  2 | [6](config/6.json) | 156.245.8.241  | Netherlands   | NL   | YISP B.V.         | 154.84.1.44     | Yes (Region: NL) |
|  3 | [8](config/8.json) | 192.203.230.86 | United States | US   | AS-GLOBALTELEHOST | 169.197.141.187 | Yes (Region: US) |
|  4 | [9](config/9.json) | 154.84.1.46    | Netherlands   | NL   | YISP B.V.         | 154.84.1.121    | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTU0Ljg1LjEuMTgiLCAicG9ydCI6ICI0MDIyMCIsICJpZCI6ICIxMzBjOWYyZS00MmIxLTRlYmYtYjM0NS1lMjY0NTZhMDYxZjkiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU2LjI0OS4xOC40OSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJkMDI0ZmQ4Yi1lYTc4LTQ3ODktYjkyOC03MGFmYTFhOTEwY2UiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTU1ODMwMzUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4MzM0NjA2NTMwMiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDYiLCAiYWRkIjogIjE1Ni4yNDUuOC4yNDEiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2ODMzNDYwNjUzMDIiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDgiLCAiYWRkIjogIjE5Mi4yMDMuMjMwLjg2IiwgInBvcnQiOiA4MCwgImlkIjogImE0NDJkYWNmLWNiYjMtNDg4YS05NzQ0LTYxNDk0ZWEzODYzMCIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAidXMtMS5hY3l1bi5jZiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAiMTU0Ljg0LjEuNDYiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiYmQyNDllMzctNzM1OS00MWVlLTg0YTctMDllNDllMGVjNWM0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQ3NTIzMzc1Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2ODMzNDYwNjUzMDIiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

