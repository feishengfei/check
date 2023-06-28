
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn            | cc   | isp               | ip             | chatgpt          |
|---:|:---------------------|:------------------------|:--------------|:-----|:------------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 142.4.99.89             | China         | CN   | PEGTECHINC        | 142.4.99.65    | Yes (Region: US) |
|  1 | [4](config/4.json)   | 64.32.20.103            | United States | US   | SHARKTECH         | 64.32.0.58     | Yes (Region: US) |
|  2 | [6](config/6.json)   | 172.247.67.46           | United States | US   | CNSERVERS         | 23.225.9.234   | Yes (Region: US) |
|  3 | [8](config/8.json)   | cn-to-hk-443.db-link.in | Germany       | DE   | AS-GLOBALTELEHOST | 193.108.118.34 | Yes (Region: DE) |
|  4 | [18](config/18.json) | 64.32.4.44              | United States | US   | SHARKTECH         | 107.167.13.162 | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMTQyLjQuOTkuODkiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJiNjVkYTRhZi1hMTJhLTRhNTktOTMxNi00NTQ5ZTEyYmE2MmMiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDMzNzksICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNjQuMzIuMjAuMTAzIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiYzFiYWQ5YTYtMTQ4Mi00OTQxLWEwYzQtZTg1ZjNjYmJjYjVhIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQwMDM5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZDb3BlcmF0aW9uIENvbG9jdGlvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA2IiwgImFkZCI6ICIxNzIuMjQ3LjY3LjQ2IiwgInBvcnQiOiAiNTAwMzUiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjIyNzhlZmU0LWFkMGMtNDdjZS05NDgwLTA2ODYwODM2OGQ3NiIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDFcdTRlMmRcdTUzNGVcdTc1MzVcdTRmZTEoSGlOZXQpIDgiLCAiYWRkIjogImNuLXRvLWhrLTQ0My5kYi1saW5rLmluIiwgInBvcnQiOiA0NDMsICJpZCI6ICI0MGNiYzc1MC1hMTgyLTNmZTItODgzMi05ZmE2MDA2MzU0Y2YiLCAiYWlkIjogMSwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImZyZWUtdG8tdXMtMDEuZGItbGluay5pbiIsICJwYXRoIjogIi9kYiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTgiLCAiYWRkIjogIjY0LjMyLjQuNDQiLCAicG9ydCI6ICI0MzE2NiIsICJpZCI6ICI4NjUzMDA0Zi1kZTY3LTQ0YzItOWNjZS1lMDgzMDkzM2ZiMDMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
```

