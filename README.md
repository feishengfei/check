
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                        | cn             | cc   | isp                           | ip                        | chatgpt          |
|---:|:---------------------|:----------------------------|:---------------|:-----|:------------------------------|:--------------------------|:-----------------|
|  0 | [3](config/3.json)   | 83.142.225.20               | United Kingdom | GB   | Iomart Cloud Services Limited | 83.142.225.28             | Yes (Region: GB) |
|  1 | [8](config/8.json)   | mg.txy.a.node1.jijio.stream | Netherlands    | NL   | YISP B.V.                     | 154.84.1.145              | Yes (Region: NL) |
|  2 | [9](config/9.json)   | cdn.noice.id                | Singapore      | SG   | DIGITALOCEAN-ASN              | 143.198.94.243            | Yes (Region: SG) |
|  3 | [12](config/12.json) | 8.v2-ray.cyou               | Japan          | JP   | AMAZON-02                     | 18.179.36.139             | Yes (Region: JP) |
|  4 | [13](config/13.json) | cf.noaries.de               | United States  | US   | DEDIPATH-LLC                  | 2602:fe90:1a:1::81b7:b0dc | Yes (Region: US) |

## Valid
```
vmess://eyJhZGQiOiAiODMuMTQyLjIyNS4yMCIsICJhaWQiOiA2NCwgImhvc3QiOiAiIiwgImlkIjogIjUyNjdjYTcxLTk3ZTYtNDRjOC04ZmI1LTlmZTRhZmUwOTU0ZSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiA0OTkyMCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU4MmYxXHU1NmZkICAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAibWcudHh5LmEubm9kZTEuamlqaW8uc3RyZWFtIiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICJhZGM1NzBmMS1kNTkxLTRhNWEtOTNmMC0wMDEzYmJhM2YxMTYiLCAibmV0IjogIndzIiwgInBhdGgiOiAiL3dlc2FkIiwgInBvcnQiOiAzODk5OSwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU2NWU1XHU2NzJjICA4IiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiY2RuLm5vaWNlLmlkIiwgImFpZCI6IDAsICJob3N0IjogIjhmaHE2YS5haW9zc2gubXkuaWQiLCAiaWQiOiAiOGJiMDdjNTUtMGVmNS00ZDY5LWIxMzEtZmQ5YmFiNDIwYWU4IiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi92MnJheSIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgOSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTRmNWJcdTVjNzFcdTVlMDJcdTc5ZmJcdTUyYTggMTIiLCAiYWRkIjogIjgudjItcmF5LmN5b3UiLCAicG9ydCI6ICIyMzYwOCIsICJpZCI6ICIwZGQxOWQyMC1lYzg2LTM2ODAtYjI1Ni04NzIzN2JhZmE4OWUiLCAiYWlkIjogIjIiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICI4LnYyLXJheS5jeW91IiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU4MjgyXHU3MGI5IDEzIiwgImFkZCI6ICJjZi5ub2FyaWVzLmRlIiwgInBvcnQiOiAyMDgyLCAiaWQiOiAiNjdjNWNlNDUtN2I0OC00NzNlLWJmMjUtZTRjODMwYjBlZDI0IiwgImFpZCI6IDAsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAiaG9zdCI6ICJkZWRpcGF0aDIuaWlpby53aWtpIiwgInBhdGgiOiAiL2FyaWVzP2VkPTIwNDgiLCAidGxzIjogIiJ9
```

