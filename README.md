
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    
|    | id                   | addr           | cn            | cc   | isp           | ip                     | chatgpt          |
|---:|:---------------------|:---------------|:--------------|:-----|:--------------|:-----------------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.4.56     | United States | US   | SHARKTECH     | 107.167.13.162         | IP is BLOCKED    |
|  1 | [3](config/3.json)   | 156.225.67.88  | Netherlands   | NL   | YISP B.V.     | 154.84.1.129           | Yes (Region: NL) |
|  2 | [4](config/4.json)   | 156.225.67.145 | Netherlands   | NL   | YISP B.V.     | 154.84.1.178           | Yes (Region: NL) |
|  3 | [5](config/5.json)   | 156.225.67.58  | Netherlands   | NL   | YISP B.V.     | 154.84.1.197           | Yes (Region: NL) |
|  4 | [11](config/11.json) | cf.noaries.de  |               |      |               | 78.157.51.201          | IP is BLOCKED    |
|  5 | [12](config/12.json) | cf.noaries.de  | Netherlands   | NL   | CLOUDFLARENET | 2a09:bac1:5520::20a:59 | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuNC41NiIsICJwb3J0IjogIjQyMTc1IiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJob3N0IjogImxnMS52MnJheTYueHl6IiwgInBhdGgiOiAiL0FVSUtOOEFVIiwgInRscyI6ICIiLCAic25pIjogIiIsICJ0eXBlIjogIm5vbmUiLCAic2VydmVyUG9ydCI6IDAsICJuYXRpb24iOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny44OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAicG9ydCI6IDUyMjkyLCAiaWQiOiAiMjBiMzA5MTYtZTIwMy00MTJlLThlYzAtOTAwZjNhY2Q1MTI4IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny4xNDUiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU1MzU3XHU5NzVlICA0IiwgInBvcnQiOiA1MTk0OCwgImlkIjogIjkzNTAzZGQ1LTI0NWEtNGViMS1hZTJhLTU3YWI5ZjJiM2MyOSIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJ0eXBlIjogIiIsICJob3N0IjogIjE4LjE0My4xMjMuMzUiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjIyNS42Ny41OCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAicG9ydCI6IDU4MTg4LCAiaWQiOiAiOWMwMjZlZmUtNmFmMC00NjVmLWI4YzAtM2Y1OGM4YzJkNGM1IiwgImFpZCI6ICI2NCIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiY2Yubm9hcmllcy5kZSIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDExIiwgInBvcnQiOiAyMDgyLCAiaWQiOiAiMzE0YzEzODctNjE4Yy00Njg5LTk3ZmMtNGJjOWExYWU1ZTA1IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIiIsICJob3N0IjogImlyMi5ubXNsLm5pbmphIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiY2Yubm9hcmllcy5kZSIsICJhaWQiOiAwLCAiaG9zdCI6ICJzY3ctbmwuY2xvdWRmbGFyZS5xdWVzdCIsICJpZCI6ICI0ZjdkNWQ0My0yMjZlLTQ4ZDgtOWRmMC01ZThiZjlmNzcyODgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2FyaWVzP2VkPTIwNDgiLCAicG9ydCI6IDIwNTIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMTIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

|    | id                           | addr              |
|---:|:-----------------------------|:------------------|
|  0 | [1](config_invalid/1.json)   | 107.167.4.122     |
|  1 | [6](config_invalid/6.json)   | 185.143.220.25    |
|  2 | [7](config_invalid/7.json)   | 172.64.173.160    |
|  3 | [8](config_invalid/8.json)   | 203.30.188.1      |
|  4 | [9](config_invalid/9.json)   | www.nivod4.tv     |
|  5 | [10](config_invalid/10.json) | 103.160.204.12    |
|  6 | [13](config_invalid/13.json) | quiz.vidio.com    |
|  7 | [14](config_invalid/14.json) | 212.110.134.10    |
|  8 | [15](config_invalid/15.json) | ccdc2.6252369.xyz |
|  9 | [16](config_invalid/16.json) | v143a.toddns.tk   |
| 10 | [17](config_invalid/17.json) | 23.227.38.39      |
| 11 | [18](config_invalid/18.json) | 158.101.7.8       |
| 12 | [19](config_invalid/19.json) | 1024.day          |
| 13 | [20](config_invalid/20.json) | 103.160.204.14    |
| 14 | [21](config_invalid/21.json) | 172.64.195.14     |
| 15 | [22](config_invalid/22.json) | lsb-gy.heinu.cf   |
| 16 | [23](config_invalid/23.json) | r2wind.com        |

## Invalid
```
vmess://eyJhZGQiOiAiMTA3LjE2Ny40LjEyMiIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjk4MzhjMWI0LWMzZmQtNDliNS04YTU5LTJmZjA1Mzg1ZjE3YyIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0Njc2NiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2XHU1ZTAyU2hhcmtUZWNoXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTg1LjE0My4yMjAuMjUiLCAiYWlkIjogMCwgImhvc3QiOiAiZGVuZ3hpbi5vbmUiLCAiaWQiOiAiZjI4ZTM1NGUtYzJkMS00OTgzLTliMDctNWFjYWYxYjNiM2U1IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi82ZTlFdFoyZEwiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU0ZmM0XHU3ZjU3XHU2NWFmICA2IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiMTcyLjY0LjE3My4xNjAiLCAiYWlkIjogMCwgImhvc3QiOiAiY2EuaWxvdmVzY3AuY29tIiwgImlkIjogIjJlNDk2NzU4LTk1MGUtNDU0OS04ODQyLWQ1ZWVjOThkOWZkZSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvc2hpcmtlciIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgNyIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJhZGQiOiAiMjAzLjMwLjE4OC4xIiwgImFpZCI6IDAsICJob3N0IjogIjE1NC52MnJheTMueHl6IiwgImlkIjogIjQwZDQ5NmE2LWNlZWItNDA5Ni1iYWViLTRjYzUyYjIwNTYyMSIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvRUNUQ0owREYiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2ZmIzXHU1OTI3XHU1MjI5XHU0ZTlhTHluZGh1cnN0IFNlY29uZGFyeSBDb2xsZWdlIDgiLCAidGxzIjogInRscyIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAid3d3Lm5pdm9kNC50diIsICJ2IjogMiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA5IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjU2YTIxODhiLTJhYjctNDAyYy1iOWI4LTM0ODQ3ZmRmMDk1OCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJsZzIudjJyYXk2Lnh5eiIsICJ0bHMiOiAidGxzIiwgInBhdGgiOiAiLzVRTlJPU1JWIn0=
vmess://eyJhZGQiOiAiMTAzLjE2MC4yMDQuMTIiLCAiYWlkIjogMCwgImhvc3QiOiAiMTU0LnYycmF5My54eXoiLCAiaWQiOiAiNDBkNDk2YTYtY2VlYi00MDk2LWJhZWItNGNjNTJiMjA1NjIxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9FQ1RDSjBERiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDEwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEzIiwgImFkZCI6ICJxdWl6LnZpZGlvLmNvbSIsICJwb3J0IjogIjQ0MyIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJ0bHMiOiAidGxzIiwgImlkIjogImU2NDQyOTAzLTQ3NTMtNDc4My04OTE2LWFjNDdjODA4MGU0ZiIsICJzbmkiOiAiIiwgImhvc3QiOiAiZHluYW1pYy1zZzNiLm9iZnMueHl6IiwgInBhdGgiOiAiLyJ9
vmess://eyJhZGQiOiAiMjEyLjExMC4xMzQuMTAiLCAiYWlkIjogMCwgImhvc3QiOiAiMTU0LnYycmF5My54eXoiLCAiaWQiOiAiNDBkNDk2YTYtY2VlYi00MDk2LWJhZWItNGNjNTJiMjA1NjIxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9FQ1RDSjBERiIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlNGNcdTUxNGJcdTUxNzAgIDE0IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2NkYzIuNjI1MjM2OS54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiY2NkYzIuNjI1MjM2OS54eXoiLCAiaWQiOiAiZjg5NDlkZmUtYzUwMS00NTNjLTk2YjYtNjc4NmZiMDNkNWY5IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92eHQ5OSIsICJwb3J0IjogODQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxNSIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byJ9
vmess://eyJhZGQiOiAidjE0M2EudG9kZG5zLnRrIiwgImFpZCI6IDAsICJob3N0IjogInYxNDNhLnRvZGRucy50ayIsICJpZCI6ICJhMjU4ODFmMy05NjdmLTMyNjUtYmM3Zi05ZTY2ODU3YjAxNmIiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2pwMTQzLWQyeGRkeHhqIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxNiIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiBmYWxzZSwgInNuaSI6ICJ2MTQzYS50b2RkbnMudGsiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8ifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDE3IiwgImFkZCI6ICIyMy4yMjcuMzguMzkiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1ZjY0ZmE2NS03YjE0LTQ5YzUtOTU0ZC1hYTE1YzZiZmNhY2QiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImxnLnYycmF5OC54eXoiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTRlOWFcdTUyMjlcdTY4NTFcdTkwYTNcdTVkZGVcdTUxZTRcdTUxZjBcdTU3Y2VPcmFjbGVcdTRlOTFcdThiYTFcdTdiOTdcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTgiLCAiYWRkIjogIjE1OC4xMDEuNy44IiwgInBvcnQiOiAiODAiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjk1YjQ1YzQ5LWY1YzAtNDk1OS1iYjY0LTJiOGZiYzRhODY5YyIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTAyNC5kYXkiLCAiYWlkIjogMCwgImhvc3QiOiAibGcxLnYycmF5Ni54eXoiLCAiaWQiOiAiYzVhMmQ3YjgtYmY4NC00Zjk3LTg1NzctYjliODdmMmJhYWY3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9BVUlLTjhBVSIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE5IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTRlOWFcdTU5MmFcdTU3MzBcdTUzM2EgIDIwIiwgImFkZCI6ICIxMDMuMTYwLjIwNC4xNCIsICJwb3J0IjogIjgwIiwgImlkIjogIjE3YjJhMzEzLTM3YTAtNDk0NS1hOGU0LWU2MzM3NTUwNmI0YSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZnIudjJyYXkxLnh5eiIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIxIiwgImFkZCI6ICIxNzIuNjQuMTk1LjE0IiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMTdiMmEzMTMtMzdhMC00OTQ1LWE4ZTQtZTYzMzc1NTA2YjRhIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJmci52MnJheTEueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAibHNiLWd5LmhlaW51LmNmIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImxzYi1neS5oZWludS5jZiIsICJpZCI6ICIxZWRhNmI5NS1mMjQ4LTRmM2ItYWUxMC1kNzUwMzQxNWE3ODgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL0BoZWludWhvbWUiLCAicG9ydCI6ICIyMDk1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyMiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiIiwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAicjJ3aW5kLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICJzc3JzdWIudjAxLnNzcnN1Yi5jb20iLCAiaWQiOiAiZjZhYTQ0NDAtZTdiZS00NGUxLTgwZTEtN2U0NWNjZDc5NmNjIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9hcGkvdjMvZG93bmxvYWQuZ2V0RmlsZSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMjMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

