
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    
|    | id                   | addr           | cn    | cc   | isp        | ip             | chatgpt          |
|---:|:---------------------|:---------------|:------|:-----|:-----------|:---------------|:-----------------|
|  0 | [10](config/10.json) | cf.noaries.de  |       |      |            | 107.189.28.253 | Yes (Region: LU) |
|  1 | [15](config/15.json) | 192.74.232.246 | China | CN   | PEGTECHINC | 198.2.200.100  | IP is BLOCKED    |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiODA4MCIsICJpZCI6ICI0ZjdkNWQ0My0yMjZlLTQ4ZDgtOWRmMC01ZThiZjlmNzcyODgiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImJ1eXZtLmNsb3VkZmxhcmUucXVlc3QiLCAicGF0aCI6ICIvYXJpZXM_ZWQ9MjA0OCIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTkyLjc0LjIzMi4yNDYiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICI0MTgwNDhhZi1hMjkzLTRiOTktOWIwYy05OGNhMzU4MGRkMjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTE4MDIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NTcyM1x1NGY1NVx1NTg1ZVBFRyBURUNIXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDE1IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
```

|    | id                           | addr               |
|---:|:-----------------------------|:-------------------|
|  0 | [1](config_invalid/1.json)   | 103.160.204.13     |
|  1 | [2](config_invalid/2.json)   | 203.24.108.100     |
|  2 | [3](config_invalid/3.json)   | 172.64.173.160     |
|  3 | [4](config_invalid/4.json)   | 185.162.228.1      |
|  4 | [5](config_invalid/5.json)   | 198.41.203.7       |
|  5 | [6](config_invalid/6.json)   | 162.159.255.200    |
|  6 | [7](config_invalid/7.json)   | 185.162.228.229    |
|  7 | [8](config_invalid/8.json)   | 203.30.188.2       |
|  8 | [11](config_invalid/11.json) | 185.162.228.2      |
|  9 | [12](config_invalid/12.json) | 203.30.189.1       |
| 10 | [13](config_invalid/13.json) | 5.78.96.204        |
| 11 | [14](config_invalid/14.json) | f-us2.wvvvv.eu.org |
| 12 | [16](config_invalid/16.json) | 144.24.72.125      |
| 13 | [17](config_invalid/17.json) | cf.515188.xyz      |
| 14 | [18](config_invalid/18.json) | 162.159.58.15      |
| 15 | [19](config_invalid/19.json) | 185.143.220.25     |

## Invalid
```
vmess://eyJhZGQiOiAiMTAzLjE2MC4yMDQuMTMiLCAiYWlkIjogMCwgImhvc3QiOiAibGcyLnYycmF5Ni54eXoiLCAiaWQiOiAiNTZhMjE4OGItMmFiNy00MDJjLWI5YjgtMzQ4NDdmZGYwOTU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi81UU5ST1NSViIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDEiLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8ifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2MgMiIsICJhZGQiOiAiMjAzLjI0LjEwOC4xMDAiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImxnLnYycmF5OC54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjY0LjE3My4xNjAiLCAiYWlkIjogMCwgImhvc3QiOiAiY2EuaWxvdmVzY3AuY29tIiwgImlkIjogIjJlNDk2NzU4LTk1MGUtNDU0OS04ODQyLWQ1ZWVjOThkOWZkZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvc2hpcmtlciIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMyIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDQiLCAiYWRkIjogIjE4NS4xNjIuMjI4LjEiLCAicG9ydCI6IDQ0MywgImlkIjogIjQwZDQ5NmE2LWNlZWItNDA5Ni1iYWViLTRjYzUyYjIwNTYyMSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAiMTU0LnYycmF5My54eXoiLCAicGF0aCI6ICIvRUNUQ0owREYiLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDUiLCAiYWRkIjogIjE5OC40MS4yMDMuNyIsICJwb3J0IjogIjgwIiwgImlkIjogIjVmNjRmYTY1LTdiMTQtNDljNS05NTRkLWFhMTVjNmJmY2FjZCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAibGcudjJyYXk4Lnh5eiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDYiLCAiYWRkIjogIjE2Mi4xNTkuMjU1LjIwMCIsICJwb3J0IjogIjgwIiwgImlkIjogIjUyNDY2ZGMyLTM1NTAtNDMxMC05MTBjLTc0YjdiZjhhMDIwZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAidXMtMS5hY3l1bi5ldS5vcmciLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDciLCAiYWRkIjogIjE4NS4xNjIuMjI4LjIyOSIsICJwb3J0IjogODAsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImxnLnYycmF5OC54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMjAzLjMwLjE4OC4yIiwgImFpZCI6IDAsICJob3N0IjogImZyLnYycmF5MS54eXoiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFMeW5kaHVyc3QgU2Vjb25kYXJ5IENvbGxlZ2UgOCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDExIiwgImFkZCI6ICIxODUuMTYyLjIyOC4yIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJmci52MnJheTEueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMjAzLjMwLjE4OS4xIiwgImFpZCI6IDAsICJob3N0IjogIjE1NC52MnJheTMueHl6IiwgImlkIjogIjQwZDQ5NmE2LWNlZWItNDA5Ni1iYWViLTRjYzUyYjIwNTYyMSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvRUNUQ0owREYiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2ZmIzXHU1OTI3XHU1MjI5XHU0ZTlhS29vd2VlcnVwIFNlY29uZGFyeSBDb2xsZWdlIDEyIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDEzIiwgImFkZCI6ICI1Ljc4Ljk2LjIwNCIsICJwb3J0IjogIjIxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZGExZDM3Mi1lYzYwLTRiODktOGEzZi03OTE1OTQzOGM2ZjAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDE0IiwgImFkZCI6ICJmLXVzMi53dnZ2di5ldS5vcmciLCAicG9ydCI6ICIyMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMGRhMWQzNzItZWM2MC00Yjg5LThhM2YtNzkxNTk0MzhjNmYwIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiZi11czIud3Z2dnYuZXUub3JnIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTQ0LjI0LjcyLjEyNSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMWMxZDk0ZGMtZTc5Yi00YTI0LWRjOWYtN2FmYTkyNTM5YTgwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDM5ODY3LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlMGNcdTgxNGEgIDE2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE3IiwgImFkZCI6ICJjZi41MTUxODgueHl6IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiZjZhYTQ0NDAtZTdiZS00NGUxLTgwZTEtN2U0NWNjZDc5NmNjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzc3JzdWIudjAxLnNzcnN1Yi5jb20iLCAicGF0aCI6ICIvYXBpL3YzL2Rvd25sb2FkLmdldEZpbGUiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTYyLjE1OS41OC4xNSIsICJhaWQiOiAwLCAiaG9zdCI6ICJsZzEudjJyYXk2Lnh5eiIsICJpZCI6ICJjNWEyZDdiOC1iZjg0LTRmOTctODU3Ny1iOWI4N2YyYmFhZjciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0FVSUtOOEFVIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTg1LjE0My4yMjAuMjUiLCAiYWlkIjogMCwgImhvc3QiOiAiZGVuZ3hpbi5vbmUiLCAiaWQiOiAiZjI4ZTM1NGUtYzJkMS00OTgzLTliMDctNWFjYWYxYjNiM2U1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi82ZTlFdFoyZEwiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZmM0XHU3ZjU3XHU2NWFmICAxOSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

## Todo
```
trojan://f0c54c4a-747e-4305-a76c-9a85cf095bc1@jp01.trojanyyds.xyz:443#github.com/freefq%20-%20%E9%A6%99%E6%B8%AFMicrosoft%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%209
```

