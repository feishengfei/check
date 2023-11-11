
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn             | cc   | isp                               | ip                                  | chatgpt          |
|---:|:---------------------|:-----------------------|:---------------|:-----|:----------------------------------|:------------------------------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.98.232           | China          | CN   | PEG-SV                            | 142.0.129.201                       | Yes (Region: US) |
|  1 | [4](config/4.json)   | n1699253769.aaigefm.cn | United States  | US   | Alibaba US Technology Co., Ltd.   | 47.76.34.124                        | Yes (Region: US) |
|  2 | [7](config/7.json)   | 198.2.193.152          | China          | CN   | PEG-SV                            | 198.2.193.145                       | Yes (Region: US) |
|  3 | [8](config/8.json)   | 137.175.3.88           | China          | CN   | PEG-SV                            | 137.175.9.177                       | Yes (Region: US) |
|  4 | [9](config/9.json)   | 156.225.67.155         | Netherlands    | NL   | YISP B.V.                         | 154.84.1.193                        | Yes (Region: NL) |
|  5 | [15](config/15.json) | 13.87.74.71            | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK       | 13.87.74.71                         | Yes (Region: GB) |
|  6 | [16](config/16.json) | 45.199.138.191         | Netherlands    | NL   | YISP B.V.                         | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |
|  7 | [20](config/20.json) | 120.233.43.47          | Taiwan         | TW   | Data Communication Business Group | 211.20.157.213                      | Yes (Region: TW) |
|  8 | [21](config/21.json) | n1697685464.aaigefm.cn | United States  | US   | Alibaba US Technology Co., Ltd.   | 47.76.44.192                        | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC45OC4yMzIiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMDUxYjg0NGYtZWZlMy00ODQ3LTkyYWEtNjZiNWRlMGI2ZDRlIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjEyOTcxNDc1Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTk1MzQ4NzYyODAiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgNCIsICJhZGQiOiAibjE2OTkyNTM3NjkuYWFpZ2VmbS5jbiIsICJwb3J0IjogNDQzLCAiaWQiOiAiOTgyZmFkZDEtM2U1Zi00YWEzLTg1NTItZWQ2ZmRhMjM0MTRhIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJuMTY5OTI1Mzc2OS5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA3IiwgImFkZCI6ICIxOTguMi4xOTMuMTUyIiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiNjhkMjM4Y2UtM2NhMS00NmRjLWI4MzMtYTA5MTZjODI5YWQzIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjI4MjUxNjU4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTk2MjQ3MjMyMTMiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDgiLCAiYWRkIjogIjEzNy4xNzUuMy44OCIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy43MDgxMjIzNi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5NjI0NzIzMjEzIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDkiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTU1IiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiMzc1ZTcwZjAtNWQ0Ni00NzZmLThkNjktMGZiMzVjNTU0OGE5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjExMzAyODUxLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTk1MzQ4NzYyODAiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRMXFsUmtub045UHdHZUV4V1Z5VEtn@13.87.74.71:14564#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%2015
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxNiIsICJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAicG9ydCI6IDMwMDAwLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjQyMDc3MjMwLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTkyODAwOTkxMzgiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjAiLCAiYWRkIjogIjEyMC4yMzMuNDMuNDciLCAicG9ydCI6ICIxMTAxMyIsICJpZCI6ICI4NWRiNjY1Mi1hNzQ3LTNhMGEtYTE3MC00MjI3MzYwNzY0MTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAibjE2OTc2ODU0NjQuYWFpZ2VmbS5jbiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMjEiLCAicG9ydCI6IDQ0MywgImlkIjogIjE4NzAwMmZkLWI4YWQtNGQzNi1iNGZiLTFhMzIyNGNjOTllMiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJuMTY5NzY4NTQ2NC5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
```

