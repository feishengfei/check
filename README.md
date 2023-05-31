
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                | cn          | cc   | isp              | ip             | chatgpt          |
|---:|:---------------------|:--------------------|:------------|:-----|:-----------------|:---------------|:-----------------|
|  0 | [3](config/3.json)   | 154.85.1.203        | Netherlands | NL   | YISP B.V.        | 154.84.1.229   | Yes (Region: NL) |
|  1 | [4](config/4.json)   | 192.74.228.184      | China       | CN   | PEGTECHINC       | 142.0.129.201  | Yes (Region: US) |
|  2 | [8](config/8.json)   | 64.32.4.36          | Netherlands | NL   | YISP B.V.        | 154.84.1.145   | Yes (Region: NL) |
|  3 | [16](config/16.json) | 8fhq6a.aiossh.my.id | Singapore   | SG   | DIGITALOCEAN-ASN | 143.198.94.243 | Yes (Region: SG) |
|  4 | [17](config/17.json) | cdn.noice.id        | Singapore   | SG   | DIGITALOCEAN-ASN | 143.198.94.243 | Yes (Region: SG) |
|  5 | [25](config/25.json) | 8.v2-ray.cyou       | Japan       | JP   | AMAZON-02        | 18.179.36.139  | Yes (Region: JP) |
|  6 | [26](config/26.json) | gzdx.jcnode.top     | Singapore   | SG   | OVH SAS          | 15.235.184.228 | Yes (Region: SG) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiMTU0Ljg1LjEuMjAzIiwgInBvcnQiOiAiNDcyODciLCAidHlwZSI6ICJub25lIiwgImlkIjogImQzMTMzNDg0LWYyYmYtNGIwYy04ZDM4LWY4ZTY0NWI2NTY4NyIsICJhaWQiOiAiNjQiLCAibmV0IjogInRjcCIsICJwYXRoIjogIi8iLCAiaG9zdCI6ICIiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgImFkZCI6ICIxOTIuNzQuMjI4LjE4NCIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTkyNzQ3MDYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4NTE4MDIyMDg1MyIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgOCIsICJhZGQiOiAiNjQuMzIuNC4zNiIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICI4NjUzMDA0Zi1kZTY3LTQ0YzItOWNjZS1lMDgzMDkzM2ZiMDMiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTc1ODg3NzYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY4NDgyOTg5NzM4MCIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDE2IiwgImFkZCI6ICI4ZmhxNmEuYWlvc3NoLm15LmlkIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4ZmhxNmEuYWlvc3NoLm15LmlkIiwgInBhdGgiOiAiL3YycmF5IiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTciLCAidGxzIjogIiIsICJ0eXBlIjogImF1dG8iLCAic2VjdXJpdHkiOiAiYXV0byIsICJza2lwLWNlcnQtdmVyaWZ5IjogdHJ1ZSwgInNuaSI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMjUiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
ss://YWVzLTI1Ni1nY206MDUyYmM3NjktMDQ4OS00OWM3LTk3ZjItNTFiM2JiOGU1NDg2@gzdx.jcnode.top:23001#github.com/freefq%20-%20%E6%B5%99%E6%B1%9F%E7%9C%81%E5%98%89%E5%85%B4%E5%B8%82%E7%94%B5%E4%BF%A1IDC%E6%9C%BA%E6%88%BF%2026
```

