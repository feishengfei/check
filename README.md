
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn             | cc   | isp                             | ip             | chatgpt          |
|---:|:---------------------|:-----------------------|:---------------|:-----|:--------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 108.186.178.134        | China          | CN   | PEG-SV                          | 142.4.108.227  | Yes (Region: US) |
|  1 | [8](config/8.json)   | 104.233.176.163        | China          | CN   | PEG-SV                          | 142.4.99.65    | Yes (Region: US) |
|  2 | [9](config/9.json)   | 156.225.67.52          | Netherlands    | NL   | YISP B.V.                       | 154.84.1.37    | Yes (Region: NL) |
|  3 | [11](config/11.json) | 156.225.67.106         | Netherlands    | NL   | YISP B.V.                       | 154.84.1.44    | Yes (Region: NL) |
|  4 | [15](config/15.json) | n1698551273.aaigefm.cn | United States  | US   | Alibaba US Technology Co., Ltd. | 47.76.57.68    | Yes (Region: US) |
|  5 | [16](config/16.json) | 156.249.18.151         | Netherlands    | NL   | YISP B.V.                       | 154.84.1.148   | Yes (Region: NL) |
|  6 | [24](config/24.json) | n1697765772.izwhvan.cn | United States  | US   | Alibaba US Technology Co., Ltd. | 47.76.34.26    | Yes (Region: US) |
|  7 | [25](config/25.json) | 183.233.187.214        | Hong Kong      | HK   | CNSERVERS                       | 172.247.18.74  | Yes (Region: US) |
|  8 | [29](config/29.json) | 54.36.174.181          | Poland         | PL   | OVH SAS                         | 54.36.174.181  | Yes (Region: FR) |
|  9 | [31](config/31.json) | n1698119642.izwhvan.cn | United States  | US   | Alibaba US Technology Co., Ltd. | 47.76.46.141   | Yes (Region: US) |
| 10 | [33](config/33.json) | api.jquery.com         | United Kingdom | GB   | AS-GLOBALTELEHOST               | 172.99.190.159 | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDIiLCAiYWRkIjogIjEwOC4xODYuMTc4LjEzNCIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy44ODk5ODYwMC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4NjcxNjAwOTg2IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1ZTVcdTY3MmNcdTRlMWNcdTRlYWNQRUcgVEVDSCA4IiwgImFkZCI6ICIxMDQuMjMzLjE3Ni4xNjMiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiYjY1ZGE0YWYtYTEyYS00YTU5LTkzMTYtNDU0OWUxMmJhNjJjIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjczMzMyNDYzLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTg2NzE2MDA5ODYiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDkiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNTIiLCAicG9ydCI6ICIzMDAwMCIsICJpZCI6ICI5OTAwMDZiZC1jYjIwLTQ4MmYtOWM5Ny1mNWZjNjUzNTk2MDUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNDM0MzAxNDAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5ODY3MTYwMDk4NiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3LjEwNiIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4NjcxNjAwOTg2IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAibjE2OTg1NTEyNzMuYWFpZ2VmbS5jbiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMTUiLCAicG9ydCI6IDQ0MywgImlkIjogIjA3ZDJlZGFjLTJhM2ItNDhjMi1iOWExLWU5NjdjYmNlNDQ1YiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTYiLCAiYWRkIjogIjE1Ni4yNDkuMTguMTUxIiwgInBvcnQiOiAiMzAwMDAiLCAiaWQiOiAiODRkMWRlMTEtY2UxMi00YTE1LTgzMTItMTMzODM1NmQ0YWM0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjU3NDI0MzQ5Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTg2NzE2MDA5ODYiLCAidGxzIjogInRscyIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAibjE2OTc3NjU3NzIuaXp3aHZhbi5jbiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMjQiLCAicG9ydCI6IDQ0MywgImlkIjogImJhOTg0Njc4LWNhODEtNDQ0My1hOWRhLTU4YWRlYTQzZDViMCIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJuMTY5Nzc2NTc3Mi5pendodmFuLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTgzLjIzMy4xODcuMjE0IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNzcwZWU3MzAtMjQ1MC00ZTNjLWE2YzYtMzkzMmJkMzJhZmJkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ5NTUzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMjUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@54.36.174.181:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2029
vmess://eyJhZGQiOiAibjE2OTgxMTk2NDIuaXp3aHZhbi5jbiIsICJhaWQiOiAwLCAiaG9zdCI6ICJuMTY5ODExOTY0Mi5pendodmFuLmNuIiwgImlkIjogImZlNTdlMWYyLTcwNGItNDg5Ni05MmI2LWMyNTY3MzdlOTczOSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OTk5OVx1NmUyZlx1OTYzZlx1OTFjY1x1NGU5MSAzMSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiBmYWxzZSwgInNuaSI6ICJuMTY5ODExOTY0Mi5pendodmFuLmNuIn0=
vmess://eyJhZGQiOiAiYXBpLmpxdWVyeS5jb20iLCAiYWlkIjogMCwgImhvc3QiOiAic3ViLnhuLS05a3E4OWQ0eTBnLnRvcCIsICJpZCI6ICIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL29jdGF2aS5jZmQ6NDQzL2xpbmt2d3MiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAzMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

