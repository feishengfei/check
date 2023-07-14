
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                              | cn   | cc   | isp   | ip             | chatgpt          |
|---:|:---------------------|:----------------------------------|:-----|:-----|:------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | twpaopao4.dskjahf.xyz             |      |      |       | 114.37.203.132 | Yes (Region: TW) |
|  1 | [3](config/3.json)   | 64.32.4.35                        |      |      |       | 107.167.13.162 | Yes (Region: US) |
|  2 | [4](config/4.json)   | 172.247.67.46                     |      |      |       | 23.225.9.234   | Yes (Region: US) |
|  3 | [5](config/5.json)   | 156.245.8.83                      |      |      |       | 154.84.1.161   | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 67.21.84.217                      |      |      |       | 67.21.85.2     | Yes (Region: US) |
|  5 | [7](config/7.json)   | 37.120.193.102                    |      |      |       | 37.120.193.102 | Yes (Region: RS) |
|  6 | [8](config/8.json)   | 0kxedm1x8q8lksmj14.xingbayun.buzz |      |      |       | 154.84.1.197   | Yes (Region: NL) |
|  7 | [10](config/10.json) | 154.85.1.123                      |      |      |       | 154.84.1.232   | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAidHdwYW9wYW80LmRza2phaGYueHl6IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJlYjg4NWZiMS0xZGJmLTM0NDctODFkOC1mOTk5MmNkNTg4MTciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogMjI4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTViOWNcdTUxNzBcdTUzYmZcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuNC4zNSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0MzE2NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2U2hhcmt0ZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTcyLjI0Ny42Ny40NiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjIyNzhlZmU0LWFkMGMtNDdjZS05NDgwLTA2ODYwODM2OGQ3NiIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA1MDAzNSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2Q29wZXJhdGlvbiBDb2xvY3Rpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDUiLCAiYWRkIjogIjE1Ni4yNDUuOC44MyIsICJwb3J0IjogIjQ4MTIzIiwgImlkIjogImQ3NzM1MDU4LTFkYWMtNDYxOC05OWZmLTBhYTA0NDFlYzJkNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNjcuMjEuODQuMjE3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYjlhMzA1YTktMWZmMi00ZWMxLWIzMzgtOTMzNTU1ODMzYmFhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3MDg4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMzcuMTIwLjE5My4xMDIiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjU3XHU5YTZjXHU1YzNjXHU0ZTlhICA3IiwgInBvcnQiOiA1MjkyMCwgImlkIjogIjU3MTcwZmYwLTcxODAtNDY2NC04ZjYxLThkZWJkZGEzNDVmNyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTRmYzRcdTUyZDJcdTUxODhcdTVkZGVcdTZjZTJcdTcyNzlcdTUxNzBBbWF6b25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiMGt4ZWRtMXg4cThsa3NtajE0LnhpbmdiYXl1bi5idXp6IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjEzMjA5OTdkLTY4MzgtNGRhOS04ZmFmLWJkMTBjZWM2OGZiNiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3Lm1pY3Jvc29mdC5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMTIzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMTMwYzlmMmUtNDJiMS00ZWJmLWIzNDUtZTI2NDU2YTA2MWY5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0MDI5OCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRpbm5vdmF0aW9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDEwIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

