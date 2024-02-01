
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                  | cn            | cc   | isp                                  | ip                       | chatgpt          |
|---:|:---------------------|:----------------------|:--------------|:-----|:-------------------------------------|:-------------------------|:-----------------|
|  0 | [4](config/4.json)   | 158.69.0.27           | Canada        | CA   | OVH SAS                              | 2607:5300:201:3100::40e9 | Yes (Region: CA) |
|  1 | [5](config/5.json)   | 104.20.231.30         | United States | US   | Hetzner Online GmbH                  | 5.161.108.237            | Yes (Region: US) |
|  2 | [12](config/12.json) | gz.daxun.cyou         | Taiwan        | TW   | Scloud Pte Ltd                       | 165.154.237.68           | Yes (Region: TW) |
|  3 | [17](config/17.json) | cfcdn3.sanfencdn9.com | Japan         | JP   | Eons Data Communications Limited     | 38.207.152.144           | Yes (Region: US) |
|  4 | [20](config/20.json) | data-us-v1.shwjfkw.cn | United States | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138          | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpLVmNkY3NKVDZmME9XTDVzRXlNMzhB@158.69.0.27:1080#github.com/freefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%E9%AD%81%E5%8C%97%E5%85%8B%E7%9C%81%E5%8D%9A%E9%98%BF%E5%8A%AA%E7%93%A6OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%204
vmess://eyJhZGQiOiAiMTA0LjIwLjIzMS4zMCIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJteTEudG9vdGVycy5pciIsICJpZCI6ICI3MDIyOTgyZi1kYTRjLTQ4YzktYzY2MC1iMjMxNWFiZGNmN2UiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjgwIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSA1IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogImd6LmRheHVuLmN5b3UiLCAicG9ydCI6ICIyNjA0MCIsICJpZCI6ICJhYzU4NTJkZi04Y2FmLTRkODYtOGM3Ny05M2E3MDkyZjY2ZjEiLCAiYWlkIjogIjAiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJhZGQiOiAiY2ZjZG4zLnNhbmZlbmNkbjkuY29tIiwgImFpZCI6ICIwIiwgImFscG4iOiAiIiwgImZwIjogIiIsICJob3N0IjogImt2anFxa256anA2LnlvZm5oa2ZjLnh5eiIsICJpZCI6ICI1OGVjYjY2Zi04YjU1LTRiMmEtOTdjOS03Yjg3ZTE4OWQyZjciLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3ZpZGVvL1pvOThQWWZFIiwgInBvcnQiOiAiMjA1MiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTciLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjAiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgInRscyI6ICIiLCAiaWQiOiAiYjE0NzhlMjQtNDkxNi0zYWJlLThmMTctMTU5MzEwMTJlY2JlIiwgInNuaSI6ICIiLCAiaG9zdCI6ICJkYXRhLXVzLXYxLnNod2pma3cuY24iLCAicGF0aCI6ICIvZGViaWFuIn0=
```

