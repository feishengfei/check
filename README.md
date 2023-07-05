
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr                     | cn          | cc   | isp       | ip                       | chatgpt          |
|---:|:-------------------|:-------------------------|:------------|:-----|:----------|:-------------------------|:-----------------|
|  0 | [2](config/2.json) | 154.85.1.245             | Netherlands | NL   | YISP B.V. | 154.84.1.206             | Yes (Region: NL) |
|  1 | [3](config/3.json) | 156.225.67.73            |             |      |           | 154.84.1.19              | Yes (Region: NL) |
|  2 | [4](config/4.json) | 45.58.186.91             |             |      |           | 64.32.2.26               | Yes (Region: US) |
|  3 | [5](config/5.json) | 94.177.25.209            |             |      |           | 2a05:1cc0:10:4::222:fffe | Yes (Region: EE) |
|  4 | [8](config/8.json) | south-connect.zhihuu.top |             |      |           | 23.225.9.234             | Yes (Region: US) |
|  5 | [9](config/9.json) | cfcdn.sanfencdn.net      |             |      |           | 104.237.159.122          | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ1IiwgInBvcnQiOiAiNDc3MzEiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1MzEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiNDUuNTguMTg2LjkxIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNGExMzhlMTktMDU5NS00ZDUxLTgzYzYtZmQyNzZjZjdkMzA3IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDUxMTQwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgzNzdcdTUxNzBcdTUzMTdcdTgzNzdcdTUxNzBcdTc3MDFcdTk2M2ZcdTU5YzZcdTY1YWZcdTcyNzlcdTRlMzlTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiOTQuMTc3LjI1LjIwOSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTcyMzFcdTZjOTlcdTVjM2NcdTRlOWEgIDUiLCAicG9ydCI6IDQ0MywgImlkIjogIjc1N2JkM2IxLTEyZjUtNDllMy1iODFiLTEwNDBmNzVhYWVkNyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMmRcdTU2ZmRcdTk2M2ZcdTkxY2NcdTRlOTEgOCIsICJhZGQiOiAic291dGgtY29ubmVjdC56aGlodXUudG9wIiwgInBvcnQiOiA0NDMsICJpZCI6ICI3NTk2ZmFjMS1lZTcyLTQ1OTAtOWZkOC05MmY3NjJlOWZhYWYiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogIm40MzkuemhpaHV1LnRvcCIsICJwYXRoIjogIi93czQzOSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiY2ZjZG4uc2FuZmVuY2RuLm5ldCIsICJhaWQiOiAwLCAiaG9zdCI6ICJ1czQuc2FuZmVuY2RuMS5jb20iLCAiaWQiOiAiZjExNGU2ZDktMGNkYS00ZmU4LWI3NjktM2JjZWIzYmNhNDUzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi96aC1jbiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDkiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

