
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn          | cc   | isp              | ip              | chatgpt          |
|---:|:---------------------|:---------------------|:------------|:-----|:-----------------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.110.142        | China       | CN   | PEG-SV           | 142.4.110.137   | Yes (Region: US) |
|  1 | [3](config/3.json)   | 45.199.138.205       | Netherlands | NL   | YISP B.V.        | 154.84.1.129    | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 154.85.1.244         | Netherlands | NL   | YISP B.V.        | 154.84.1.216    | Yes (Region: NL) |
|  3 | [6](config/6.json)   | gzcm01.celerlink.one | Singapore   | SG   | ORACLE-BMC-31898 | 158.178.226.110 | Yes (Region: SG) |
|  4 | [9](config/9.json)   | 156.225.67.104       | Netherlands | NL   | YISP B.V.        | 154.84.1.44     | Yes (Region: NL) |
|  5 | [10](config/10.json) | 45.199.138.186       | Netherlands | NL   | YISP B.V.        | 154.84.1.122    | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC4xMTAuMTQyIiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjY4ZDIzOGNlLTNjYTEtNDZkYy1iODMzLWEwOTE2YzgyOWFkMyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODI1MTY1OC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk3Mzc2NzgyODc5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4LjIwNSIsICJwb3J0IjogMzAwMDAsICJpZCI6ICIyMGIzMDkxNi1lMjAzLTQxMmUtOGVjMC05MDBmM2FjZDUxMjgiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNjk3MDgyNzIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NzI4ODcyMjI2NiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjFkNDc0ZjBiLWU3OGQtNGFmOS1iYzRhLWE0Njc0NjdiYzdhNyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODExNTM2MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozNTI1NTg4ZWUxNGVhOTI0@gzcm01.celerlink.one:41040#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%A7%BB%E5%8A%A8%206
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDkiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTY5NDQ4MDY5NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMCIsICJhZGQiOiAiNDUuMTk5LjEzOC4xODYiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNGVjMGFlNjItZGUwOS00MDI5LTkwNGEtMDMxM2Q0NjI4ZWNmIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjE5MjI5MzYyLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTczNzY3ODI4NzkiLCAidGxzIjogInRscyJ9
```

