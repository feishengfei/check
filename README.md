
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                     | cn   | cc   | isp   | ip              | chatgpt          |
|---:|:-------------------|:-------------------------|:-----|:-----|:------|:----------------|:-----------------|
|  0 | [1](config/1.json) | 107.167.7.22             |      |      |       | 107.167.18.50   | Yes (Region: US) |
|  1 | [2](config/2.json) | 198.2.204.249            |      |      |       | 142.0.133.253   | Yes (Region: US) |
|  2 | [6](config/6.json) | 156.225.67.144           |      |      |       | 154.84.1.37     | Yes (Region: NL) |
|  3 | [7](config/7.json) | 156.225.67.136           |      |      |       | 154.84.1.137    | Yes (Region: NL) |
|  4 | [8](config/8.json) | cf-lt.sharecentre.online |      |      |       | 169.197.141.187 | Yes (Region: US) |
|  5 | [9](config/9.json) | 64.32.4.36               |      |      |       | 107.167.13.162  | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJhZGQiOiAiMTA3LjE2Ny43LjIyIiwgInBvcnQiOiAiNDE2NTQiLCAiaWQiOiAiYmRlZTIwMmMtOGZhZS00NDFmLWE1ODgtN2JjNGQzODg3MDE5IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTk4LjIuMjA0LjI0OSIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0NjgwMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2UGV0YUV4cHJlc3MgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTQ0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjk5MDAwNmJkLWNiMjAtNDgyZi05Yzk3LWY1ZmM2NTM1OTYwNSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40MzQzMDE0MC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjgzNzc3ODc2MzgwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDciLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTM2IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjk2NGJmNDk5LTllYzAtNDM3OC05MmI2LTg3ZDhkODYxYjJkMCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy44MTY3ODAzNC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjgzNzc3ODc2MzgwIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjJkNWQ4YjljLThlYzQtNGEzNy1iNjEwLTc4ZTcxZTEzZWFlZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAibHYxLnNoYXJlY2VudHJlcHJvLm9yZyIsICJwYXRoIjogIi9zaGlya2VyIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAiNjQuMzIuNC4zNiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI4NjUzMDA0Zi1kZTY3LTQ0YzItOWNjZS1lMDgzMDkzM2ZiMDMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTc1ODg3NzYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4Mzc3Nzg3NjM4MCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

