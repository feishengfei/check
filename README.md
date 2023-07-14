
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                  | cn          | cc   | isp                               | ip             | chatgpt          |
|---:|:-------------------|:----------------------|:------------|:-----|:----------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json) | 154.85.1.123          | Netherlands | NL   | YISP B.V.                         | 154.84.1.232   | Yes (Region: NL) |
|  1 | [3](config/3.json) | 37.120.193.102        | Serbia      | RS   | M247 Europe SRL                   | 146.70.111.194 | Yes (Region: RS) |
|  2 | [5](config/5.json) | twpaopao3.dskjahf.xyz | Taiwan      | TW   | Data Communication Business Group | 114.37.174.211 | Yes (Region: TW) |
|  3 | [6](config/6.json) | twpaopao4.dskjahf.xyz | Taiwan      | TW   | Data Communication Business Group | 114.37.203.132 | Yes (Region: TW) |
|  4 | [7](config/7.json) | 156.245.8.83          | Netherlands | NL   | YISP B.V.                         | 154.84.1.161   | Yes (Region: NL) |
|  5 | [8](config/8.json) | digitalocean.com      | Netherlands | NL   | YISP B.V.                         | 154.84.1.197   | Yes (Region: NL) |
|  6 | [9](config/9.json) | awsjp1.gfwisbest.xyz  | Japan       | JP   | DMIT                              | 154.31.112.51  | Yes (Region: JP) |

## Valid
```
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMTIzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMTMwYzlmMmUtNDJiMS00ZWJmLWIzNDUtZTI2NDU2YTA2MWY5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0MDI5OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMzcuMTIwLjE5My4xMDIiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjU3XHU5YTZjXHU1YzNjXHU0ZTlhICAzIiwgInBvcnQiOiA1MjkyMCwgImlkIjogIjU3MTcwZmYwLTcxODAtNDY2NC04ZjYxLThkZWJkZGEzNDVmNyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAidHdwYW9wYW8zLmRza2phaGYueHl6IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NjViMFx1N2FmOVx1NWUwMlx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSA1IiwgInBvcnQiOiAyMzAsICJpZCI6ICJlYjg4NWZiMS0xZGJmLTM0NDctODFkOC1mOTk5MmNkNTg4MTciLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAidHdwYW9wYW80LmRza2phaGYueHl6IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJlYjg4NWZiMS0xZGJmLTM0NDctODFkOC1mOTk5MmNkNTg4MTciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMjI4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTViOWNcdTUxNzBcdTUzYmZcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDciLCAiYWRkIjogIjE1Ni4yNDUuOC44MyIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImRpZ2l0YWxvY2Vhbi5jb20iLCAicG9ydCI6IDgwODAsICJpZCI6ICI1ZjA5ODAyOC1lYTIyLTQyZWEtYWJmZC05MjIyY2IyOThiNzQiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInZjZXUudnBuNjYuZXUub3JnIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiYXdzanAxLmdmd2lzYmVzdC54eXoiLCAiYWlkIjogMiwgImhvc3QiOiAiIiwgImlkIjogImViODg1ZmIxLTFkYmYtMzQ0Ny04MWQ4LWY5OTkyY2Q1ODgxNyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAyMjksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY1x1OTBmZFx1NGU5YVx1OWE2Y1x1OTAwYShBbWF6b24pXHU1MTZjXHU1M2Y4XHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDkiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

