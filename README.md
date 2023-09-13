
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp       | ip             | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:----------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 192.243.126.47  | Japan         | JP   | IT7NET    | 192.243.126.47 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 46.182.107.22   | Netherlands   | NL   | YISP B.V. | 154.84.1.16    | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 45.199.138.148  | Netherlands   | NL   | YISP B.V. | 46.182.107.123 | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 142.4.122.65    | China         | CN   | PEG-SV    | 142.4.101.146  | Yes (Region: US) |
|  4 | [6](config/6.json)   | 64.32.20.125    | United States | US   | SHARKTECH | 64.32.0.58     | Yes (Region: US) |
|  5 | [7](config/7.json)   | 67.21.90.5      | United States | US   | SHARKTECH | 107.167.22.10  | Yes (Region: US) |
|  6 | [8](config/8.json)   | 67.21.84.164    | Poland        | PL   | OVH SAS   | 54.36.174.181  | Yes (Region: FR) |
|  7 | [9](config/9.json)   | 192.74.228.186  | United States | US   | PEG-SV    | 142.0.129.201  | Yes (Region: US) |
|  8 | [10](config/10.json) | 137.175.69.209  | China         | CN   | PEG-SV    | 137.175.14.21  | Yes (Region: US) |
|  9 | [11](config/11.json) | 45.58.185.157   | Netherlands   | NL   | SHARKTECH | 45.58.185.146  | Yes (Region: US) |
| 10 | [12](config/12.json) | 67.21.77.77     | United States | US   | SHARKTECH | 107.167.18.42  | Yes (Region: US) |
| 11 | [13](config/13.json) | 142.4.99.72     | United States | US   | PEG-SV    | 142.4.99.65    | Yes (Region: US) |
| 12 | [15](config/15.json) | 162.159.60.89   | Spain         | ES   | NIXVAL    | 213.162.210.42 | Yes (Region: ES) |
| 13 | [17](config/17.json) | 156.245.8.141   | Netherlands   | NL   | YISP B.V. | 154.84.1.139   | Yes (Region: NL) |
| 14 | [19](config/19.json) | 156.225.67.51   | Netherlands   | NL   | YISP B.V. | 154.84.1.37    | Yes (Region: NL) |
| 15 | [21](config/21.json) | 156.245.8.240   | Netherlands   | NL   | YISP B.V. | 154.84.1.44    | Yes (Region: NL) |
| 16 | [22](config/22.json) | 104.160.186.195 | United States | US   | SHARKTECH | 64.32.2.26     | Yes (Region: US) |
| 17 | [31](config/31.json) | 156.245.8.220   | Netherlands   | NL   | YISP B.V. | 154.84.1.134   | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzAgIDIiLCAiYWRkIjogIjE5Mi4yNDMuMTI2LjQ3IiwgInBvcnQiOiAiMTkyMTgiLCAiaWQiOiAiYjgyMmI4NjMtY2RlMS00MjJkLThmNzYtMjJhZGY4N2M4Mzk5IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzAgIDMiLCAiYWRkIjogIjQ2LjE4Mi4xMDcuMjIiLCAicG9ydCI6ICI0OTkyMiIsICJpZCI6ICJkZTQ5MTgwMi0yMzNlLTQ3ZjItOGM2Yy1kMTliY2Y1YmQ1NmIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xNDgiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmOWZhM2E5Yy1mN2Q1LTQxNGYtODhlNi02OTcwNTg1ZDk5NDkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDY2MTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZU1VTFRBQ09NXHU2NzNhXHU2MjNmIDQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA1IiwgImFkZCI6ICIxNDIuNC4xMjIuNjUiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODgyMDAwNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0NTE2MDY0MjE1IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiNjQuMzIuMjAuMTI1IiwgInBvcnQiOiA0NDMsICJpZCI6ICJjMWJhZDlhNi0xNDgyLTQ5NDEtYTBjNC1lODVmM2NiYmNiNWEiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNzkyNTE2NzEueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDQyOTkwODc0OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiNjcuMjEuOTAuNSIsICJwb3J0IjogNDQzLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiNjcuMjEuODQuMTY0IiwgInBvcnQiOiA0NDMsICJpZCI6ICJjZmY5ZDg2MC03MzMwLTRlZTEtYjA3Mi03MTQyZGRmMTU3MWQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuODI2MTUzNTUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDQyOTkwODc0OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA5IiwgImFkZCI6ICIxOTIuNzQuMjI4LjE4NiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTkyNzQ3MDYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDI1NTg0OTMzOCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDEwIiwgImFkZCI6ICIxMzcuMTc1LjY5LjIwOSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjcyNjQ5MDAwLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ1MTYwNjQyMTUiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAiYWRkIjogIjQ1LjU4LjE4NS4xNTciLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41OTc2MDE2My54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0NDI5OTA4NzQ4IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTIiLCAiYWRkIjogIjY3LjIxLjc3Ljc3IiwgInBvcnQiOiA0NDMsICJpZCI6ICJmYWJiMzBlOC0zYTJjLTQxNDktOTY1MS0yNzU4Zjc3MTI0ODEiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuODcwOTczNTUueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDQyOTkwODc0OCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAxMyIsICJhZGQiOiAiMTQyLjQuOTkuNzIiLCAicG9ydCI6IDQ0MywgImlkIjogImI2NWRhNGFmLWExMmEtNGE1OS05MzE2LTQ1NDllMTJiYTYyYyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy43MzMzMjQ2My54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk0NTE2MDY0MjE1IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE1IiwgImFkZCI6ICIxNjIuMTU5LjYwLjg5IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiN2E2MGMxNWUtY2JjZC00ODZkLWFlZTYtMDdhNDk0ZjQwM2UzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ4YnkuZGFvemhhbmcubGluayIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE3IiwgImFkZCI6ICIxNTYuMjQ1LjguMTQxIiwgInBvcnQiOiA0NDMsICJpZCI6ICI2MTkzMTE2ZC05NmY5LTRkN2EtOWJlNS01YmIwNmE2OWFmMGIiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuOTI4NzM4ODkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDUxNjA2NDIxNSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE5IiwgImFkZCI6ICIxNTYuMjI1LjY3LjUxIiwgInBvcnQiOiA0NDMsICJpZCI6ICI5OTAwMDZiZC1jYjIwLTQ4MmYtOWM5Ny1mNWZjNjUzNTk2MDUiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNDM0MzAxNDAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDUxNjA2NDIxNSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDIxIiwgImFkZCI6ICIxNTYuMjQ1LjguMjQwIiwgInBvcnQiOiA0NDMsICJpZCI6ICIyOWE1ZDQ4ZS0yNGYxLTQ4ZmQtYTVlMS05YTQ2Y2IzMTAzMmYiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNDE3NTgxMTIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDUxNjA2NDIxNSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjIiLCAiYWRkIjogIjEwNC4xNjAuMTg2LjE5NSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjU2MTgxMjM0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDMxIiwgImFkZCI6ICIxNTYuMjQ1LjguMjIwIiwgInBvcnQiOiA0NDMsICJpZCI6ICI2M2I0YjgyOS03ZjAxLTRlMjYtYjAzNy1mMDRiMWYwOTg3NjUiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMzIxNTk4NzcueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NDQyOTkwODc0OCIsICJ0bHMiOiAidGxzIn0=
```

