
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn            | cc   | isp          | ip             | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:-------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 140.99.77.12   | United States | US   | DEDIPATH-LLC | 140.99.150.90  | Yes (Region: US) |
|  1 | [6](config/6.json)   | 45.92.160.20   | United States | US   | DEDIPATH-LLC | 193.202.44.194 | Yes (Region: US) |
|  2 | [7](config/7.json)   | 156.225.67.105 | Netherlands   | NL   | YISP B.V.    | 154.84.1.44    | Yes (Region: NL) |
|  3 | [8](config/8.json)   | cf.515188.xyz  | United States | US   | CNSERVERS    | 23.225.9.234   | Yes (Region: US) |
|  4 | [9](config/9.json)   | 192.74.228.189 | United States | US   | PEGTECHINC   | 142.0.129.201  | Yes (Region: US) |
|  5 | [10](config/10.json) | 192.74.228.171 | United States | US   | PEGTECHINC   | 142.0.129.201  | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmREYXRhYmlsaXR5IDMiLCAiYWRkIjogIjE0MC45OS43Ny4xMiIsICJwb3J0IjogIjU0Nzc0IiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiNDUuOTIuMTYwLjIwIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NmIyN1x1NzZkZiAgNiIsICJwb3J0IjogNDc4MzksICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDciLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTA1IiwgInBvcnQiOiAiNDkxMDEiLCAiaWQiOiAiMjlhNWQ0OGUtMjRmMS00OGZkLWE1ZTEtOWE0NmNiMzEwMzJmIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIlx1ZDgzY1x1ZGRmYVx1ZDgzY1x1ZGRmOFVTXHU3ZjhlXHU1NmZkKHlvdXR1YmVcdTk2M2ZcdTRmMWZcdTc5ZDFcdTYyODAyKSIsICJwYXRoIjogIi9pc2FpZnFhYWdwaSIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLjUxNTE4OC54eXoiLCAicG9ydCI6ICI4MCIsICJpZCI6ICJhNTc1Njg1My00YTgwLTQ2OGEtYWY2Mi0xMDU2NTkxOGY1OGYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNzcnN1Yi52MDMuc3Nyc3ViLmNvbSIsICJwYXRoIjogIi9hcGkvdjMvZG93bmxvYWQuZ2V0RmlsZSIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTkyLjc0LjIyOC4xODkiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU1NzIzXHU0ZjU1XHU1ODVlUEVHIFRFQ0hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOSIsICJwb3J0IjogNDI4NTcsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxMCIsICJhZGQiOiAiMTkyLjc0LjIyOC4xNzEiLCAicG9ydCI6ICI0Mjg1NyIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMDUxYjg0NGYtZWZlMy00ODQ3LTkyYWEtNjZiNWRlMGI2ZDRlIiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL3BvaXNvbiIsICJob3N0IjogInMxLjJiMi50b3AiLCAidGxzIjogIiJ9
```

