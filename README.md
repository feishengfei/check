
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    
|    | id                 | addr          | cn         | cc   | isp     | ip             | chatgpt          |
|---:|:-------------------|:--------------|:-----------|:-----|:--------|:---------------|:-----------------|
|  0 | [3](config/3.json) | cf.noaries.de | Luxembourg | LU   | PONYNET | 107.189.28.253 | Yes (Region: LU) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDMiLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6ICI4MDgwIiwgImlkIjogIjRmN2Q1ZDQzLTIyNmUtNDhkOC05ZGYwLTVlOGJmOWY3NzI4OCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiYnV5dm0uY2xvdWRmbGFyZS5xdWVzdCIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiJ9
```

|    | id                           | addr               |
|---:|:-----------------------------|:-------------------|
|  0 | [1](config_invalid/1.json)   | 194.61.120.50      |
|  1 | [2](config_invalid/2.json)   | 185.162.228.2      |
|  2 | [4](config_invalid/4.json)   | f-us2.wvvvv.eu.org |
|  3 | [5](config_invalid/5.json)   | 203.30.188.2       |
|  4 | [6](config_invalid/6.json)   | 185.162.228.229    |
|  5 | [7](config_invalid/7.json)   | 172.64.173.160     |
|  6 | [8](config_invalid/8.json)   | 203.30.189.1       |
|  7 | [9](config_invalid/9.json)   | 203.24.108.100     |
|  8 | [10](config_invalid/10.json) | 162.159.255.200    |
|  9 | [11](config_invalid/11.json) | 103.160.204.13     |
| 10 | [12](config_invalid/12.json) | cf.515188.xyz      |

## Invalid
```
vmess://eyJhZGQiOiAiMTk0LjYxLjEyMC41MCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiNTU0OWYzNjAtZjU5MC00NzlhLWJhNDctMjUyMDczYzA1M2JjIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDI1NzQ0LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTgyZjFcdTU2ZmQgIDEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDIiLCAiYWRkIjogIjE4NS4xNjIuMjI4LjIiLCAicG9ydCI6ICI4MCIsICJpZCI6ICIxN2IyYTMxMy0zN2EwLTQ5NDUtYThlNC1lNjMzNzU1MDZiNGEiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImZyLnYycmF5MS54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDQiLCAiYWRkIjogImYtdXMyLnd2dnZ2LmV1Lm9yZyIsICJwb3J0IjogIjIxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZGExZDM3Mi1lYzYwLTRiODktOGEzZi03OTE1OTQzOGM2ZjAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICJmLXVzMi53dnZ2di5ldS5vcmciLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMjAzLjMwLjE4OC4yIiwgImFpZCI6IDAsICJob3N0IjogImZyLnYycmF5MS54eXoiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFMeW5kaHVyc3QgU2Vjb25kYXJ5IENvbGxlZ2UgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDYiLCAiYWRkIjogIjE4NS4xNjIuMjI4LjIyOSIsICJwb3J0IjogODAsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImxnLnYycmF5OC54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTcyLjY0LjE3My4xNjAiLCAiYWlkIjogMCwgImhvc3QiOiAiY2EuaWxvdmVzY3AuY29tIiwgImlkIjogIjJlNDk2NzU4LTk1MGUtNDU0OS04ODQyLWQ1ZWVjOThkOWZkZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvc2hpcmtlciIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgNyIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJhZGQiOiAiMjAzLjMwLjE4OS4xIiwgImFpZCI6IDAsICJob3N0IjogIjE1NC52MnJheTMueHl6IiwgImlkIjogIjQwZDQ5NmE2LWNlZWItNDA5Ni1iYWViLTRjYzUyYjIwNTYyMSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvRUNUQ0owREYiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2ZmIzXHU1OTI3XHU1MjI5XHU0ZTlhS29vd2VlcnVwIFNlY29uZGFyeSBDb2xsZWdlIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2MgOSIsICJhZGQiOiAiMjAzLjI0LjEwOC4xMDAiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImxnLnYycmF5OC54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICIxNjIuMTU5LjI1NS4yMDAiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1MjQ2NmRjMi0zNTUwLTQzMTAtOTEwYy03NGI3YmY4YTAyMGUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVzLTEuYWN5dW4uZXUub3JnIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTAzLjE2MC4yMDQuMTMiLCAiYWlkIjogMCwgImhvc3QiOiAibGcyLnYycmF5Ni54eXoiLCAiaWQiOiAiNTZhMjE4OGItMmFiNy00MDJjLWI5YjgtMzQ4NDdmZGYwOTU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi81UU5ST1NSViIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDExIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICJjZi41MTUxODgueHl6IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiZjZhYTQ0NDAtZTdiZS00NGUxLTgwZTEtN2U0NWNjZDc5NmNjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzc3JzdWIudjAxLnNzcnN1Yi5jb20iLCAicGF0aCI6ICIvYXBpL3YzL2Rvd25sb2FkLmdldEZpbGUiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
```

