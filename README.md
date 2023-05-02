
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                   | cn   | cc   | isp   | ip                    | chatgpt          |
|---:|:---------------------|:-----------------------|:-----|:-----|:------|:----------------------|:-----------------|
|  0 | [3](config/3.json)   | 156.245.8.168          |      |      |       | 154.84.1.140          | Yes (Region: NL) |
|  1 | [5](config/5.json)   | 154.85.0.242           |      |      |       | 154.84.1.145          | Yes (Region: NL) |
|  2 | [8](config/8.json)   | 173.245.49.16          |      |      |       | 169.197.141.187       | Yes (Region: US) |
|  3 | [9](config/9.json)   | join-bede.vmessorg.fun |      |      |       | 2a01:4f8:192:348a::2  | Yes (Region: DE) |
|  4 | [11](config/11.json) | 169.197.141.187        |      |      |       | 169.197.141.187       | Yes (Region: US) |
|  5 | [15](config/15.json) | 104.26.1.48            |      |      |       | 2a01:4f8:c010:7f47::1 | Yes (Region: DE) |
|  6 | [26](config/26.json) | 172.64.153.178         |      |      |       | 2a01:4f9:c010:baec::1 | Yes (Region: DE) |
|  7 | [27](config/27.json) | new6.huvicloud.com     |      |      |       | 199.195.251.9         | Yes (Region: US) |
|  8 | [35](config/35.json) | 167.88.61.213          |      |      |       | 167.88.61.213         | Yes (Region: US) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDMiLCAiYWRkIjogIjE1Ni4yNDUuOC4xNjgiLCAicG9ydCI6ICI0OTkyMCIsICJpZCI6ICJiOGRmM2VmMS04ODdmLTRlZTQtODU1Zi00ZjgwNDE2YzI0NjQiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU0Ljg1LjAuMjQyIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiNmU3OWVlYTQtNWY3Mi00NjgzLWFkMGUtNTMzOWYwMTM0MjFiIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQyMjYyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTVmMTdcdTU0MDlcdTVjM2NcdTRlOWFcdTVkZGVcdTk2M2ZcdTRlYzBcdTY3MmNOViBORVhUXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIDgiLCAiYWRkIjogIjE3My4yNDUuNDkuMTYiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiNjYyZjRlNzQtYjA3NS00ZDg1LWQ2OGQtNjFjNTE4ODI0MjlmIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJrb3R0MS52dGNzcy50b3AiLCAicGF0aCI6ICIvIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiam9pbi1iZWRlLnZtZXNzb3JnLmZ1biIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjkxMTA1YzktMjA2MS00MGU2LTkyMTktZDA0ZDViNDg2OWQzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI4MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OWE2Y1x1Njc2NVx1ODk3Zlx1NGU5YVRtbmV0XHU1OTI3XHU5YTZjXHU3NTM1XHU4YmFmIDkiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@169.197.141.187:7307#github.com/freefq%20-%20%E5%8C%97%E7%BE%8E%E5%9C%B0%E5%8C%BA%20%2011
vmess://eyJhZGQiOiAiMTA0LjI2LjEuNDgiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiaDMubWFtYWRjdWN1LmNvbSIsICJpZCI6ICIxOTM1MGQ2NC02ODY4LTRhNjQtZTUwMS05YzBkZjkwM2Q3ODgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjIwOTUiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE1IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4xNzgiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiaC5oM2lvLmNvIiwgImlkIjogImZjYmQ1YzA3LWZiYTUtNGZmOS1jMTljLTAyZTAyMzIyMDYyOCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICJobzNpbm8iLCAicG9ydCI6ICIyMDk2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyNiIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiaC5oM2lvLmNvIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAibmV3Ni5odXZpY2xvdWQuY29tIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJhMTFjYTc2MC05ZWY5LTRhNjMtOTVjOS00YzVjMzJkNTYyNTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL2h1dmkiLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyNyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@167.88.61.213:8090#github.com/freefq%20-%20%E7%91%9E%E5%85%B8%20%2035
```

