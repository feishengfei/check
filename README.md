
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn          | cc   | isp       | ip                                  | chatgpt          |
|---:|:---------------------|:----------------|:------------|:-----|:----------|:------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 104.233.249.242 | China       | CN   | PEG-SV    | 142.4.99.65                         | Yes (Region: US) |
|  1 | [3](config/3.json)   | 198.2.193.146   | China       | CN   | PEG-SV    | 198.2.193.145                       | Yes (Region: US) |
|  2 | [5](config/5.json)   | 142.4.98.226    | China       | CN   | PEG-SV    | 142.0.129.201                       | Yes (Region: US) |
|  3 | [6](config/6.json)   | 156.245.8.146   | Netherlands | NL   | YISP B.V. | 154.84.1.134                        | Yes (Region: NL) |
|  4 | [11](config/11.json) | 156.225.67.203  | Netherlands | NL   | YISP B.V. | 46.182.107.123                      | Yes (Region: NL) |
|  5 | [13](config/13.json) | 156.225.67.48   | Netherlands | NL   | YISP B.V. | 154.84.1.164                        | Yes (Region: NL) |
|  6 | [14](config/14.json) | 154.85.1.244    | Netherlands | NL   | YISP B.V. | 154.84.1.216                        | Yes (Region: NL) |
|  7 | [16](config/16.json) | 45.199.138.191  | Netherlands | NL   | YISP B.V. | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |
|  8 | [19](config/19.json) | 156.245.8.130   | Netherlands | NL   | YISP B.V. | 154.84.1.121                        | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNQRUcgVEVDSCAyIiwgImFkZCI6ICIxMDQuMjMzLjI0OS4yNDIiLCAicG9ydCI6IDQ0MywgImlkIjogImI2NWRhNGFmLWExMmEtNGE1OS05MzE2LTQ1NDllMTJiYTYyYyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy43MzMzMjQ2My54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MjM5ODg4OTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyAzIiwgImFkZCI6ICIxOTguMi4xOTMuMTQ2IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjY4ZDIzOGNlLTNjYTEtNDZkYy1iODMzLWEwOTE2YzgyOWFkMyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODI1MTY1OC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MjM5ODg4OTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA1IiwgImFkZCI6ICIxNDIuNC45OC4yMjYiLCAicG9ydCI6IDQ0MywgImlkIjogIjA1MWI4NDRmLWVmZTMtNDg0Ny05MmFhLTY2YjVkZTBiNmQ0ZSIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41OTI3NDcwNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MjM5ODg4OTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDYiLCAiYWRkIjogIjE1Ni4yNDUuOC4xNDYiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNjNiNGI4MjktN2YwMS00ZTI2LWIwMzctZjA0YjFmMDk4NzY1IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjMyMTU5ODc3Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTgyMzk4ODg5MTQiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3LjIwMyIsICJwb3J0IjogMzAwMDAsICJpZCI6ICJmOWZhM2E5Yy1mN2Q1LTQxNGYtODhlNi02OTcwNTg1ZDk5NDkiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMjIyNjI3NjkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5ODIzOTg4ODkxNCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEzIiwgImFkZCI6ICIxNTYuMjI1LjY3LjQ4IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjNjYTkxMmRhLTZhYzItNDE4Zi1iOWNmLTQ1YjZmNjk0NTc5YiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4zODA2NzU0OC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MjM5ODg4OTE0IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAiYWRkIjogIjE1NC44NS4xLjI0NCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICIxZDQ3NGYwYi1lNzhkLTRhZjktYmM0YS1hNDY3NDY3YmM3YTciLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMjgxMTUzNjEueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5ODIzOTg4ODkxNCIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNiIsICJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjQyMDc3MjMwLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE1MjI0MzgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE5IiwgImFkZCI6ICIxNTYuMjQ1LjguMTMwIiwgInBvcnQiOiAzMDAwMCwgImlkIjogImJkMjQ5ZTM3LTczNTktNDFlZS04NGE3LTA5ZTQ5ZTBlYzVjNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40NzUyMzM3NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4MjM5ODg4OTE0IiwgInRscyI6ICJ0bHMifQ==
```

