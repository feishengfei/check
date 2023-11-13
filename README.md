
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn            | cc   | isp                              | ip             | chatgpt          |
|---:|:---------------------|:-----------------------|:--------------|:-----|:---------------------------------|:---------------|:-----------------|
|  0 | [9](config/9.json)   | cfcdn3.sanfencdn9.com  | Japan         | JP   | Eons Data Communications Limited | 38.207.152.110 | Yes (Region: US) |
|  1 | [12](config/12.json) | 183.233.187.214        | Hong Kong     | HK   | CNSERVERS                        | 172.247.18.74  | Yes (Region: US) |
|  2 | [16](config/16.json) | n1699253769.aaigefm.cn | United States | US   | Alibaba US Technology Co., Ltd.  | 47.76.34.124   | Yes (Region: US) |
|  3 | [22](config/22.json) | n1697685464.aaigefm.cn | United States | US   | Alibaba US Technology Co., Ltd.  | 47.76.44.192   | Yes (Region: US) |
|  4 | [24](config/24.json) | n1697555560.aaigefm.cn | United States | US   | Alibaba US Technology Co., Ltd.  | 47.76.35.240   | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiY2ZjZG4zLnNhbmZlbmNkbjkuY29tIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgOSIsICJwb3J0IjogODAsICJpZCI6ICIyY2Y0NzJkNC03MWFhLTQ2MzktOThjOS1iZDEzZTE2NDllMTMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAianAxN2FhYjcyYTcuY2h2c2lmZXRyai54eXoiLCAicGF0aCI6ICIvdmlkZW8vdXViQ2RKdEsiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjE4My4yMzMuMTg3LjIxNCIsICJwb3J0IjogIjM4OTYyIiwgImlkIjogIjc3MGVlNzMwLTI0NTAtNGUzYy1hNmM2LTM5MzJiZDMyYWZiZCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMTYiLCAiYWRkIjogIm4xNjk5MjUzNzY5LmFhaWdlZm0uY24iLCAicG9ydCI6IDQ0MywgImlkIjogIjk4MmZhZGQxLTNlNWYtNGFhMy04NTUyLWVkNmZkYTIzNDE0YSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAibjE2OTkyNTM3NjkuYWFpZ2VmbS5jbiIsICJwYXRoIjogIi8iLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAibjE2OTc2ODU0NjQuYWFpZ2VmbS5jbiIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMjIiLCAicG9ydCI6IDQ0MywgImlkIjogIjE4NzAwMmZkLWI4YWQtNGQzNi1iNGZiLTFhMzIyNGNjOTllMiIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJuMTY5NzY4NTQ2NC5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmZcdTk2M2ZcdTkxY2NcdTRlOTEgMjQiLCAiYWRkIjogIm4xNjk3NTU1NTYwLmFhaWdlZm0uY24iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNTY2OTFjM2MtYjlhNS00NDBmLWE2NzgtNDc4NjE4ODU0ZTc1IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJuMTY5NzU1NTU2MC5hYWlnZWZtLmNuIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

