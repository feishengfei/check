
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr            | cn            | cc   | isp              | ip                                   | chatgpt          |
|---:|:---------------------|:----------------|:--------------|:-----|:-----------------|:-------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | cf.noaries.de   | United States | US   | DEDIPATH-LLC     | 2602:fe90:1a:1::81b7:b0dc            | Yes (Region: US) |
|  1 | [5](config/5.json)   | 154.85.1.218    | Netherlands   | NL   | YISP B.V.        | 2a02:2a38:1:2796:ae1f:6bff:fe9b:2864 | Yes (Region: NL) |
|  2 | [6](config/6.json)   | 141.147.153.244 | Japan         | JP   | ORACLE-BMC-31898 | 141.147.153.244                      | Yes (Region: JP) |
|  3 | [11](config/11.json) | 64.32.4.36      | United States | US   | SHARKTECH        | 107.167.13.162                       | Yes (Region: US) |
|  4 | [13](config/13.json) | cdn.noice.id    | Singapore     | SG   | DIGITALOCEAN-ASN | 143.198.94.243                       | Yes (Region: SG) |
|  5 | [19](config/19.json) | 8.v2-ray.cyou   | Japan         | JP   | AMAZON-02        | 18.179.36.139                        | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDMiLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6IDIwODIsICJpZCI6ICI2N2M1Y2U0NS03YjQ4LTQ3M2UtYmYyNS1lNGM4MzBiMGVkMjQiLCAiYWlkIjogMCwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJob3N0IjogImRlZGlwYXRoMi5paWlvLndpa2kiLCAicGF0aCI6ICIvYXJpZXM_ZWQ9MjA0OCIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNSIsICJhZGQiOiAiMTU0Ljg1LjEuMjE4IiwgInBvcnQiOiAiNDgzMjAiLCAiaWQiOiAiNzQzYmRjODctMWRlYS00MWJmLWFhMGItNTFkZmJiZmVjOGFhIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiMTQxLjE0Ny4xNTMuMjQ0IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJkNDdkNzEzNS0wOTU0LTQ2YWItYTE5MC0xN2I2Yzg2MzBhODUiLCAibmV0IjogInRjcCIsICJwYXRoIjogIiIsICJwb3J0IjogNDE1NDUsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NzQ1ZVx1NTE3OE9yYWNsZSBDb3Jwb3JhdGlvbiA2IiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTEiLCAiYWRkIjogIjY0LjMyLjQuMzYiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiODY1MzAwNGYtZGU2Ny00NGMyLTljY2UtZTA4MzA5MzNmYjAzIiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAid3d3LjU3NTg4Nzc2Lnh5eiIsICJwYXRoIjogIi9wYXRoLzE2ODUzNjE1Njc3NjEiLCAidGxzIjogInRscyIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTkiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

