
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp        | ip                                  | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:-----------|:------------------------------------|:-----------------|
|  0 | [11](config/11.json) | www.75409854.xyz            | United States | US   | SHARKTECH  | 107.167.22.10                       | Yes (Region: US) |
|  1 | [13](config/13.json) | 45.199.138.191              | Netherlands   | NL   | YISP B.V.  | 2a02:2a38:1:2796:ec4:7aff:fe81:77ba | Yes (Region: NL) |
|  2 | [19](config/19.json) | us02.shawbrothersstudio.com | United States | US   | NETLAB-SDN | 154.40.56.206                       | Yes (Region: US) |
|  3 | [20](config/20.json) | 154.85.1.244                | Netherlands   | NL   | YISP B.V.  | 154.84.1.216                        | Yes (Region: NL) |
|  4 | [24](config/24.json) | 156.225.67.104              | Netherlands   | NL   | YISP B.V.  | 154.84.1.44                         | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAiYWRkIjogInd3dy43NTQwOTg1NC54eXoiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiNDUuMTk5LjEzOC4xOTEiLCAiYWlkIjogNjQsICJob3N0IjogInd3dy40MjA3NzIzMC54eXoiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9wYXRoLzE2OTYyNTE1MjI0MzgiLCAicG9ydCI6IDMwMDAwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiAxMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpoZzloNUtwTW1KTGxpNlc2UWpkMnlp@us02.shawbrothersstudio.com:43642#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E6%96%B0%E5%9B%BD%E4%BF%A1%E9%80%9A%E4%BF%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2019
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjAiLCAiYWRkIjogIjE1NC44NS4xLjI0NCIsICJwb3J0IjogMzAwMDAsICJpZCI6ICIxZDQ3NGYwYi1lNzhkLTRhZjktYmM0YS1hNDY3NDY3YmM3YTciLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuMjgxMTUzNjEueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5Njk0NDgwNjk2MSIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDI0IiwgImFkZCI6ICIxNTYuMjI1LjY3LjEwNCIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

