
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn             | cc   | isp                               | ip                                 | chatgpt          |
|---:|:---------------------|:----------------------|:---------------|:-----|:----------------------------------|:-----------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 107.167.16.102        |                |      |                                   | 2610:150:c011:6:ec4:7aff:fe4a:b00a | Yes (Region: US) |
|  1 | [5](config/5.json)   | 154.85.1.123          |                |      |                                   | 154.84.1.232                       | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 64.32.4.44            |                |      |                                   | 107.167.13.162                     | Yes (Region: US) |
|  3 | [7](config/7.json)   | awsjp1.gfwisbest.xyz  |                |      |                                   | 154.31.112.51                      | Yes (Region: JP) |
|  4 | [8](config/8.json)   | 156.245.8.83          |                |      |                                   | 154.84.1.197                       | Yes (Region: NL) |
|  5 | [9](config/9.json)   | 37.120.193.102        |                |      |                                   | 146.70.111.194                     | Yes (Region: RS) |
|  6 | [13](config/13.json) | 202.79.174.157        |                |      |                                   | 202.79.174.146                     | Yes (Region: SG) |
|  7 | [24](config/24.json) | vuk2.0bad.com         | United Kingdom | GB   | Akamai Connected Cloud            | 176.58.118.208                     | Yes (Region: GB) |
|  8 | [26](config/26.json) | twpaopao3.dskjahf.xyz | Taiwan         | TW   | Data Communication Business Group | 114.37.174.211                     | Yes (Region: TW) |
|  9 | [27](config/27.json) | twpaopao4.dskjahf.xyz | Taiwan         | TW   | Data Communication Business Group | 114.37.203.132                     | Yes (Region: TW) |

## Valid
```
vmess://eyJhZGQiOiAiMTA3LjE2Ny4xNi4xMDIiLCAiYWlkIjogIjY0IiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogIiIsICJpZCI6ICJiNzRmNGFmYS0xYTU3LTRhZmYtYjdlNS04YWQ1ZWEzMzU2NmYiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogIjQ3MDc0IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMTIzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMTMwYzlmMmUtNDJiMS00ZWJmLWIzNDUtZTI2NDU2YTA2MWY5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0MDI5OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuNC40NCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJwb3J0IjogNDMxNjYsICJpZCI6ICI4NjUzMDA0Zi1kZTY3LTQ0YzItOWNjZS1lMDgzMDkzM2ZiMDMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiYXdzanAxLmdmd2lzYmVzdC54eXoiLCAiYWlkIjogMiwgImhvc3QiOiAiIiwgImlkIjogImViODg1ZmIxLTFkYmYtMzQ0Ny04MWQ4LWY5OTkyY2Q1ODgxNyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAyMjksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY1x1OTBmZFx1NGU5YVx1OWE2Y1x1OTAwYShBbWF6b24pXHU1MTZjXHU1M2Y4XHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDciLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDgiLCAiYWRkIjogIjE1Ni4yNDUuOC44MyIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMzcuMTIwLjE5My4xMDIiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjU3XHU5YTZjXHU1YzNjXHU0ZTlhICA5IiwgInBvcnQiOiA1MjkyMCwgImlkIjogIjU3MTcwZmYwLTcxODAtNDY2NC04ZjYxLThkZWJkZGEzNDVmNyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMjAyLjc5LjE3NC4xNTciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmQkdQLk5FVCBDTjJcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAicG9ydCI6IDU1MjY0LCAiaWQiOiAiMTIxYzljODktN2QxMS00ZjQ5LTkxMTItZGMxZTg1MzYzZjZmIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAidnVrMi4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9jaGF0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1ODJmMVx1NTZmZFx1NGYyNlx1NjU2Nkxpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyNCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAidHdwYW9wYW8zLmRza2phaGYueHl6IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NjViMFx1N2FmOVx1NWUwMlx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSAyNiIsICJwb3J0IjogMjMwLCAiaWQiOiAiZWI4ODVmYjEtMWRiZi0zNDQ3LTgxZDgtZjk5OTJjZDU4ODE3IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAidHdwYW9wYW80LmRza2phaGYueHl6IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJlYjg4NWZiMS0xZGJmLTM0NDctODFkOC1mOTk5MmNkNTg4MTciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMjI4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTViOWNcdTUxNzBcdTUzYmZcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMjciLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

