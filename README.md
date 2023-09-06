
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                       | cn            | cc   | isp                                      | ip             | chatgpt          |
|---:|:---------------------|:---------------------------|:--------------|:-----|:-----------------------------------------|:---------------|:-----------------|
|  0 | [2](config/2.json)   | 64.32.4.54                 | United States | US   | SHARKTECH                                | 107.167.13.162 | Yes (Region: US) |
|  1 | [3](config/3.json)   | 1496join.outline-vpn.cloud | United States | US   | MULTA-ASN1                               | 173.82.156.42  | Yes (Region: US) |
|  2 | [8](config/8.json)   | ophelia.mom                | Poland        | PL   | OVH SAS                                  | 54.36.174.181  | Yes (Region: FR) |
|  3 | [12](config/12.json) | 162.159.58.164             | France        | FR   | SYNLINQ                                  | 103.252.90.249 | Yes (Region: FR) |
|  4 | [17](config/17.json) | 185.39.204.69              | Turkey        | TR   | Global Internet Solutions LLC            | 185.39.204.69  | Yes (Region: TR) |
|  5 | [19](config/19.json) | 6.wyhkaa0.gq               | United States | US   | Zhejiang Aiyun Network Technology Co Ltd | 38.95.233.155  | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiNjQuMzIuNC41NCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJwb3J0IjogNDM1NTYsICJpZCI6ICI4NjUzMDA0Zi1kZTY3LTQ0YzItOWNjZS1lMDgzMDkzM2ZiMDMiLCAiYWlkIjogIjY0IiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTQ5NmpvaW4ub3V0bGluZS12cG4uY2xvdWQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICIyNjhhNDkxYi03NjRjLTQ0ZDEtODFhNC0zMGRlMTYxMzA4NjciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDQ5NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZFx1NTJhMFx1NTIyOVx1Nzk4Zlx1NWMzY1x1NGU5YVx1NWRkZVx1NmQxYlx1Njc0OVx1NzdmNk1VTFRBQ09NXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAib3BoZWxpYS5tb20iLCAiYWlkIjogMSwgImhvc3QiOiAib3BoZWxpYS5tb20iLCAiaWQiOiAiMDNmY2M2MTgtYjkzZC02Nzk2LTZhZWQtOGEzOGM5NzVkNTgxIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogImxpbmt2d3MiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEyIiwgImFkZCI6ICIxNjIuMTU5LjU4LjE2NCIsICJwb3J0IjogODAsICJpZCI6ICJjZDBjNTcwZi03NTdjLTQ4ZDItYTFiNi1jMDk0MDQzMWNjNDciLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogIm5sMTBnYnBzLjY1Nzc2MTcueHl6IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpadHJYazY1R0ZkdzduaVFZRzlh@185.39.204.69:51348#github.com/freefq%20-%20%E4%BF%84%E7%BD%97%E6%96%AF%20%2017
vmess://eyJhZGQiOiAiNi53eWhrYWEwLmdxIiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTkiLCAicG9ydCI6IDIwOTUsICJpZCI6ICI2YmJjOTU1NC0wN2JjLTQ3YzYtYTA4OC04N2FhNzlmZDVjYTEiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAiNi53eWhrYWEwLmdxIiwgInBhdGgiOiAiL1RHOkBoa2FhMCIsICJ0bHMiOiAiIn0=
```

