
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn            | cc   | isp              | ip                                    | chatgpt          |
|---:|:---------------------|:--------------------|:--------------|:-----|:-----------------|:--------------------------------------|:-----------------|
|  0 | [8](config/8.json)   | armus.114514782.xyz | Netherlands   | NL   | YISP B.V.        | 154.84.1.145                          | Yes (Region: NL) |
|  1 | [24](config/24.json) | cdn.noice.id        | Singapore     | SG   | DIGITALOCEAN-ASN | 143.198.94.243                        | Yes (Region: SG) |
|  2 | [29](config/29.json) | cf.noaries.de       | United States | US   | DEDIPATH-LLC     | 2602:fe90:1a:1::81b7:b0dc             | Yes (Region: US) |
|  3 | [30](config/30.json) | cdn.yuntujisu.ml    | United States | US   | PONYNET          | 2605:6400:20:1fa6:c288:57d0:989e:4654 | Yes (Region: US) |
|  4 | [33](config/33.json) | 8.v2-ray.cyou       | Japan         | JP   | AMAZON-02        | 18.179.36.139                         | Yes (Region: JP) |
|  5 | [36](config/36.json) | gzdx.jcnode.top     | Singapore     | SG   | OVH SAS          | 15.235.184.228                        | Yes (Region: SG) |

## Valid
```
vmess://eyJhZGQiOiAiYXJtdXMuMTE0NTE0NzgyLnh5eiIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMTRhOGJhMzgtODkxOC0zZGUxLWJjOTMtOWZjODc3NzdkYTMwIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9taWFvIiwgInBvcnQiOiAyMDUyLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFNZWxib3VybmUgR2lybHMgQ29sbGVnZSA4IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMjQiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDI5IiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiMjA4MiIsICJpZCI6ICI2N2M1Y2U0NS03YjQ4LTQ3M2UtYmYyNS1lNGM4MzBiMGVkMjQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImRlZGlwYXRoMi5paWlvLndpa2kiLCAicGF0aCI6ICIvYXJpZXM_ZWQ9MjA0OCIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiY2RuLnl1bnR1amlzdS5tbCIsICJhaWQiOiAwLCAiaG9zdCI6ICJuYW5vdXMueXRqczExNDUxNC5tbCIsICJpZCI6ICJkNTliMjRiMS1iNDc1LTRkNDQtYmU0Ni1hMTg1NjNhODc3MTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogMjA5NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAzMCIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMzMiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206MDUyYmM3NjktMDQ4OS00OWM3LTk3ZjItNTFiM2JiOGU1NDg2@gzdx.jcnode.top:23001#github.com/freefq%20-%20%E6%B5%99%E6%B1%9F%E7%9C%81%E5%98%89%E5%85%B4%E5%B8%82%E7%94%B5%E4%BF%A1IDC%E6%9C%BA%E6%88%BF%2036
```

