
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn             | cc   | isp                               | ip                   | chatgpt          |
|---:|:---------------------|:-----------------------|:---------------|:-----|:----------------------------------|:---------------------|:-----------------|
|  0 | [2](config/2.json)   | 13.87.74.71            | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK       | 13.87.74.71          | Yes (Region: GB) |
|  1 | [3](config/3.json)   | 112.29.94.23           | United Kingdom | GB   | OVH SAS                           | 2001:41d0:700:2c84:: | Yes (Region: GB) |
|  2 | [5](config/5.json)   | 198.2.193.152          | China          | CN   | PEG-SV                            | 198.2.193.145        | Yes (Region: US) |
|  3 | [11](config/11.json) | 156.225.67.155         | Netherlands    | NL   | YISP B.V.                         | 154.84.1.193         | Yes (Region: NL) |
|  4 | [12](config/12.json) | n1697685464.aaigefm.cn | United States  | US   | Alibaba US Technology Co., Ltd.   | 47.76.44.192         | Yes (Region: US) |
|  5 | [19](config/19.json) | 120.233.43.47          | Taiwan         | TW   | Data Communication Business Group | 211.20.157.212       | Yes (Region: TW) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpRMXFsUmtub045UHdHZUV4V1Z5VEtn@13.87.74.71:14564#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDMicrosoft%E5%85%AC%E5%8F%B8%202
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTViODlcdTVmYmRcdTc3MDFcdTU0MDhcdTgwYTVcdTVlMDJcdTc5ZmJcdTUyYTggMyIsICJhZGQiOiAiMTEyLjI5Ljk0LjIzIiwgInBvcnQiOiAiNDkwNTYiLCAiaWQiOiAiMjFhOWJmZjItNzJkZS00ZTYyLTkzZmYtOGIxNTlmNjZkODc1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA1IiwgImFkZCI6ICIxOTguMi4xOTMuMTUyIiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiNjhkMjM4Y2UtM2NhMS00NmRjLWI4MzMtYTA5MTZjODI5YWQzIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjI4MjUxNjU4Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTk2MjQ3MjMyMTMiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3LjE1NSIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xMTMwMjg1MS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5NTM0ODc2MjgwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAibjE2OTc2ODU0NjQuYWFpZ2VmbS5jbiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMTIiLCAicG9ydCI6IDQ0MywgImlkIjogIjE4NzAwMmZkLWI4YWQtNGQzNi1iNGZiLTFhMzIyNGNjOTllMiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJuMTY5NzY4NTQ2NC5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMTkiLCAiYWRkIjogIjEyMC4yMzMuNDMuNDciLCAicG9ydCI6ICIxMTAxMyIsICJpZCI6ICI4NWRiNjY1Mi1hNzQ3LTNhMGEtYTE3MC00MjI3MzYwNzY0MTAiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

