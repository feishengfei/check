
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    
|    | id                   | addr           | ip            | chatgpt          | netflix        | tiktok           |
|---:|:---------------------|:---------------|:--------------|:-----------------|:---------------|:-----------------|
|  0 | [5](config/5.json)   | 156.249.18.232 | 154.84.1.231  | Yes (Region: NL) | Originals Only | Yes (Region: NL) |
|  1 | [11](config/11.json) | 203.24.108.2   | 172.99.188.99 | Yes (Region: NL) | Originals Only | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4yMzIiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJmNTI1MGM0ZS1mODU1LTRlZmYtYjczYy1hMDIyMjZkNDJmZTciLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6IDQyNTQyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMjAzLjI0LjEwOC4yIiwgImFpZCI6IDAsICJob3N0IjogImZyLnYycmF5MS54eXoiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2MgMTEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

|    | id                           | addr                    |
|---:|:-----------------------------|:------------------------|
|  0 | [1](config_invalid/1.json)   | tw2.sanfen001.pics      |
|  1 | [2](config_invalid/2.json)   | 185.162.228.229         |
|  2 | [3](config_invalid/3.json)   | 212.110.134.10          |
|  3 | [4](config_invalid/4.json)   | 103.160.204.13          |
|  4 | [6](config_invalid/6.json)   | 185.162.228.1           |
|  5 | [7](config_invalid/7.json)   | zhuyong.hucloud-dns.xyz |
|  6 | [8](config_invalid/8.json)   | cf.noaries.de           |
|  7 | [9](config_invalid/9.json)   | 162.159.58.15           |
|  8 | [10](config_invalid/10.json) | 198.41.203.7            |
|  9 | [12](config_invalid/12.json) | 162.159.255.200         |
| 10 | [13](config_invalid/13.json) | v140.toddns.tk          |
| 11 | [14](config_invalid/14.json) | 188.114.99.2            |
| 12 | [15](config_invalid/15.json) | www.udemy.com           |
| 13 | [16](config_invalid/16.json) | cf.515188.xyz           |
| 14 | [17](config_invalid/17.json) | 203.24.108.100          |
| 15 | [18](config_invalid/18.json) | 188.114.96.1            |
| 16 | [19](config_invalid/19.json) | 103.160.204.15          |
| 17 | [20](config_invalid/20.json) | new6.huvicloud.com      |
| 18 | [21](config_invalid/21.json) | 192.203.230.101         |
| 19 | [22](config_invalid/22.json) | cdn.moonfree.top        |
| 20 | [23](config_invalid/23.json) | dj02.yumili.cf          |

## Invalid
```
vmess://eyJhZGQiOiAidHcyLnNhbmZlbjAwMS5waWNzIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NTNmMFx1NTMxN1x1NWUwMlx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSAxIiwgInBvcnQiOiA0NDMsICJpZCI6ICJkYTlkNWM3NC1hNTcyLTRjZjQtYTM3NS0xOWI4ODZmNWZmYzQiLCAiYWlkIjogIjAiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIiIsICJwYXRoIjogIi8iLCAidGxzIjogInRscyJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDIiLCAiYWRkIjogIjE4NS4xNjIuMjI4LjIyOSIsICJwb3J0IjogIjgwIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImxnLnYycmF5OC54eXoiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlNGNcdTUxNGJcdTUxNzAgIDMiLCAiYWRkIjogIjIxMi4xMTAuMTM0LjEwIiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjQwZDQ5NmE2LWNlZWItNDA5Ni1iYWViLTRjYzUyYjIwNTYyMSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiMTU0LnYycmF5My54eXoiLCAicGF0aCI6ICIvRUNUQ0owREYiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiMTAzLjE2MC4yMDQuMTMiLCAiYWlkIjogMCwgImhvc3QiOiAibGcyLnYycmF5Ni54eXoiLCAiaWQiOiAiNTZhMjE4OGItMmFiNy00MDJjLWI5YjgtMzQ4NDdmZGYwOTU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi81UU5ST1NSViIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDQiLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8ifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDYiLCAiYWRkIjogIjE4NS4xNjIuMjI4LjEiLCAicG9ydCI6IDQ0MywgImlkIjogIjQwZDQ5NmE2LWNlZWItNDA5Ni1iYWViLTRjYzUyYjIwNTYyMSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAiMTU0LnYycmF5My54eXoiLCAicGF0aCI6ICIvRUNUQ0owREYiLCAidGxzIjogInRscyJ9
vmess://eyJhZGQiOiAiemh1eW9uZy5odWNsb3VkLWRucy54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjlhMThjYmIxLTgxZDItNDcyMC05ZjA5LTQ2ZWEyNzZiNmRkYiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvaHVodWJsb2ciLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA3IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6ICI4MDgwIiwgImlkIjogIjRmN2Q1ZDQzLTIyNmUtNDhkOC05ZGYwLTVlOGJmOWY3NzI4OCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiYnV5dm0uY2xvdWRmbGFyZS5xdWVzdCIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiMTYyLjE1OS41OC4xNSIsICJhaWQiOiAwLCAiaG9zdCI6ICJsZzEudjJyYXk2Lnh5eiIsICJpZCI6ICJjNWEyZDdiOC1iZjg0LTRmOTctODU3Ny1iOWI4N2YyYmFhZjciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0FVSUtOOEFVIiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgOSIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICIxOTguNDEuMjAzLjciLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImxnLnYycmF5OC54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICIxNjIuMTU5LjI1NS4yMDAiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1MjQ2NmRjMi0zNTUwLTQzMTAtOTEwYy03NGI3YmY4YTAyMGUiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVzLTEuYWN5dW4uZXUub3JnIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAidjE0MC50b2RkbnMudGsiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogImEyNTg4MWYzLTk2N2YtMzI2NS1iYzdmLTllNjY4NTdiMDE2YiIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvZnItODg4Z2lrZGx4IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTMiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTg4LjExNC45OS4yIiwgImFpZCI6IDAsICJob3N0IjogImZyLnYycmF5MS54eXoiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDgwLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVkZjRcdTg5N2ZcdTU3MjNcdTRmZGRcdTdmNTdDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE1IiwgImFkZCI6ICJ3d3cudWRlbXkuY29tIiwgInBvcnQiOiAiNDQzIiwgImlkIjogImU2NDQyOTAzLTQ3NTMtNDc4My04OTE2LWFjNDdjODA4MGU0ZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZHluYW1pYy1zZzNiLm9iZnMueHl6IiwgInBhdGgiOiAiL3dvcnJ5ZnJlZSIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICJjZi41MTUxODgueHl6IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiZjZhYTQ0NDAtZTdiZS00NGUxLTgwZTEtN2U0NWNjZDc5NmNjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzc3JzdWIudjAxLnNzcnN1Yi5jb20iLCAicGF0aCI6ICIvYXBpL3YzL2Rvd25sb2FkLmdldEZpbGUiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFcdTYwODlcdTVjM2MgMTciLCAiYWRkIjogIjIwMy4yNC4xMDguMTAwIiwgInBvcnQiOiAiODAiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjVmNjRmYTY1LTdiMTQtNDljNS05NTRkLWFhMTVjNmJmY2FjZCIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAibGcudjJyYXk4Lnh5eiIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTg4LjExNC45Ni4xIiwgInYiOiAyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVkZjRcdTg5N2ZcdTU3MjNcdTRmZGRcdTdmNTdDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE4IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjJlNDk2NzU4LTk1MGUtNDU0OS04ODQyLWQ1ZWVjOThkOWZkZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJsdjIuc2hhcmVjZW50cmVwcm8ub3JnIiwgInRscyI6ICJ0bHMiLCAicGF0aCI6ICIvc2hpcmtlciJ9
vmess://eyJhZGQiOiAiMTAzLjE2MC4yMDQuMTUiLCAiYWlkIjogMCwgImhvc3QiOiAibGcxLnYycmF5Ni54eXoiLCAiaWQiOiAiYzVhMmQ3YjgtYmY4NC00Zjk3LTg1NzctYjliODdmMmJhYWY3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9BVUlLTjhBVSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDE5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAibmV3Ni5odXZpY2xvdWQuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImhvc3QiOiAibmV3Ni5odXZpY2xvdWQuY29tIiwgImlkIjogImExMWNhNzYwLTllZjktNGE2My05NWM5LTRjNWMzMmQ1NjI1MSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiNDQzIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyMCIsICJzY3kiOiAibm9uZSIsICJzbmkiOiAibmV3Ni5odXZpY2xvdWQuY29tIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAiMTkyLjIwMy4yMzAuMTAxIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZCAgMjEiLCAicG9ydCI6IDQ0MywgImlkIjogImZjY2E0ZDA2LTNkMWEtNGQxMS1iMmJiLWQ4Yjg3ZDBhYTkxYyIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJoazAxLmtlbGVjbG91ZC54eXoiLCAicGF0aCI6ICIvcXdlcnR5IiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIyIiwgImFkZCI6ICJjZG4ubW9vbmZyZWUudG9wIiwgInBvcnQiOiAiODQ0MyIsICJpZCI6ICJlZGYxNDBmMS0zNWU5LTQxNjAtYjVhMC02YjI3ZjM0MTlhNmYiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVzdjZ3YXJwLmhhcHB5ZnJlZS50b3AiLCAicGF0aCI6ICIvZmlndXJlIiwgInRscyI6ICJ0bHMiLCAic25pIjogInVzdjZ3YXJwLmhhcHB5ZnJlZS50b3AiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiZGowMi55dW1pbGkuY2YiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogImM1Y2Q0NjczLTc4ZGUtNDNjZC1iNDYxLWRkMjQ1YzUxZjdiMSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvYWFhYSIsICJwb3J0IjogMjA5NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAyMyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

