
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    
|    | id                   | addr            | cn            | cc   | isp        | ip              | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------|:----------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.21.241    | United States | US   | SHARKTECH  | 107.167.24.162  | IP is BLOCKED    |
|  1 | [3](config/3.json)   | 64.32.4.56      | United States | US   | SHARKTECH  | 107.167.13.162  | IP is BLOCKED    |
|  2 | [4](config/4.json)   | 107.148.194.228 | United States | US   | PEGTECHINC | 107.148.194.225 | IP is BLOCKED    |
|  3 | [5](config/5.json)   | 107.167.4.122   | United States | US   | SHARKTECH  | 107.167.18.58   | IP is BLOCKED    |
|  4 | [6](config/6.json)   | 156.225.67.58   | Netherlands   | NL   | YISP B.V.  | 154.84.1.197    | Yes (Region: NL) |
|  5 | [7](config/7.json)   | 156.225.67.88   | Netherlands   | NL   | YISP B.V.  | 154.84.1.129    | Yes (Region: NL) |
|  6 | [9](config/9.json)   | 156.225.67.145  | Netherlands   | NL   | YISP B.V.  | 154.84.1.178    | Yes (Region: NL) |
|  7 | [21](config/21.json) | cf.noaries.de   |               |      |            | 78.157.51.201   | IP is BLOCKED    |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuMjEuMjQxIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNTdmOTNlOTItZWJiOS00ZjE2LTliZGMtODIyNWQyMDEwOTk1IiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ0MzEzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiNjQuMzIuNC41NiIsICJwb3J0IjogIjQyMTc1IiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJob3N0IjogImxnMS52MnJheTYueHl6IiwgInBhdGgiOiAiL0FVSUtOOEFVIiwgInRscyI6ICIiLCAic25pIjogIiIsICJ0eXBlIjogIm5vbmUiLCAic2VydmVyUG9ydCI6IDAsICJuYXRpb24iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZQZXRhRXhwcmVzcyA0IiwgImFkZCI6ICIxMDcuMTQ4LjE5NC4yMjgiLCAicG9ydCI6ICI1NDkwNCIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiL3NoaXJrZXIiLCAiaG9zdCI6ICJ1azEuc2Nwcm94eS50b3AiLCAidGxzIjogIiJ9
vmess://eyJhZGQiOiAiMTA3LjE2Ny40LjEyMiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjk4MzhjMWI0LWMzZmQtNDliNS04YTU5LTJmZjA1Mzg1ZjE3YyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Njc2NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny41OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDYiLCAicG9ydCI6IDU4MTg4LCAiaWQiOiAiOWMwMjZlZmUtNmFmMC00NjVmLWI4YzAtM2Y1OGM4YzJkNGM1IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny44OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDciLCAicG9ydCI6IDUyMjkyLCAiaWQiOiAiMjBiMzA5MTYtZTIwMy00MTJlLThlYzAtOTAwZjNhY2Q1MTI4IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNDUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA5IiwgInBvcnQiOiA1MTk0OCwgImlkIjogIjkzNTAzZGQ1LTI0NWEtNGViMS1hZTJhLTU3YWI5ZjJiM2MyOSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIjE4LjE0My4xMjMuMzUiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiY2Yubm9hcmllcy5kZSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIxIiwgInBvcnQiOiAyMDgyLCAiaWQiOiAiMzE0YzEzODctNjE4Yy00Njg5LTk3ZmMtNGJjOWExYWU1ZTA1IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogImlyMi5ubXNsLm5pbmphIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
```

|    | id                           | addr                   |
|---:|:-----------------------------|:-----------------------|
|  0 | [1](config_invalid/1.json)   | n1680937004.sxhucjg.cn |
|  1 | [10](config_invalid/10.json) | 172.64.173.160         |
|  2 | [11](config_invalid/11.json) | www.nivod4.tv          |
|  3 | [12](config_invalid/12.json) | 212.110.134.10         |
|  4 | [13](config_invalid/13.json) | lsb-gy.heinu.cf        |
|  5 | [14](config_invalid/14.json) | lsb-gy.heinu.cf        |
|  6 | [15](config_invalid/15.json) | v143a.toddns.tk        |
|  7 | [16](config_invalid/16.json) | 23.227.38.39           |
|  8 | [17](config_invalid/17.json) | quiz.vidio.com         |
|  9 | [18](config_invalid/18.json) | 1024.day               |
| 10 | [19](config_invalid/19.json) | ccdc2.6252369.xyz      |
| 11 | [20](config_invalid/20.json) | 185.143.220.25         |
| 12 | [22](config_invalid/22.json) | 185.162.228.229        |
| 13 | [23](config_invalid/23.json) | f-us2.wvvvv.eu.org     |
| 14 | [24](config_invalid/24.json) | sg1.fightertunnel.xyz  |
| 15 | [25](config_invalid/25.json) | r2wind.com             |

## Invalid
```
vmess://eyJhZGQiOiAibjE2ODA5MzcwMDQuc3hodWNqZy5jbiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiZGYyY2ZhMzktM2RkMy00MTFhLTk4NzItOGU1MDhmNWUyNDgzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU5OTk5XHU2ZTJmXHU5NjNmXHU5MWNjXHU0ZTkxIDEiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICJuMTY4MDkzNzAwNC5zeGh1Y2pnLmNuIn0=
vmess://eyJhZGQiOiAiMTcyLjY0LjE3My4xNjAiLCAiYWlkIjogMCwgImhvc3QiOiAiY2EuaWxvdmVzY3AuY29tIiwgImlkIjogIjJlNDk2NzU4LTk1MGUtNDU0OS04ODQyLWQ1ZWVjOThkOWZkZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvc2hpcmtlciIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTAiLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8ifQ==
vmess://eyJhZGQiOiAid3d3Lm5pdm9kNC50diIsICJ2IjogMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI1NmEyMTg4Yi0yYWI3LTQwMmMtYjliOC0zNDg0N2ZkZjA5NTgiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAibGcyLnYycmF5Ni54eXoiLCAidGxzIjogInRscyIsICJwYXRoIjogIi81UU5ST1NSViJ9
vmess://eyJhZGQiOiAiMjEyLjExMC4xMzQuMTAiLCAiYWlkIjogMCwgImhvc3QiOiAiMTU0LnYycmF5My54eXoiLCAiaWQiOiAiNDBkNDk2YTYtY2VlYi00MDk2LWJhZWItNGNjNTJiMjA1NjIxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9FQ1RDSjBERiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlNGNcdTUxNGJcdTUxNzAgIDEyIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAibHNiLWd5LmhlaW51LmNmIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImxzYi1neS5oZWludS5jZiIsICJpZCI6ICIxZWRhNmI5NS1mMjQ4LTRmM2ItYWUxMC1kNzUwMzQxNWE3ODgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0BoZWludWhvbWUiLCAicG9ydCI6ICIyMDk1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAibHNiLWd5LmhlaW51LmNmIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNzkzYzAxMy1mNTk2LTRhZjktZGUwYS0yMDYyYmI4NjRkZDciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0BoZWludWhvbWUiLCAicG9ydCI6IDIwOTYsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTQiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAidjE0M2EudG9kZG5zLnRrIiwgImFpZCI6IDAsICJob3N0IjogInYxNDNhLnRvZGRucy50ayIsICJpZCI6ICJhMjU4ODFmMy05NjdmLTMyNjUtYmM3Zi05ZTY2ODU3YjAxNmIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2pwMTQzLWQyeGRkeHhqIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxNSIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiBmYWxzZSwgInNuaSI6ICJ2MTQzYS50b2RkbnMudGsiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8ifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDE2IiwgImFkZCI6ICIyMy4yMjcuMzguMzkiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImxnLnYycmF5OC54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE3IiwgImFkZCI6ICJxdWl6LnZpZGlvLmNvbSIsICJwb3J0IjogIjQ0MyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAidGxzIiwgImlkIjogImU2NDQyOTAzLTQ3NTMtNDc4My04OTE2LWFjNDdjODA4MGU0ZiIsICJzbmkiOiAiIiwgImhvc3QiOiAiZHluYW1pYy1zZzNiLm9iZnMueHl6IiwgInBhdGgiOiAiLyJ9
vmess://eyJhZGQiOiAiMTAyNC5kYXkiLCAiYWlkIjogMCwgImhvc3QiOiAibGcxLnYycmF5Ni54eXoiLCAiaWQiOiAiYzVhMmQ3YjgtYmY4NC00Zjk3LTg1NzctYjliODdmMmJhYWY3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9BVUlLTjhBVSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2NkYzIuNjI1MjM2OS54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiY2NkYzIuNjI1MjM2OS54eXoiLCAiaWQiOiAiZjg5NDlkZmUtYzUwMS00NTNjLTk2YjYtNjc4NmZiMDNkNWY5IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92eHQ5OSIsICJwb3J0IjogODQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxOSIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJhZGQiOiAiMTg1LjE0My4yMjAuMjUiLCAiYWlkIjogMCwgImhvc3QiOiAiZGVuZ3hpbi5vbmUiLCAiaWQiOiAiZjI4ZTM1NGUtYzJkMS00OTgzLTliMDctNWFjYWYxYjNiM2U1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi82ZTlFdFoyZEwiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZmM0XHU3ZjU3XHU2NWFmICAyMCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlMzlcdTllYTYgIDIyIiwgImFkZCI6ICIxODUuMTYyLjIyOC4yMjkiLCAicG9ydCI6IDgwLCAiaWQiOiAiNWY2NGZhNjUtN2IxNC00OWM1LTk1NGQtYWExNWM2YmZjYWNkIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJsZy52MnJheTgueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDIzIiwgImFkZCI6ICJmLXVzMi53dnZ2di5ldS5vcmciLCAicG9ydCI6ICIyMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiMGRhMWQzNzItZWM2MC00Yjg5LThhM2YtNzkxNTk0MzhjNmYwIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiZi11czIud3Z2dnYuZXUub3JnIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAic2cxLmZpZ2h0ZXJ0dW5uZWwueHl6IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI0YjU2ZGE2ZC1hNjJlLTQwZTAtODViNy1mYzdhN2NhMzFjNDYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3ZtZXNzIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWIwXHU1MmEwXHU1NzYxRGlnaXRhbE9jZWFuXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDI0IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAicjJ3aW5kLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJzc3JzdWIudjAxLnNzcnN1Yi5jb20iLCAiaWQiOiAiZjZhYTQ0NDAtZTdiZS00NGUxLTgwZTEtN2U0NWNjZDc5NmNjIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkvdjMvZG93bmxvYWQuZ2V0RmlsZSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMjUiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

## Todo
```
trojan://6e3d2643-6283-4962-82b5-2fca9753e4cb@as.steamdownload.top:36643#github.com/freefq%20-%20%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%B9%BF%E5%B7%9E%E5%B8%82%E7%A7%BB%E5%8A%A8%208
```

