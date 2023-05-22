
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp                              | ip                                 | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:---------------------------------|:-----------------------------------|:-----------------|
|  0 | [3](config/3.json)   | 23.234.198.83       |               |      |                                  | 2607:f130:109:0:225:90ff:fe79:7d34 | Yes (Region: US) |
|  1 | [8](config/8.json)   | 23.227.38.99        |               |      |                                  | 2a09:bac5:422a:187::27:84          | Yes (Region: IT) |
|  2 | [12](config/12.json) | 139.99.180.115      | Australia     | AU   | OVH SAS                          | 2402:1f00:8100:371::               | Yes (Region: AU) |
|  3 | [14](config/14.json) | cf.noaries.de       | Italy         | IT   | CLOUDFLARENET                    | 2a09:bac5:422a:187::27:84          | Yes (Region: IT) |
|  4 | [19](config/19.json) | cfcdn.sanfencdn.net | United States | US   | Eons Data Communications Limited | 65.75.221.195                      | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiMjMuMjM0LjE5OC44MyIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogImE5YWJmM2U3LTg3ZjQtNDczZC04ZDAzLTJmMjZjYTRiMzU4MyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogMzQ4ODgsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogIjIzLjIyNy4zOC45OSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI4NmQzNzUyNi01NzU4LTRjZWMtODYyZi1kZjQwNGIzMTMwODYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIjEuZnJlZWsxLnh5eiIsICJwYXRoIjogIi8zRzZXUERMNyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTM5Ljk5LjE4MC4xMTUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2ZmIzXHU1OTI3XHU1MjI5XHU0ZTlhXHU2MDg5XHU1YzNjT1ZIIDEyIiwgInBvcnQiOiAzMzUwNSwgImlkIjogIjZjMDRhMjczLTczMDItNGUwOS05Y2VkLWFlZGFhYTc0NjFhZiIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiMjA1MiIsICJpZCI6ICI2N2M1Y2U0NS03YjQ4LTQ3M2UtYmYyNS1lNGM4MzBiMGVkMjQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImF6c3R1LWl0LmlpaW8ud2lraSIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE5IiwgImFkZCI6ICJjZmNkbi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImRkODMxNGNjLTM3NTQtNDE2ZC05NDU2LTA5OTFmMmU3NDc1MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMyLnNhbmZlbmNkbi5uZXQiLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

