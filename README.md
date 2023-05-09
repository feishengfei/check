
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp                 | ip                    | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:--------------------|:----------------------|:-----------------|
|  0 | [4](config/4.json)   | d.mamadcucu.com | Germany       | DE   | Hetzner Online GmbH | 2a01:4f8:c010:3d51::1 | Yes (Region: DE) |
|  1 | [6](config/6.json)   | 156.225.67.6    | Netherlands   | NL   | YISP B.V.           | 154.84.1.161          | Yes (Region: NL) |
|  2 | [7](config/7.json)   | 156.245.8.126   | Netherlands   | NL   | YISP B.V.           | 154.84.1.164          | Yes (Region: NL) |
|  3 | [8](config/8.json)   | 192.203.230.86  | United States | US   | AS-GLOBALTELEHOST   | 169.197.141.187       | Yes (Region: US) |
|  4 | [11](config/11.json) | 156.225.67.143  | Netherlands   | NL   | YISP B.V.           | 154.84.1.37           | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDQiLCAiYWRkIjogImQubWFtYWRjdWN1LmNvbSIsICJwb3J0IjogIjIwODIiLCAiaWQiOiAiMzhjOGU3MzQtZjg3Zi00Yzc0LWI1ZWQtNjNlMTBjZTU0YjkzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJpNS5tYW1hZGN1Y3UuY29tIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJkNzczNTA1OC0xZGFjLTQ2MTgtOTlmZi0wYWEwNDQxZWMyZDciLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMjAxNjMzMjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4MzU0MzAyNDQ1MyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDciLCAiYWRkIjogIjE1Ni4yNDUuOC4xMjYiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiM2NhOTEyZGEtNmFjMi00MThmLWI5Y2YtNDViNmY2OTQ1NzliIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjM4MDY3NTQ4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2ODM1NDMwMjQ0NTMiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDgiLCAiYWRkIjogIjE5Mi4yMDMuMjMwLjg2IiwgInBvcnQiOiA4MCwgImlkIjogImE0NDJkYWNmLWNiYjMtNDg4YS05NzQ0LTYxNDk0ZWEzODYzMCIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAidXMtMS5hY3l1bi5jZiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3LjE0MyIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI5OTAwMDZiZC1jYjIwLTQ4MmYtOWM5Ny1mNWZjNjUzNTk2MDUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNDM0MzAxNDAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4MzU0MzAyNDQ1MyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

