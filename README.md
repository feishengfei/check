
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn            | cc   | isp                             | ip             | chatgpt          |
|---:|:---------------------|:-----------------------|:--------------|:-----|:--------------------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 156.225.67.106         | Netherlands   | NL   | YISP B.V.                       | 154.84.1.44    | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 45.199.138.146         | Netherlands   | NL   | YISP B.V.                       | 154.84.1.122   | Yes (Region: NL) |
|  2 | [8](config/8.json)   | n1698119642.izwhvan.cn | United States | US   | Alibaba US Technology Co., Ltd. | 47.76.46.141   | Yes (Region: US) |
|  3 | [10](config/10.json) | 142.4.112.157          | China         | CN   | PEG-SV                          | 192.74.242.129 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xMDYiLCAidiI6IDIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZSAgMyIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjI5YTVkNDhlLTI0ZjEtNDhmZC1hNWUxLTlhNDZjYjMxMDMyZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAid3d3LjQxNzU4MTEyLnh5eiIsICJ0bHMiOiAidGxzIiwgInBhdGgiOiAiL3BhdGgvMTY5ODY3MTYwMDk4NiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVNVUxUQUNPTVx1NjczYVx1NjIzZiA0IiwgImFkZCI6ICI0NS4xOTkuMTM4LjE0NiIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjRlYzBhZTYyLWRlMDktNDAyOS05MDRhLTAzMTNkNDYyOGVjZiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy4xOTIyOTM2Mi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk4OTMyNDAxNTc3IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgNSIsICJhZGQiOiAibjE2OTc2ODU0NjQuYWFpZ2VmbS5jbiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIxODcwMDJmZC1iOGFkLTRkMzYtYjRmYi0xYTMyMjRjYzk5ZTIiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm4xNjk3Njg1NDY0LmFhaWdlZm0uY24iLCAicGF0aCI6ICIvIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgOCIsICJhZGQiOiAibjE2OTgxMTk2NDIuaXp3aHZhbi5jbiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICJmZTU3ZTFmMi03MDRiLTQ4OTYtOTJiNi1jMjU2NzM3ZTk3MzkiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIm4xNjk4MTE5NjQyLml6d2h2YW4uY24iLCAicGF0aCI6ICIvIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSCAxMCIsICJhZGQiOiAiMTQyLjQuMTEyLjE1NyIsICJwb3J0IjogIjMwMDAwIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy42NzAyMzU4Mi54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjk5MDE3ODIxMTQ4IiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
```

