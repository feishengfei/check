
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                    | ip             | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:-----------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 107.167.16.85            | United States | US   | SHARKTECH              | 170.178.189.50 | Yes (Region: US) |
|  1 | [6](config/6.json)   | 154.85.1.245             | Netherlands   | NL   | YISP B.V.              | 154.84.1.206   | Yes (Region: NL) |
|  2 | [8](config/8.json)   | cf-lt.sharecentre.online | United States | US   | CNSERVERS              | 23.225.9.234   | Yes (Region: US) |
|  3 | [9](config/9.json)   | cfcdn.sanfencdn.net      | United States | US   | Akamai Connected Cloud | 45.33.45.177   | Yes (Region: US) |
|  4 | [16](config/16.json) | dl8.v001sssv.pw          | France        | FR   | OVH SAS                | 51.178.24.58   | Yes (Region: FR) |

## Valid
```
vmess://eyJhZGQiOiAiMTA3LjE2Ny4xNi44NSIsICJhaWQiOiAiNjQiLCAiYWxwbiI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiNzY0MGExZTctOTcwMS00MjhlLWE0YjItMTliM2U3ZGQ2ZjlmIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDU2ODkiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAiMTU0Ljg1LjEuMjQ1IiwgInBvcnQiOiAiNDc3MzEiLCAiaWQiOiAiMWQ0NzRmMGItZTc4ZC00YWY5LWJjNGEtYTQ2NzQ2N2JjN2E3IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogODAsICJpZCI6ICI1Zjc1MWM2ZS01MGIxLTQ3OTctYmE4ZS02ZmZlMzI0YTBiY2UiLCAiYWlkIjogMCwgInNjeSI6ICJhZXMtMTI4LWdjbSIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJjYS5pbG92ZXNjcC5jb20iLCAicGF0aCI6ICIvc2hpcmtlciIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDkiLCAiYWRkIjogImNmY2RuLnNhbmZlbmNkbi5uZXQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiZjExNGU2ZDktMGNkYS00ZmU4LWI3NjktM2JjZWIzYmNhNDUzIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1czQuc2FuZmVuY2RuMS5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAidXMxLnNhbmZlbmNkbjEuY29tIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICJkbDgudjAwMXNzc3YucHciLCAicG9ydCI6ICI4MCIsICJpZCI6ICIzZmVjNzE4Mi0wMmZiLTQ3MzAtOWI5Ny00YzlhZWU1NjNlZjYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImRsOC52MDAxc3Nzdi5wdyIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

