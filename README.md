
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn            | cc   | isp       | ip             | chatgpt          |
|---:|:---------------------|:----------------------------|:--------------|:-----|:----------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 156.225.67.104              | Netherlands   | NL   | YISP B.V. | 154.84.1.44    | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 183.238.202.173             | Hong Kong     | HK   | CNSERVERS | 156.227.19.218 | Yes (Region: US) |
|  2 | [5](config/5.json)   | 142.4.110.145               | China         | CN   | PEG-SV    | 142.4.110.137  | Yes (Region: US) |
|  3 | [9](config/9.json)   | www.75409854.xyz            | United States | US   | SHARKTECH | 107.167.22.10  | Yes (Region: US) |
|  4 | [15](config/15.json) | us01.shawbrothersstudio.com | United States | US   | HVC-AS    | 38.180.5.0     | Yes (Region: US) |
|  5 | [22](config/22.json) | 67.21.90.5                  | United States | US   | SHARKTECH | 107.167.22.10  | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDIiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA0IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy40MTc1ODExMi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMyIsICJhZGQiOiAiMTgzLjIzOC4yMDIuMTczIiwgInBvcnQiOiAiNTE5MDQiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCA1IiwgImFkZCI6ICIxNDIuNC4xMTAuMTQ1IiwgInBvcnQiOiAzMDAwMCwgImlkIjogIjY4ZDIzOGNlLTNjYTEtNDZkYy1iODMzLWEwOTE2YzgyOWFkMyIsICJhaWQiOiA2NCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInd3dy4yODI1MTY1OC54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk2OTQ0ODA2OTYxIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJhZGQiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwb3J0IjogNDQzLCAiaWQiOiAiMjhkZDZjMjYtMDVhNS00YmJhLThhNWQtMDUyYjcwYWMxM2IyIiwgImFpZCI6IDY0LCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpMYW02bWdJMFpuSXFUNDU5Q1RUT0pS@us01.shawbrothersstudio.com:19922#github.com/freefq%20-%20%E5%8C%97%E4%BA%AC%E5%B8%82%E7%A7%BB%E5%8A%A8%2015
vmess://eyJhZGQiOiAiNjcuMjEuOTAuNSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya1RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjIiLCAicG9ydCI6IDQ0MywgImlkIjogIjI4ZGQ2YzI2LTA1YTUtNGJiYS04YTVkLTA1MmI3MGFjMTNiMiIsICJhaWQiOiAiNjQiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAid3d3Ljc1NDA5ODU0Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2OTQ0Mjk5MDg3NDgiLCAidGxzIjogInRscyJ9
```

