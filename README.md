
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn          | cc   | isp                 | ip              | chatgpt          |
|---:|:---------------------|:---------------|:------------|:-----|:--------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 156.225.67.158 | Netherlands | NL   | YISP B.V.           | 154.84.1.197    | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 104.31.16.71   | Germany     | DE   | Hetzner Online GmbH | 116.203.200.107 | Yes (Region: DE) |
|  2 | [5](config/5.json)   | api.jquery.com | Canada      | CA   | AS-GLOBALTELEHOST   | 172.99.189.86   | Yes (Region: CA) |
|  3 | [8](config/8.json)   | 172.64.90.186  | Poland      | PL   | OVH SAS             | 54.36.174.181   | Yes (Region: FR) |
|  4 | [10](config/10.json) | 156.249.18.204 | Netherlands | NL   | YISP B.V.           | 154.84.1.229    | Yes (Region: NL) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDMiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTU4IiwgInBvcnQiOiA0NDMsICJpZCI6ICI5YzAyNmVmZS02YWYwLTQ2NWYtYjhjMC0zZjU4YzhjMmQ0YzUiLCAiYWlkIjogNjQsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJ3d3cuODQ2NjExNTgueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5NTE3NzA2Mjk1NiIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDQiLCAiYWRkIjogIjEwNC4zMS4xNi43MSIsICJwb3J0IjogMjA4MywgImlkIjogIjE1YmYwZGI0LWZiZmYtNDZkMC1hNDg2LWI2ZTRhOWU3NGE5MSIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAiZ2VybWFueS1vbmUucG9ydDg4OC5zaXRlIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDUiLCAiYWRkIjogImFwaS5qcXVlcnkuY29tIiwgInBvcnQiOiA0NDMsICJpZCI6ICIwM2ZjYzYxOC1iOTNkLTY3OTYtNmFlZC04YTM4Yzk3NWQ1ODEiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogInN1Yi55aWZlbmppY2hhbmcudG9wIiwgInBhdGgiOiAiL29saXYuYmVhdXR5OjQ0My9saW5rdndzIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogIjE3Mi42NC45MC4xODYiLCAicG9ydCI6ICI4MCIsICJpZCI6ICI1Zjc1MWM2ZS01MGIxLTQ3OTctYmE4ZS02ZmZlMzI0YTBiY2UiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImNhLmlsb3Zlc2NwLmNvbSIsICJwYXRoIjogIi9zaGlya2VyIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC4yMDQiLCAiYWlkIjogNjQsICJob3N0IjogIiIsICJpZCI6ICJkMzEzMzQ4NC1mMmJmLTRiMGMtOGQzOC1mOGU2NDViNjU2ODciLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNTQ4ODUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZVx1OGM2YVx1NzY3Ylx1NzcwMVx1N2VhNlx1N2ZmMFx1NTE4NVx1NjVhZlx1NTgyMUNsb3VkaW5ub3ZhdGlvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAxMCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

