
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn             | cc   | isp                              | ip                        | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:---------------|:-----|:---------------------------------|:--------------------------|:-----------------|
|  0 | [3](config/3.json)   | 83.142.225.20                                                                                   | United Kingdom | GB   | Iomart Cloud Services Limited    | 83.142.225.28             | Yes (Region: GB) |
|  1 | [8](config/8.json)   | 173.245.49.94                                                                                   | United States  | US   | Eons Data Communications Limited | 65.75.221.195             | Yes (Region: US) |
|  2 | [9](config/9.json)   | ak1749.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | United Kingdom | GB   | OVH SAS                          | 145.239.6.202             | Yes (Region: GB) |
|  3 | [14](config/14.json) | cf.noaries.de                                                                                   | Italy          | IT   | CLOUDFLARENET                    | 2a09:bac5:4228:187::27:84 | Yes (Region: IT) |
|  4 | [20](config/20.json) | cfcdn.sanfencdn.net                                                                             | United States  | US   | Eons Data Communications Limited | 65.75.221.195             | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiODMuMTQyLjIyNS4yMCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjUyNjdjYTcxLTk3ZTYtNDRjOC04ZmI1LTlmZTRhZmUwOTU0ZSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTkyMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4MmYxXHU1NmZkICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTVmMTdcdTU0MDlcdTVjM2NcdTRlOWFcdTVkZGVcdTk2M2ZcdTRlYzBcdTY3MmNOViBORVhUXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDgiLCAiYWRkIjogIjE3My4yNDUuNDkuOTQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiOTU4OGNiMGYtNTEwMi00ZTY2LWQ1ZmItZjk2Y2JhOWFjZGRhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ0b3UudnRjc3MudG9wIiwgInBhdGgiOiAiL3FhenhjdjUyMiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@ak1749.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:4444#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%20%209
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiMjA1MiIsICJpZCI6ICI2N2M1Y2U0NS03YjQ4LTQ3M2UtYmYyNS1lNGM4MzBiMGVkMjQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImF6c3R1LWl0LmlpaW8ud2lraSIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE5IiwgImFkZCI6ICJjZmNkbi5zYW5mZW5jZG4ubmV0IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImRkODMxNGNjLTM3NTQtNDE2ZC05NDU2LTA5OTFmMmU3NDc1MyIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMyLnNhbmZlbmNkbi5uZXQiLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

