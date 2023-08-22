
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn          | cc   | isp                    | ip              | chatgpt          |
|---:|:---------------------|:---------------------|:------------|:-----|:-----------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 156.225.67.78        | Netherlands | NL   | YISP B.V.              | 46.182.107.216  | Yes (Region: US) |
|  1 | [7](config/7.json)   | a26.2e5bf271.win     | South Korea | KR   | AMAZON-02              | 3.37.128.198    | Yes (Region: KR) |
|  2 | [8](config/8.json)   | speedip.eu.org       | Poland      | PL   | OVH SAS                | 54.36.174.181   | Yes (Region: FR) |
|  3 | [10](config/10.json) | 156.225.67.243       | Netherlands | NL   | YISP B.V.              | 154.84.1.37     | Yes (Region: NL) |
|  4 | [11](config/11.json) | cfcdn3.sanfencdn.net | Singapore   | SG   | Akamai Connected Cloud | 172.104.161.252 | Yes (Region: US) |
|  5 | [14](config/14.json) | 157.230.47.44        | Singapore   | SG   | GOOGLE-CLOUD-PLATFORM  | 35.240.146.255  | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuNzgiLCAicG9ydCI6ICI0MjIzOSIsICJpZCI6ICIzZTAxNmM0ZC05ODZlLTQyZGYtODM4Yy02MDQ2ZjNkODllY2YiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRBbWF6b24gRUMyXHU2NzBkXHU1MmExXHU1NjY4IDciLCAiYWRkIjogImEyNi4yZTViZjI3MS53aW4iLCAicG9ydCI6ICI4MCIsICJpZCI6ICIyMTcwMDBiNy1iM2JmLTRlMGUtOWQyYy0xZWMyYmExYmU2ODciLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImEyNi4yZTViZjI3MS53aW4iLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogInNwZWVkaXAuZXUub3JnIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiNzJlODAzMGEtOTZjMi00YmRiLWFjZmItNWJjMDIyNDhmOWYwIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzc3JzdWIudjA0LnNzcnN1Yi5jb20iLCAicGF0aCI6ICIvYXBpL3YzL2Rvd25sb2FkLmdldEZpbGUiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEwIiwgImFkZCI6ICIxNTYuMjI1LjY3LjI0MyIsICJwb3J0IjogIjQzNTgyIiwgImlkIjogIjk5MDAwNmJkLWNiMjAtNDgyZi05Yzk3LWY1ZmM2NTM1OTYwNSIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDExIiwgImFkZCI6ICJjZmNkbjMuc2FuZmVuY2RuLm5ldCIsICJwb3J0IjogIjIwNTIiLCAiaWQiOiAiMTY1ODI3NTktM2QyMC00ODA0LTljOWMtYTU4YWQ3YjI2MGE4IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJzZzMuc2FuZmVuY2RuMi5jb20iLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTY1YjBcdTUyYTBcdTU3NjFEaWdpdGFsT2NlYW5cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTQiLCAiYWRkIjogIjE1Ny4yMzAuNDcuNDQiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiYWViZmM1YWUtZmZlYi00OGVlLWIzMTktZjMxOGI2Y2U5MmQ4IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ4anBwLm1sYmxkenoudG9wIiwgInBhdGgiOiAiL2FlYmZjNWFlLWZmZWItNDhlZS1iMzE5LWYzMThiNmNlOTJkOCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiNi53eWhrYWEwLmdxIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgMzgiLCAicG9ydCI6IDIwOTUsICJpZCI6ICI2YmJjOTU1NC0wN2JjLTQ3YzYtYTA4OC04N2FhNzlmZDVjYTEiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiNi53eWhrYWEwLmdxIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJ0bHMiOiAiIn0=
```

