
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    
|    | id                   | addr          | cn          | cc   | isp              | ip            | chatgpt          |
|---:|:---------------------|:--------------|:------------|:-----|:-----------------|:--------------|:-----------------|
|  0 | [22](config/22.json) | 144.24.72.125 | South Korea | KR   | ORACLE-BMC-31898 | 144.24.72.125 | Yes (Region: KR) |

## Valid
```
vmess://eyJhZGQiOiAiMTQ0LjI0LjcyLjEyNSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlMGNcdTgxNGEgIDIyIiwgInBvcnQiOiAzOTg2NywgImlkIjogIjFjMWQ5NGRjLWU3OWItNGEyNC1kYzlmLTdhZmE5MjUzOWE4MCIsICJhaWQiOiAiMCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
```

|    | id                           | addr                   |
|---:|:-----------------------------|:-----------------------|
|  0 | [1](config_invalid/1.json)   | f-us2.wvvvv.eu.org     |
|  1 | [2](config_invalid/2.json)   | 23.224.9.93            |
|  2 | [3](config_invalid/3.json)   | f-us1.wvvvv.eu.org     |
|  3 | [4](config_invalid/4.json)   | 192.74.243.41          |
|  4 | [5](config_invalid/5.json)   | luxl.xyz               |
|  5 | [6](config_invalid/6.json)   | 203.30.190.1           |
|  6 | [7](config_invalid/7.json)   | 103.160.204.13         |
|  7 | [8](config_invalid/8.json)   | cf.noaries.de          |
|  8 | [9](config_invalid/9.json)   | 172.64.173.160         |
|  9 | [10](config_invalid/10.json) | 203.24.108.100         |
| 10 | [11](config_invalid/11.json) | lsb-gy.heinu.cf        |
| 11 | [12](config_invalid/12.json) | 185.162.228.229        |
| 12 | [13](config_invalid/13.json) | 185.162.228.2          |
| 13 | [14](config_invalid/14.json) | 203.30.188.2           |
| 14 | [15](config_invalid/15.json) | lsb-gy.heinu.cf        |
| 15 | [16](config_invalid/16.json) | 23.227.38.102          |
| 16 | [17](config_invalid/17.json) | quiz.vidio.com         |
| 17 | [18](config_invalid/18.json) | 162.159.255.200        |
| 18 | [19](config_invalid/19.json) | 103.160.204.12         |
| 19 | [20](config_invalid/20.json) | usv6warp.happyfree.top |
| 20 | [21](config_invalid/21.json) | 198.41.203.7           |

## Invalid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDEiLCAiYWRkIjogImYtdXMyLnd2dnZ2LmV1Lm9yZyIsICJwb3J0IjogIjIxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZGExZDM3Mi1lYzYwLTRiODktOGEzZi03OTE1OTQzOGM2ZjAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICJmLXVzMi53dnZ2di5ldS5vcmciLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZcdTVlMDJDb3BlcmF0aW9uIENvbG9jdGlvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyIiwgImFkZCI6ICIyMy4yMjQuOS45MyIsICJwb3J0IjogIjUxNTA0IiwgImlkIjogImJiMjU4NTllLWY2ZGEtNDEwMS05ODlmLWI0ZGQ2N2EyMjY4MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRmMGFcdTY3MTcgIDMiLCAiYWRkIjogImYtdXMxLnd2dnZ2LmV1Lm9yZyIsICJwb3J0IjogIjIxIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICIwZGExZDM3Mi1lYzYwLTRiODktOGEzZi03OTE1OTQzOGM2ZjAiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICJmLXVzMS53dnZ2di5ldS5vcmciLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgImFkZCI6ICIxOTIuNzQuMjQzLjQxIiwgInBvcnQiOiAiNDkyMDYiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDUiLCAiYWRkIjogImx1eGwueHl6IiwgInBvcnQiOiAiMTEwMTYiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjc0YTdmNGNhLTdkNjItNDNlNS05MDc0LTVmNzQ4MzEwZjAwYSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvMTEwMTYiLCAiaG9zdCI6ICJsdXhsLnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFMYW5nd2FycmluIFNlY29uZGFyeSBDb2xsZWdlIDYiLCAiYWRkIjogIjIwMy4zMC4xOTAuMSIsICJwb3J0IjogNDQzLCAiaWQiOiAiNDBkNDk2YTYtY2VlYi00MDk2LWJhZWItNGNjNTJiMjA1NjIxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICIxNTQudjJyYXkzLnh5eiIsICJwYXRoIjogIi9FQ1RDSjBERiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiMTAzLjE2MC4yMDQuMTMiLCAiYWlkIjogMCwgImhvc3QiOiAibGcyLnYycmF5Ni54eXoiLCAiaWQiOiAiNTZhMjE4OGItMmFiNy00MDJjLWI5YjgtMzQ4NDdmZGYwOTU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi81UU5ST1NSViIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDciLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8ifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6ICI4MDgwIiwgImlkIjogIjRmN2Q1ZDQzLTIyNmUtNDhkOC05ZGYwLTVlOGJmOWY3NzI4OCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiYnV5dm0uY2xvdWRmbGFyZS5xdWVzdCIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTcyLjY0LjE3My4xNjAiLCAiYWlkIjogMCwgImhvc3QiOiAiY2EuaWxvdmVzY3AuY29tIiwgImlkIjogIjJlNDk2NzU4LTk1MGUtNDU0OS04ODQyLWQ1ZWVjOThkOWZkZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvc2hpcmtlciIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgOSIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2MgMTAiLCAiYWRkIjogIjIwMy4yNC4xMDguMTAwIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiNWY2NGZhNjUtN2IxNC00OWM1LTk1NGQtYWExNWM2YmZjYWNkIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJsZy52MnJheTgueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAibHNiLWd5LmhlaW51LmNmIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImxzYi1neS5oZWludS5jZiIsICJpZCI6ICIxZWRhNmI5NS1mMjQ4LTRmM2ItYWUxMC1kNzUwMzQxNWE3ODgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0BoZWludWhvbWUiLCAicG9ydCI6ICIyMDk1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAxMSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDEyIiwgImFkZCI6ICIxODUuMTYyLjIyOC4yMjkiLCAicG9ydCI6IDgwLCAiaWQiOiAiNWY2NGZhNjUtN2IxNC00OWM1LTk1NGQtYWExNWM2YmZjYWNkIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJsZy52MnJheTgueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDEzIiwgImFkZCI6ICIxODUuMTYyLjIyOC4yIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJmci52MnJheTEueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMjAzLjMwLjE4OC4yIiwgImFpZCI6IDAsICJob3N0IjogImZyLnYycmF5MS54eXoiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFMeW5kaHVyc3QgU2Vjb25kYXJ5IENvbGxlZ2UgMTQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAibHNiLWd5LmhlaW51LmNmIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNzkzYzAxMy1mNTk2LTRhZjktZGUwYS0yMDYyYmI4NjRkZDciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0BoZWludWhvbWUiLCAicG9ydCI6IDIwOTYsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTUiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDE2IiwgImFkZCI6ICIyMy4yMjcuMzguMTAyIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJmci52MnJheTEueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE3IiwgImFkZCI6ICJxdWl6LnZpZGlvLmNvbSIsICJwb3J0IjogIjQ0MyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAidGxzIiwgImlkIjogImU2NDQyOTAzLTQ3NTMtNDc4My04OTE2LWFjNDdjODA4MGU0ZiIsICJzbmkiOiAiIiwgImhvc3QiOiAiZHluYW1pYy1zZzNiLm9iZnMueHl6IiwgInBhdGgiOiAiLyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE4IiwgImFkZCI6ICIxNjIuMTU5LjI1NS4yMDAiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1MjQ2NmRjMi0zNTUwLTQzMTAtOTEwYy03NGI3YmY4YTAyMGUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVzLTEuYWN5dW4uZXUub3JnIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDE5IiwgImFkZCI6ICIxMDMuMTYwLjIwNC4xMiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI0MGQ0OTZhNi1jZWViLTQwOTYtYmFlYi00Y2M1MmIyMDU2MjEiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIjE1NC52MnJheTMueHl6IiwgInBhdGgiOiAiL0VDVENKMERGIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAidXN2NndhcnAuaGFwcHlmcmVlLnRvcCIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZWRmMTQwZjEtMzVlOS00MTYwLWI1YTAtNmIyN2YzNDE5YTZmIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9maWd1cmUiLCAicG9ydCI6IDg0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMjAiLCAidGxzIjogInRscyIsICJ0eXBlIjogIm5vbmUiLCAic2VjdXJpdHkiOiAibm9uZSIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTk4LjQxLjIwMy43IiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImhvc3QiOiAibGcudjJyYXk4Lnh5eiIsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyMSIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICJub25lIiwgInYiOiAiMiJ9
```

