
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn          | cc   | isp           | ip                   | chatgpt          |
|---:|:---------------------|:---------------|:------------|:-----|:--------------|:---------------------|:-----------------|
|  0 | [2](config/2.json)   | 154.84.1.47    | Netherlands | NL   | YISP B.V.     | 154.84.1.121         | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 156.245.8.66   | Netherlands | NL   | YISP B.V.     | 154.84.1.40          | Yes (Region: NL) |
|  2 | [5](config/5.json)   | 156.245.8.17   | Netherlands | NL   | YISP B.V.     | 154.84.1.145         | Yes (Region: NL) |
|  3 | [7](config/7.json)   | 156.249.18.14  | Netherlands | NL   | YISP B.V.     | 154.84.1.193         | Yes (Region: NL) |
|  4 | [16](config/16.json) | cf.noaries.de  | France      | FR   | Online S.a.s. | 2001:bc8:a00:3200::1 | Yes (Region: FR) |
|  5 | [17](config/17.json) | 156.225.67.121 | Netherlands | NL   | YISP B.V.     | 154.84.1.134         | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTU0Ljg0LjEuNDciLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiZDI0OWUzNy03MzU5LTQxZWUtODRhNy0wOWU0OWUwZWM1YzQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDIxMTAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkaW5ub3ZhdGlvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDMiLCAiYWRkIjogIjE1Ni4yNDUuOC42NiIsICJwb3J0IjogIjQ5NTE5IiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0NS44LjE3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNmU3OWVlYTQtNWY3Mi00NjgzLWFkMGUtNTMzOWYwMTM0MjFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0NDA2MiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmICA1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4xNCIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAiNDkyMjAiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiODA4MCIsICJpZCI6ICI0ZjdkNWQ0My0yMjZlLTQ4ZDgtOWRmMC01ZThiZjlmNzcyODgiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImZ0LmNsb3VkZmxhcmUucXVlc3QiLCAicGF0aCI6ICIvYXJpZXM_ZWQ9MjA0OCIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMjEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICAxNyIsICJwb3J0IjogNDc3NDQsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJzdXJvbmd3ZWkuZXUub3JnIiwgInBhdGgiOiAiL3JlZmZzN3kyNmcwdWEiLCAidGxzIjogIiJ9
```

