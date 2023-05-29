
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr           | cn          | cc   | isp              | ip                          | chatgpt          |
|---:|:---------------------|:---------------|:------------|:-----|:-----------------|:----------------------------|:-----------------|
|  0 | [8](config/8.json)   | cf6.biger.club | Netherlands | NL   | YISP B.V.        | 154.84.1.145                | Yes (Region: NL) |
|  1 | [9](config/9.json)   | cdn.noice.id   | Singapore   | SG   | DIGITALOCEAN-ASN | 143.198.94.243              | Yes (Region: SG) |
|  2 | [10](config/10.json) | 162.159.35.77  | France      | FR   | FEELB SARL       | 2a04:ecc0:8:a8:4567:103:0:1 | Yes (Region: FR) |
|  3 | [16](config/16.json) | cf.noaries.de  | France      | FR   | CLOUDFLARENET    | 2a09:bac1:27a0:48::13:284   | Yes (Region: FR) |
|  4 | [19](config/19.json) | 8.v2-ray.cyou  | Japan       | JP   | AMAZON-02        | 18.179.36.139               | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogImNmNi5iaWdlci5jbHViIiwgInBvcnQiOiAiMjA4NyIsICJpZCI6ICI1YWE0ZGMyMC1lYjcyLTRhMjItOTkwZi05NGFlNWNlN2E3NDMiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInVzMi5iaWdlci5jbHViIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAidGxzIn0=
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEwIiwgImFkZCI6ICIxNjIuMTU5LjM1Ljc3IiwgInBvcnQiOiA0NDMsICJpZCI6ICJjOTFjN2NiNS02MDljLTRmYWUtODE4ZS05MTk0YzNkNDY5NjkiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImFmcmhtczEyLmJlc3QtdGl6aS50b3AiLCAicGF0aCI6ICIvbGlua3dzIiwgInRscyI6ICJ0bHMifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDE2IiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiMjA1MiIsICJpZCI6ICI2N2M1Y2U0NS03YjQ4LTQ3M2UtYmYyNS1lNGM4MzBiMGVkMjQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInNjdy1mci5paWlvLndpa2kiLCAicGF0aCI6ICIvYXJpZXM_ZWQ9MjA0OCIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTkiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

