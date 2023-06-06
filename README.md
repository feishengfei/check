
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr          | cn            | cc   | isp                    | ip              | chatgpt          |
|---:|:---------------------|:--------------|:--------------|:-----|:-----------------------|:----------------|:-----------------|
|  0 | [10](config/10.json) | 167.88.61.60  | United States | US   | AS-GLOBALTELEHOST      | 167.88.61.60    | Yes (Region: US) |
|  1 | [15](config/15.json) | 38.64.138.145 | United States | US   | AS-GLOBALTELEHOST      | 38.64.138.145   | Yes (Region: US) |
|  2 | [17](config/17.json) | 104.18.23.26  | Brazil        | BR   | ORACLE-BMC-31898       | 150.230.84.193  | Yes (Region: BR) |
|  3 | [20](config/20.json) | 188.114.96.3  | United States | US   | PONYNET                | 209.141.61.121  | Yes (Region: US) |
|  4 | [21](config/21.json) | vjp1.0bad.com | Japan         | JP   | Akamai Connected Cloud | 139.162.123.236 | Yes (Region: JP) |
|  5 | [31](config/31.json) | 8.v2-ray.cyou | Japan         | JP   | AMAZON-02              | 18.179.36.139   | Yes (Region: JP) |

## Valid
```
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@167.88.61.60:7001#github.com/freefq%20-%20%E7%91%9E%E5%85%B8%20%2010
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@38.64.138.145:8090#github.com/freefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2015
vmess://eyJhZGQiOiAiMTA0LjE4LjIzLjI2IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTciLCAicG9ydCI6IDgwODAsICJpZCI6ICJkY2FmYjY2OS1mZWZjLTQ5OTQtZTNhOS01ZjQwZWQ2YWE3Y2YiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAidjJmcmVlLnNzaHRwcm9lY3Quc2hvcCIsICJwYXRoIjogIi9zc2h0cHJvamVjdCIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTg4LjExNC45Ni4zIiwgImFpZCI6IDAsICJob3N0IjogIm5ldzguaHV2aWNsb3VkLmNvbSIsICJpZCI6ICJhMTFjYTc2MC05ZWY5LTRhNjMtOTVjOS00YzVjMzJkNTYyNTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogNDQzLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVkZjRcdTg5N2ZcdTU3MjNcdTRmZGRcdTdmNTdDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIwIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAidmpwMS4wYmFkLmNvbSIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9jaGF0IiwgInBvcnQiOiA0NDMsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NjVlNVx1NjcyY1x1NGUxY1x1NGVhY1x1OTBmZFx1NTRjMVx1NWRkZFx1NTMzYUxpbm9kZVx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyAyMSIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogInZqcDEuMGJhZC5jb20ifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMzEiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

