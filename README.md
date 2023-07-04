
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                 | addr            | cn            | cc   | isp       | ip             | chatgpt          |
|---:|:-------------------|:----------------|:--------------|:-----|:----------|:---------------|:-----------------|
|  0 | [3](config/3.json) | 45.199.138.95   | Netherlands   | NL   | YISP B.V. | 154.84.1.229   | Yes (Region: NL) |
|  1 | [4](config/4.json) | 64.32.24.213    | United States | US   | SHARKTECH | 170.178.189.58 | Yes (Region: US) |
|  2 | [5](config/5.json) | 154.85.1.245    | Netherlands   | NL   | YISP B.V. | 154.84.1.206   | Yes (Region: NL) |
|  3 | [6](config/6.json) | 156.225.67.73   | Netherlands   | NL   | YISP B.V. | 154.84.1.19    | Yes (Region: NL) |
|  4 | [8](config/8.json) | 183.249.207.247 | United States | US   | CNSERVERS | 23.225.9.234   | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAzIiwgImFkZCI6ICI0NS4xOTkuMTM4Ljk1IiwgInBvcnQiOiAiNDk5MjEiLCAiaWQiOiAiZDMxMzM0ODQtZjJiZi00YjBjLThkMzgtZjhlNjQ1YjY1Njg3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjEzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ4NjU5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ1IiwgInBvcnQiOiAiNDc3MzEiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzMiLCAicG9ydCI6ICI1MzEyMyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMjExNTVlZmQtOGUyOS00M2QyLTk1YmMtZmUzMTkwZWNiMWM2IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTgzLjI0OS4yMDcuMjQ3IiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiODNhNDI0ZDgtNGJjYi00Y2VlLWIwMTYtMmM4ZjFkYjRhOTIxIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ3MDA5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZkNTlcdTZjNWZcdTc3MDFcdTRlM2RcdTZjMzRcdTVlMDJcdTc5ZmJcdTUyYTggOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

