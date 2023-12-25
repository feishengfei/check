
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn              | cc   | isp                              | ip              | chatgpt          |
|---:|:---------------------|:---------------------|:----------------|:-----|:---------------------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | cm1.awslcn.info      | Malaysia        | MY   | TM TECHNOLOGY SERVICES SDN. BHD. | 58.26.140.91    | Yes (Region: US) |
|  1 | [13](config/13.json) | hk1.awslcn.info      | Hong Kong       | HK   | Hong Kong Broadband Network Ltd. | 124.244.178.235 | Yes (Region: US) |
|  2 | [27](config/27.json) | cm-cdn.kfcvme50.life | United Kingdom  | GB   | CLOUDFLARENET                    | 104.28.224.64   | Yes (Region: GB) |
|  3 | [32](config/32.json) | 156.249.18.65        | The Netherlands | NL   | YISP B.V.                        | 154.84.1.122    | Yes (Region: NL) |
|  4 | [43](config/43.json) | 45.121.48.196        | Taiwan          | TW   | EMGINECONCEPT-01                 | 45.121.48.196   | Yes (Region: TW) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMyIsICJhZGQiOiAiY20xLmF3c2xjbi5pbmZvIiwgInBvcnQiOiAiMjUyNTgiLCAidHlwZSI6ICJub25lIiwgImlkIjogIjkzZWM3MjYxLTFjOTItNDE0OS04NDhhLTI2YjZmYjlmYzRjZSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiY20xLmF3c2xjbi5pbmZvIiwgInRscyI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMTMiLCAiYWRkIjogImhrMS5hd3NsY24uaW5mbyIsICJwb3J0IjogIjI1MjQyIiwgInR5cGUiOiAibm9uZSIsICJpZCI6ICI5M2VjNzI2MS0xYzkyLTQxNDktODQ4YS0yNmI2ZmI5ZmM0Y2UiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJob3N0IjogImhrMS5hd3NsY24uaW5mbyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTdmOGVcdTU3MzBcdTUzM2EgIDI3IiwgImFkZCI6ICJjbS1jZG4ua2Zjdm1lNTAubGlmZSIsICJwb3J0IjogIjIwOTUiLCAiaWQiOiAiN2I1MjlhOGItZDMwNi00NzQ0LWI0ZTUtYzI5YWFhNDJlYzBiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1ay5rZmN2bWU1MC5saWZlIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiMTU2LjI0OS4xOC42NSIsICJhaWQiOiA2NCwgImhvc3QiOiAid3d3LjcyMjgxMTQ5Lnh5eiIsICJpZCI6ICI0ZWMwYWU2Mi1kZTA5LTQwMjktOTA0YS0wMzEzZDQ2MjhlY2YiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3BhdGgvMTcwMzIzMTI2Mjg3NSIsICJwb3J0IjogMzAwMDAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTM1N1x1OTc1ZVx1OGM2YVx1NzY3Ylx1NzcwMVx1N2VhNlx1N2ZmMFx1NTE4NVx1NjVhZlx1NTgyMUNsb3VkaW5ub3ZhdGlvblx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAzMiIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzZjBcdTZlN2VcdTc3MDEgIDQzIiwgImFkZCI6ICI0NS4xMjEuNDguMTk2IiwgInBvcnQiOiAiMTAwMDEiLCAiaWQiOiAiMGVkMzU2MjktOTE5YS00ODkxLWJhMGYtMTNjZDE5OGY4NjNiIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ0Y3AiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

