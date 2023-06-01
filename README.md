
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                     | cn            | cc   | isp                              | ip                        | chatgpt          |
|---:|:---------------------|:-------------------------|:--------------|:-----|:---------------------------------|:--------------------------|:-----------------|
|  0 | [6](config/6.json)   | cf.noaries.de            | United States | US   | DEDIPATH-LLC                     | 2602:fe90:1a:1::81b7:b0dc | Yes (Region: US) |
|  1 | [8](config/8.json)   | cf-lt.sharecentre.online | Netherlands   | NL   | YISP B.V.                        | 154.84.1.145              | Yes (Region: NL) |
|  2 | [12](config/12.json) | cdn.noice.id             | Singapore     | SG   | DIGITALOCEAN-ASN                 | 143.198.94.243            | Yes (Region: SG) |
|  3 | [13](config/13.json) | cfcdn.sanfencdn.net      | United States | US   | Eons Data Communications Limited | 65.75.220.16              | Yes (Region: US) |
|  4 | [15](config/15.json) | gzdx.jcnode.top          | Singapore     | SG   | OVH SAS                          | 15.235.184.228            | Yes (Region: SG) |
|  5 | [16](config/16.json) | 8.v2-ray.cyou            | Japan         | JP   | AMAZON-02                        | 18.179.36.139             | Yes (Region: JP) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDYiLCAiYWRkIjogImNmLm5vYXJpZXMuZGUiLCAicG9ydCI6ICIyMDgyIiwgImlkIjogIjY3YzVjZTQ1LTdiNDgtNDczZS1iZjI1LWU0YzgzMGIwZWQyNCIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGVkaXBhdGgyLmlpaW8ud2lraSIsICJwYXRoIjogIi9hcmllcz9lZD0yMDQ4IiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDgiLCAiYWRkIjogImNmLWx0LnNoYXJlY2VudHJlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjJkNWQ4YjljLThlYzQtNGEzNy1iNjEwLTc4ZTcxZTEzZWFlZiIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAibHYyLnNoYXJlY2VudHJlcHJvLm9yZyIsICJwYXRoIjogIi9zaGlya2VyIiwgInRscyI6ICIiLCAic25pIjogIiIsICJhbHBuIjogIiJ9
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTIiLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJhZGQiOiAiY2ZjZG4uc2FuZmVuY2RuLm5ldCIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDEzIiwgInBvcnQiOiA0NDMsICJpZCI6ICI5NTFhMzkzYS1iNTU3LTQ1OTAtODhiNi0zMDk0OGUxZTBiOGQiLCAiYWlkIjogIjAiLCAibmV0IjogIndzIiwgInR5cGUiOiAiIiwgImhvc3QiOiAidXMxLnNhbmZlbmNkbi5uZXQiLCAicGF0aCI6ICIvemgtY24iLCAidGxzIjogInRscyJ9
ss://YWVzLTI1Ni1nY206MDUyYmM3NjktMDQ4OS00OWM3LTk3ZjItNTFiM2JiOGU1NDg2@gzdx.jcnode.top:23001#github.com/freefq%20-%20%E6%B5%99%E6%B1%9F%E7%9C%81%E5%98%89%E5%85%B4%E5%B8%82%E7%94%B5%E4%BF%A1IDC%E6%9C%BA%E6%88%BF%2015
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTYiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
```

