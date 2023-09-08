
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp       | ip            | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:----------|:--------------|:-----------------|
|  0 | [4](config/4.json)   | 45.199.138.157  | Netherlands   | NL   | YISP B.V. | 154.84.1.231  | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 39.kccic2pa.xyz | United States | US   | OVH SAS   | 51.81.211.205 | Yes (Region: US) |
|  2 | [6](config/6.json)   | 192.74.228.185  | United States | US   | PEG-SV    | 142.0.129.201 | Yes (Region: US) |
|  3 | [7](config/7.json)   | 199.180.102.13  | United States | US   | PEG-SV    | 142.4.99.65   | Yes (Region: US) |
|  4 | [8](config/8.json)   | jp6.lianpi.xyz  | Poland        | PL   | OVH SAS   | 54.36.174.181 | Yes (Region: FR) |
|  5 | [9](config/9.json)   | 156.245.8.220   | Netherlands   | NL   | YISP B.V. | 154.84.1.134  | Yes (Region: NL) |
|  6 | [10](config/10.json) | 156.245.8.235   | Netherlands   | NL   | YISP B.V. | 154.84.1.139  | Yes (Region: NL) |
|  7 | [13](config/13.json) | 154.85.1.245    | Netherlands   | NL   | YISP B.V. | 154.84.1.206  | Yes (Region: NL) |
|  8 | [18](config/18.json) | 156.225.67.112  | Netherlands   | NL   | YISP B.V. | 154.84.1.140  | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE1NyIsICJwb3J0IjogIjQ5OTIyIiwgImlkIjogImY1MjUwYzRlLWY4NTUtNGVmZi1iNzNjLWEwMjIyNmQ0MmZlNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggNSIsICJhZGQiOiAiMzkua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwMzkiLCAidHlwZSI6ICJub25lIiwgImlkIjogImJhZWZjMzg5LTcyYjEtNGYyMy1iYmFkLTNhODVjZjUxZmU4YSIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIjM5LmtjY2ljMnBhLnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2IiwgImFkZCI6ICIxOTIuNzQuMjI4LjE4NSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTkyNzQ3MDYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5Mzk5MjgyMTc3NiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDciLCAiYWRkIjogIjE5OS4xODAuMTAyLjEzIiwgInBvcnQiOiAiNDQzIiwgImlkIjogImI2NWRhNGFmLWExMmEtNGE1OS05MzE2LTQ1NDllMTJiYTYyYyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy43MzMzMjQ2My54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkzOTkyODIxNzc2IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAianA2LmxpYW5waS54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjFmM2Q2N2I0LTY5MjktNDU5OC05MGNhLTg0YTg0MWJmMDJlNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAyMzIzNCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjXHU0ZTFjXHU0ZWFjQW1hem9uXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDkiLCAiYWRkIjogIjE1Ni4yNDUuOC4yMjAiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNjNiNGI4MjktN2YwMS00ZTI2LWIwMzctZjA0YjFmMDk4NzY1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjMyMTU5ODc3Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQwODMyODQ4NjYiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDEwIiwgImFkZCI6ICIxNTYuMjQ1LjguMjM1IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjYxOTMxMTZkLTk2ZjktNGQ3YS05YmU1LTViYjA2YTY5YWYwYiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy45Mjg3Mzg4OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjkzOTkyODIxNzc2IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogIjE1NC44NS4xLjI0NSIsICJwb3J0IjogIjQ5OTgxIiwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE4IiwgImFkZCI6ICIxNTYuMjI1LjY3LjExMiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJiOGRmM2VmMS04ODdmLTRlZTQtODU1Zi00ZjgwNDE2YzI0NjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuMTI0NjAxNTgueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5Mzk5MjgyMTc3NiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIifQ==
```

