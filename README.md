
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.110.144   | China         | CN   | PEG-SV            | 142.4.110.137  | Yes (Region: US) |
|  1 | [3](config/3.json)   | 142.4.99.76     | United States | US   | PEG-SV            | 142.4.99.65    | Yes (Region: US) |
|  2 | [4](config/4.json)   | 40.kccic2pa.xyz | United States | US   | OVH SAS           | 51.81.211.205  | Yes (Region: US) |
|  3 | [5](config/5.json)   | 142.4.114.20    | China         | CN   | PEG-SV            | 142.0.138.129  | Yes (Region: US) |
|  4 | [6](config/6.json)   | api.jquery.com  | United States | US   | AS-GLOBALTELEHOST | 158.51.123.252 | Yes (Region: US) |
|  5 | [7](config/7.json)   | 156.225.67.205  | Netherlands   | NL   | YISP B.V.         | 154.84.1.161   | Yes (Region: NL) |
|  6 | [8](config/8.json)   | 156.225.67.78   | Poland        | PL   | OVH SAS           | 54.36.174.181  | Yes (Region: FR) |
|  7 | [10](config/10.json) | 156.245.8.169   | Netherlands   | NL   | YISP B.V.         | 154.84.1.158   | Yes (Region: NL) |
|  8 | [11](config/11.json) | 156.225.67.181  | Netherlands   | NL   | YISP B.V.         | 154.84.1.138   | Yes (Region: NL) |
|  9 | [12](config/12.json) | 156.245.8.151   |               |      |                   | 154.84.1.148   | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAyIiwgImFkZCI6ICIxNDIuNC4xMTAuMTQ0IiwgInBvcnQiOiA0NDMsICJpZCI6ICI2OGQyMzhjZS0zY2ExLTQ2ZGMtYjgzMy1hMDkxNmM4MjlhZDMiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMjgyNTE2NTgueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NTIwNDU2NzIzNyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAzIiwgImFkZCI6ICIxNDIuNC45OS43NiIsICJwb3J0IjogNDQzLCAiaWQiOiAiYjY1ZGE0YWYtYTEyYS00YTU5LTkzMTYtNDU0OWUxMmJhNjJjIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjczMzMyNDYzLnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTUyMDQ1NjcyMzciLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggNCIsICJhZGQiOiAiNDAua2NjaWMycGEueHl6IiwgInBvcnQiOiAiNTAwNDAiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjVjM2Q2MGMxLWVjMmItNDFmNC1iZDIyLWI3MzM2ZDdlMzdiYiIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogImlwMjY0ODQyODA3NS5tb2Jnc2xiLnRiY2FjaGUuY29tIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA1IiwgImFkZCI6ICIxNDIuNC4xMTQuMjAiLCAicG9ydCI6IDQ0MywgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40NzczNDk1NC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk1MTc3MDYyOTU2IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDYiLCAiYWRkIjogImFwaS5qcXVlcnkuY29tIiwgInBvcnQiOiA0NDMsICJpZCI6ICIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInN1Yi55aWZlbmppY2hhbmcudG9wIiwgInBhdGgiOiAiL29saXYuYmVhdXR5OjQ0My9saW5rdndzIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDciLCAiYWRkIjogIjE1Ni4yMjUuNjcuMjA1IiwgInBvcnQiOiA0NDMsICJpZCI6ICJkNzczNTA1OC0xZGFjLTQ2MTgtOTlmZi0wYWEwNDQxZWMyZDciLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMjAxNjMzMjIueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NTIwNDU2NzIzNyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDgiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzgiLCAicG9ydCI6IDQ0MywgImlkIjogIjNlMDE2YzRkLTk4NmUtNDJkZi04MzhjLTYwNDZmM2Q4OWVjZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy41NjQyNzk5NC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk1MjA0NTY3MjM3IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDEwIiwgImFkZCI6ICIxNTYuMjQ1LjguMTY5IiwgInBvcnQiOiA0NDMsICJpZCI6ICIzYTNjOGE5Yy0zMzRlLTQzNjAtYWRiOC1hODBhNTdkZGNiYmYiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMTYwNDY2MjYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NTE3NzA2Mjk1NiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDExIiwgImFkZCI6ICIxNTYuMjI1LjY3LjE4MSIsICJwb3J0IjogNDQzLCAiaWQiOiAiMTExMTdkNGMtM2I2YS00ZTc2LThiY2MtMmI0MWIzZTljYTkzIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3LjExNjQ5NzY5Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTUyMDQ1NjcyMzciLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDEyIiwgImFkZCI6ICIxNTYuMjQ1LjguMTUxIiwgInBvcnQiOiA0NDMsICJpZCI6ICI4NGQxZGUxMS1jZTEyLTRhMTUtODMxMi0xMzM4MzU2ZDRhYzQiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuNTc0MjQzNDkueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NTIwNDU2NzIzNyIsICJ0bHMiOiAidGxzIn0=
```

