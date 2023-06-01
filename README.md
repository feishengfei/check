
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr               | cn            | cc   | isp                                           | ip                                    | chatgpt          |
|---:|:---------------------|:-------------------|:--------------|:-----|:----------------------------------------------|:--------------------------------------|:-----------------|
|  0 | [3](config/3.json)   | cdn.yuntujisu.ml   | United States | US   | PONYNET                                       | 2605:6400:20:1fa6:c288:57d0:989e:4654 | Yes (Region: US) |
|  1 | [16](config/16.json) | 156.245.8.158      | Netherlands   | NL   | YISP B.V.                                     | 154.84.1.138                          | Yes (Region: NL) |
|  2 | [17](config/17.json) | 156.249.18.9       | Netherlands   | NL   | YISP B.V.                                     | 154.84.1.40                           | Yes (Region: NL) |
|  3 | [20](config/20.json) | 154.84.1.46        | Netherlands   | NL   | YISP B.V.                                     | 154.84.1.121                          | Yes (Region: NL) |
|  4 | [22](config/22.json) | cf.noaries.de      | United States | US   | DEDIPATH-LLC                                  | 2602:fe90:1a:1::81b7:b0dc             | Yes (Region: US) |
|  5 | [23](config/23.json) | cdn.noice.id       | Singapore     | SG   | DIGITALOCEAN-ASN                              | 143.198.94.243                        | Yes (Region: SG) |
|  6 | [30](config/30.json) | 8.v2-ray.cyou      | Japan         | JP   | AMAZON-02                                     | 18.179.36.139                         | Yes (Region: JP) |
|  7 | [31](config/31.json) | turkey.abraak.site | Turkey        | TR   | Teknosos Bilisim Hizmetleri Ve Tic. Ltd. Sti. | 212.64.214.179                        | Yes (Region: TR) |

## Valid
```
vmess://eyJhZGQiOiAiY2RuLnl1bnR1amlzdS5tbCIsICJhaWQiOiAwLCAiaG9zdCI6ICJuYW5vdXMueXRqczExNDUxNC5tbCIsICJpZCI6ICJkNTliMjRiMS1iNDc1LTRkNDQtYmU0Ni1hMTg1NjNhODc3MTEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogMjA5NSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTk5OTlcdTZlMmYgIDE2IiwgImFkZCI6ICIxNTYuMjQ1LjguMTU4IiwgInBvcnQiOiAiNDQzIiwgImlkIjogIjExMTE3ZDRjLTNiNmEtNGU3Ni04YmNjLTJiNDFiM2U5Y2E5MyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAiZHRscyIsICJob3N0IjogInd3dy4xMTY0OTc2OS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjg0NzUwOTYxMTczIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMTciLCAiYWRkIjogIjE1Ni4yNDkuMTguOSIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI1YTRkNjlhZC0yMGE5LTQ5NDEtYjIyMy04N2JiZDA5ZjVmNTIiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNDg2NDM3MDAueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4NDMwNjI3MjQzMCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMjAiLCAiYWRkIjogIjE1NC44NC4xLjQ2IiwgInBvcnQiOiAiNDQzIiwgImlkIjogImJkMjQ5ZTM3LTczNTktNDFlZS04NGE3LTA5ZTQ5ZTBlYzVjNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogInd3dy40NzUyMzM3NS54eXoiLCAicGF0aCI6ICIvcGF0aC8xNjg0NjY3NjM2NjMyIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDIyIiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAiMjA4MiIsICJpZCI6ICI2N2M1Y2U0NS03YjQ4LTQ3M2UtYmYyNS1lNGM4MzBiMGVkMjQiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogImRlZGlwYXRoMi5paWlvLndpa2kiLCAicGF0aCI6ICIvYXJpZXM_ZWQ9MjA0OCIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMjMiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMzAiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAidHVya2V5LmFicmFhay5zaXRlIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICIyMTAyNTgzOS1jMTQwLTRjNjctOGY0Yy05YTQxM2NhOGRlM2YiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAicG9ydCI6IDIwODcsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NGYwYVx1NjcxNyAgMzEiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
```

