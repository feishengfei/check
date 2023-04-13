
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    
|    | id                   | addr          | cn          | cc   | isp           | ip                   | chatgpt          |
|---:|:---------------------|:--------------|:------------|:-----|:--------------|:---------------------|:-----------------|
|  0 | [5](config/5.json)   | cf.noaries.de | France      | FR   | Online S.a.s. | 2001:bc8:a00:3200::1 | Yes (Region: FR) |
|  1 | [17](config/17.json) | 156.225.67.58 | Netherlands | NL   | YISP B.V.     | 154.84.1.197         | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDUiLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6ICI4MDgwIiwgImlkIjogIjRmN2Q1ZDQzLTIyNmUtNDhkOC05ZGYwLTVlOGJmOWY3NzI4OCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZnQuY2xvdWRmbGFyZS5xdWVzdCIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny41OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE3IiwgInBvcnQiOiA1ODE4OCwgImlkIjogIjljMDI2ZWZlLTZhZjAtNDY1Zi1iOGMwLTNmNThjOGMyZDRjNSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogIiJ9
```

|    | id                           | addr                  |
|---:|:-----------------------------|:----------------------|
|  0 | [1](config_invalid/1.json)   | 103.160.204.13        |
|  1 | [2](config_invalid/2.json)   | f-us2.wvvvv.eu.org    |
|  2 | [3](config_invalid/3.json)   | 185.143.220.25        |
|  3 | [4](config_invalid/4.json)   | f-us1.wvvvv.eu.org    |
|  4 | [6](config_invalid/6.json)   | 172.64.173.160        |
|  5 | [7](config_invalid/7.json)   | v143a.toddns.tk       |
|  6 | [8](config_invalid/8.json)   | sg1.fightertunnel.xyz |
|  7 | [9](config_invalid/9.json)   | 203.24.108.8          |
|  8 | [10](config_invalid/10.json) | 23.227.38.102         |
|  9 | [11](config_invalid/11.json) | lsb-gy.heinu.cf       |
| 10 | [12](config_invalid/12.json) | ccdc2.6252369.xyz     |
| 11 | [13](config_invalid/13.json) | 185.162.228.229       |
| 12 | [14](config_invalid/14.json) | quiz.vidio.com        |
| 13 | [15](config_invalid/15.json) | 203.30.189.2          |
| 14 | [16](config_invalid/16.json) | 212.110.134.10        |
| 15 | [18](config_invalid/18.json) | lsb-gy.heinu.cf       |

## Invalid
```
vmess://eyJhZGQiOiAiMTAzLjE2MC4yMDQuMTMiLCAiYWlkIjogMCwgImhvc3QiOiAibGcyLnYycmF5Ni54eXoiLCAiaWQiOiAiNTZhMjE4OGItMmFiNy00MDJjLWI5YjgtMzQ4NDdmZGYwOTU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi81UU5ST1NSViIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDEiLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8ifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDIiLCAiYWRkIjogImYtdXMyLnd2dnZ2LmV1Lm9yZyIsICJwb3J0IjogIjIxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZGExZDM3Mi1lYzYwLTRiODktOGEzZi03OTE1OTQzOGM2ZjAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICJmLXVzMi53dnZ2di5ldS5vcmciLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTg1LjE0My4yMjAuMjUiLCAiYWlkIjogMCwgImhvc3QiOiAiZGVuZ3hpbi5vbmUiLCAiaWQiOiAiZjI4ZTM1NGUtYzJkMS00OTgzLTliMDctNWFjYWYxYjNiM2U1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi82ZTlFdFoyZEwiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZmM0XHU3ZjU3XHU2NWFmICAzIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDQiLCAiYWRkIjogImYtdXMxLnd2dnZ2LmV1Lm9yZyIsICJwb3J0IjogIjIxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZGExZDM3Mi1lYzYwLTRiODktOGEzZi03OTE1OTQzOGM2ZjAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICJmLXVzMS53dnZ2di5ldS5vcmciLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjY0LjE3My4xNjAiLCAiYWlkIjogMCwgImhvc3QiOiAiY2EuaWxvdmVzY3AuY29tIiwgImlkIjogIjJlNDk2NzU4LTk1MGUtNDU0OS04ODQyLWQ1ZWVjOThkOWZkZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvc2hpcmtlciIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgNiIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJhZGQiOiAidjE0M2EudG9kZG5zLnRrIiwgImFpZCI6IDAsICJob3N0IjogInYxNDNhLnRvZGRucy50ayIsICJpZCI6ICJhMjU4ODFmMy05NjdmLTMyNjUtYmM3Zi05ZTY2ODU3YjAxNmIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2pwMTQzLWQyeGRkeHhqIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA3IiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IGZhbHNlLCAic25pIjogInYxNDNhLnRvZGRucy50ayIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJhZGQiOiAic2cxLmZpZ2h0ZXJ0dW5uZWwueHl6IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI0YjU2ZGE2ZC1hNjJlLTQwZTAtODViNy1mYzdhN2NhMzFjNDYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3ZtZXNzIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWIwXHU1MmEwXHU1NzYxRGlnaXRhbE9jZWFuXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDgiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMjAzLjI0LjEwOC44IiwgImFpZCI6IDAsICJob3N0IjogImZyMS52MnJheTUueHl6IiwgImlkIjogIjJiMjE0MTIyLTE5MDYtNDI4YS1iYmI3LWEwMzljYmI3Y2Q1YyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NmZiM1x1NTkyN1x1NTIyOVx1NGU5YVx1NjA4OVx1NWMzYyA5IiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDEwIiwgImFkZCI6ICIyMy4yMjcuMzguMTAyIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJmci52MnJheTEueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAibHNiLWd5LmhlaW51LmNmIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImxzYi1neS5oZWludS5jZiIsICJpZCI6ICIxZWRhNmI5NS1mMjQ4LTRmM2ItYWUxMC1kNzUwMzQxNWE3ODgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0BoZWludWhvbWUiLCAicG9ydCI6ICIyMDk1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiY2NkYzIuNjI1MjM2OS54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiY2NkYzIuNjI1MjM2OS54eXoiLCAiaWQiOiAiZjg5NDlkZmUtYzUwMS00NTNjLTk2YjYtNjc4NmZiMDNkNWY5IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92eHQ5OSIsICJwb3J0IjogODQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMiIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDEzIiwgImFkZCI6ICIxODUuMTYyLjIyOC4yMjkiLCAicG9ydCI6IDgwLCAiaWQiOiAiNWY2NGZhNjUtN2IxNC00OWM1LTk1NGQtYWExNWM2YmZjYWNkIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJsZy52MnJheTgueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE0IiwgImFkZCI6ICJxdWl6LnZpZGlvLmNvbSIsICJwb3J0IjogIjQ0MyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAidGxzIiwgImlkIjogImU2NDQyOTAzLTQ3NTMtNDc4My04OTE2LWFjNDdjODA4MGU0ZiIsICJzbmkiOiAiIiwgImhvc3QiOiAiZHluYW1pYy1zZzNiLm9iZnMueHl6IiwgInBhdGgiOiAiLyJ9
vmess://eyJhZGQiOiAiMjAzLjMwLjE4OS4yIiwgImFpZCI6IDAsICJob3N0IjogImZyLnYycmF5MS54eXoiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFLb293ZWVydXAgU2Vjb25kYXJ5IENvbGxlZ2UgMTUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMjEyLjExMC4xMzQuMTAiLCAiYWlkIjogMCwgImhvc3QiOiAiMTU0LnYycmF5My54eXoiLCAiaWQiOiAiNDBkNDk2YTYtY2VlYi00MDk2LWJhZWItNGNjNTJiMjA1NjIxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9FQ1RDSjBERiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlNGNcdTUxNGJcdTUxNzAgIDE2IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAibHNiLWd5LmhlaW51LmNmIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNzkzYzAxMy1mNTk2LTRhZjktZGUwYS0yMDYyYmI4NjRkZDciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0BoZWludWhvbWUiLCAicG9ydCI6IDIwOTYsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

