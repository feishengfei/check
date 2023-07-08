
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp          | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 142.4.99.91    | United States | US   | PEGTECHINC   | 142.4.99.65    | Yes (Region: US) |
|  1 | [3](config/3.json)   | 64.32.4.47     | United States | US   | SHARKTECH    | 107.167.13.162 | Yes (Region: US) |
|  2 | [4](config/4.json)   | 45.199.138.121 | Netherlands   | NL   | YISP B.V.    | 46.182.107.129 | Yes (Region: US) |
|  3 | [5](config/5.json)   | 156.225.67.152 | Netherlands   | NL   | YISP B.V.    | 154.84.1.194   | Yes (Region: NL) |
|  4 | [6](config/6.json)   | 156.225.67.105 | Netherlands   | NL   | YISP B.V.    | 154.84.1.44    | Yes (Region: NL) |
|  5 | [8](config/8.json)   | cf2.992688.xyz | United States | US   | CNSERVERS    | 23.225.9.234   | Yes (Region: US) |
|  6 | [10](config/10.json) | 140.99.77.12   | United States | US   | DEDIPATH-LLC | 140.99.150.90  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuOTkuOTEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0ggMiIsICJwb3J0IjogNDMzNzksICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjQuMzIuNC40NyIsICJwb3J0IjogIjQzMTY2IiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjEyMSIsICJwb3J0IjogIjUxMjA0IiwgImlkIjogIjk1NDlhMmNmLTEyOWItNDNhMS04OGRiLWVmN2Y2NDhkZTc0YSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZjNcdWQ4M2NcdWRkZjFOTFx1ODM3N1x1NTE3MCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNTIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJhN2ZhOGYxNC00ZmI2LTQyODAtOTAwNS1kNmJiZTk5YzVkYTkiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDYzMTQsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA1IiwgInBvcnQiOiAiNDkxMDEiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi9pc2FpZnFhYWdwaSIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiY2YyLjk5MjY4OC54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAibzEuOTkyNjg4Lnh5eiIsICJpZCI6ICI2YjA1NmEyYy1iODIxLTQ0YjItY2Y2Ni01OWExMTI2ZjZjOTUiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogODA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmREYXRhYmlsaXR5IDEwIiwgImFkZCI6ICIxNDAuOTkuNzcuMTIiLCAicG9ydCI6ICI1NDc3NCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJob3N0IjogIiIsICJ0bHMiOiAiIn0=
```

