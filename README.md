
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn             | cc   | isp     | ip                   | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:---------------|:-----|:--------|:---------------------|:-----------------|
|  0 | [5](config/5.json)   | 145.239.6.202                                                                                   | United Kingdom | GB   | OVH SAS | 145.239.6.202        | Yes (Region: GB) |
|  1 | [8](config/8.json)   | cf.noaries.de                                                                                   |                |      |         | 154.84.1.145         | Yes (Region: NL) |
|  2 | [9](config/9.json)   | 206.189.98.76                                                                                   |                |      |         | 206.189.98.76        | Yes (Region: NL) |
|  3 | [12](config/12.json) | cdn.noice.id                                                                                    |                |      |         | 143.198.94.243       | Yes (Region: SG) |
|  4 | [13](config/13.json) | 64.32.4.36                                                                                      |                |      |         | 107.167.13.162       | Yes (Region: US) |
|  5 | [14](config/14.json) | ak1749.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou |                |      |         | 145.239.6.202        | Yes (Region: GB) |
|  6 | [21](config/21.json) | 174.136.205.11                                                                                  |                |      |         | 2605:52c0:1001:237:: | Yes (Region: US) |
|  7 | [22](config/22.json) | 8.v2-ray.cyou                                                                                   |                |      |         | 18.179.36.139        | Yes (Region: JP) |

## Valid
```
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@145.239.6.202:4444#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%20%205
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6ICIyMDgyIiwgImlkIjogIjY3YzVjZTQ1LTdiNDgtNDczZS1iZjI1LWU0YzgzMGIwZWQyNCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGVkaXBhdGgyLmlpaW8ud2lraSIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMjA2LjE4OS45OC43NiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiODVjM2ZmNmEtYmI1Yy00NjE1LTk3ZmUtYWM3NWJiY2U3YzY2IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi90ZWxlZ3JhbTpVQ0lSQU5JUiIsICJwb3J0IjogODA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4Mzc3XHU1MTcwICA5IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTMiLCAiYWRkIjogIjY0LjMyLjQuMzYiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiODY1MzAwNGYtZGU2Ny00NGMyLTljY2UtZTA4MzA5MzNmYjAzIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjU3NTg4Nzc2Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2ODQ5MDc1MTE4NDIiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@ak1749.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:4444#github.com/freefq%20-%20%E8%8B%B1%E5%9B%BD%20%2014
vmess://eyJhZGQiOiAiMTc0LjEzNi4yMDUuMTEiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkdGhlcGxhbmV0IDIxIiwgInBvcnQiOiA0MTA1MCwgImlkIjogIjVmOTA0Y2Q0LWVlOWYtNDc3Yy1mY2NlLWIyYmQyYjk3ZWZiMyIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMjIiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

