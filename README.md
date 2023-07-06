
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp        | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-----------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 154.85.1.123   | Netherlands   | NL   | YISP B.V.  | 154.84.1.232   | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 142.4.99.89    | United States | US   | PEGTECHINC | 142.4.99.65    | Yes (Region: US) |
|  2 | [4](config/4.json)   | 156.249.18.16  | Netherlands   | NL   | YISP B.V.  | 154.84.1.193   | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 45.199.138.89  | Netherlands   | NL   | YISP B.V.  | 154.84.1.159   | Yes (Region: NL) |
|  4 | [8](config/8.json)   | 202.79.174.157 | United States | US   | CNSERVERS  | 23.225.9.234   | Yes (Region: US) |
|  5 | [10](config/10.json) | 139.99.245.164 | Australia     | AU   | OVH SAS    | 139.99.130.144 | Yes (Region: AU) |

## Valid
```
vmess://eyJhZGQiOiAiMTU0Ljg1LjEuMTIzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiMTMwYzlmMmUtNDJiMS00ZWJmLWIzNDUtZTI2NDU2YTA2MWY5IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQwMjk4LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTQyLjQuOTkuODkiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0ggMyIsICJwb3J0IjogNDMzNzksICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJhZGQiOiAiMTU2LjI0OS4xOC4xNiIsICJwb3J0IjogIjQ3MjUwIiwgImlkIjogIjM3NWU3MGYwLTVkNDYtNDc2Zi04ZDY5LTBmYjM1YzU1NDhhOSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA1IiwgImFkZCI6ICI0NS4xOTkuMTM4Ljg5IiwgInBvcnQiOiAiNDA2NTYiLCAiaWQiOiAiMDc4ZWIyNGQtOGQxZC00ZmJkLWI5MTQtZWU1OGE4OTdhMzVlIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMjAyLjc5LjE3NC4xNTciLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmQkdQLk5FVCBDTjJcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJwb3J0IjogNTUyNjQsICJpZCI6ICIxMjFjOWM4OS03ZDExLTRmNDktOTExMi1kYzFlODUzNjNmNmYiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2NPVkggMTAiLCAiYWRkIjogIjEzOS45OS4yNDUuMTY0IiwgInBvcnQiOiAiNDk5MjEiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRlNlx1ZDgzY1x1ZGRmYUFVXHU2ZmIzXHU1OTI3XHU1MjI5XHU0ZTlhKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODApIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
```

