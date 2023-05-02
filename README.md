
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                    | cn            | cc   | isp                               | ip                    | chatgpt          |
|---:|:---------------------|:------------------------|:--------------|:-----|:----------------------------------|:----------------------|:-----------------|
|  0 | [3](config/3.json)   | hinet1261.gfwisbest.xyz | Taiwan        | TW   | Data Communication Business Group | 1.171.220.200         | Yes (Region: TW) |
|  1 | [5](config/5.json)   | join-bede.vmessorg.fun  | Germany       | DE   | Hetzner Online GmbH               | 2a01:4f8:192:348a::2  | Yes (Region: DE) |
|  2 | [7](config/7.json)   | snappfood.ir            | Netherlands   | NL   | DIGITALOCEAN-ASN                  | 146.190.21.248        | Yes (Region: NL) |
|  3 | [10](config/10.json) | hd.mamadcucu.com        | Germany       | DE   | Hetzner Online GmbH               | 2a01:4f8:c010:7495::1 | Yes (Region: DE) |
|  4 | [12](config/12.json) | 167.88.61.213           | United States | US   | AS-GLOBALTELEHOST                 | 167.88.61.213         | Yes (Region: US) |
|  5 | [16](config/16.json) | 104.26.1.48             | Germany       | DE   | Hetzner Online GmbH               | 2a01:4f8:c010:7f47::1 | Yes (Region: DE) |
|  6 | [17](config/17.json) | 172.64.153.178          | Finland       | FI   | Hetzner Online GmbH               | 2a01:4f9:c010:baec::1 | Yes (Region: DE) |
|  7 | [21](config/21.json) | snappfood.ir            | Netherlands   | NL   | DIGITALOCEAN-ASN                  | 146.190.21.248        | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiaGluZXQxMjYxLmdmd2lzYmVzdC54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogIjIyODUxMzNlLWI5YmEtM2ZiNS1hMjQ2LTljN2RkY2MyY2Q3YSIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiIiwgInBvcnQiOiAyMjQsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1NTNmMFx1NmU3ZVx1NzcwMVx1NjViMFx1NTMxN1x1NWUwMlx1NGUyZFx1NTM0ZVx1NzUzNVx1NGZlMSAzIiwgInRscyI6ICIiLCAidHlwZSI6ICJhdXRvIiwgInNlY3VyaXR5IjogImF1dG8iLCAic2tpcC1jZXJ0LXZlcmlmeSI6IHRydWUsICJzbmkiOiAiIn0=
vmess://eyJhZGQiOiAiam9pbi1iZWRlLnZtZXNzb3JnLmZ1biIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICIiLCAiaWQiOiAiYjkxMTA1YzktMjA2MS00MGU2LTkyMTktZDA0ZDViNDg2OWQzIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6ICI4MCIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1OWE2Y1x1Njc2NVx1ODk3Zlx1NGU5YVRtbmV0XHU1OTI3XHU5YTZjXHU3NTM1XHU4YmFmIDUiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAic25hcHBmb29kLmlyIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiMmRiYjQwM2UtMzQzYy00YjA5LWE4NGQtYzRlNmFmZjRkNmIxIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDciLCAiaG9zdCI6ICJkYXl6LWdvbmUud2Vic2l0ZSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIiwgInR5cGUiOiAibm9uZSIsICJzZXJ2ZXJQb3J0IjogMCwgIm5hdGlvbiI6ICIifQ==
vmess://eyJhZGQiOiAiaGQubWFtYWRjdWN1LmNvbSIsICJhaWQiOiAiMCIsICJhbHBuIjogIiIsICJmcCI6ICIiLCAiaG9zdCI6ICJoNC5tYW1hZGN1Y3UuY29tIiwgImlkIjogIjhlZDlhZWMyLWUwMmUtNGEyNy1mZTAyLWMzZTIwNDUyZTRjNyIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvIiwgInBvcnQiOiAiMjA1MiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMTAiLCAic2N5IjogImF1dG8iLCAic25pIjogIiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiIiwgInYiOiAiMiJ9
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@167.88.61.213:8090#github.com/freefq%20-%20%E7%91%9E%E5%85%B8%20%2012
vmess://eyJhZGQiOiAiMTA0LjI2LjEuNDgiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiaDMubWFtYWRjdWN1LmNvbSIsICJpZCI6ICIxOTM1MGQ2NC02ODY4LTRhNjQtZTUwMS05YzBkZjkwM2Q3ODgiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjIwOTUiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5IDE2IiwgInNjeSI6ICJhdXRvIiwgInNuaSI6ICIiLCAidGxzIjogIiIsICJ0eXBlIjogIiIsICJ2IjogIjIifQ==
vmess://eyJhZGQiOiAiMTcyLjY0LjE1My4xNzgiLCAiYWlkIjogIjAiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIiwgImhvc3QiOiAiaC5oM2lvLmNvIiwgImlkIjogImZjYmQ1YzA3LWZiYTUtNGZmOS1jMTljLTAyZTAyMzIyMDYyOCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICJobzNpbm8iLCAicG9ydCI6ICIyMDk2IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAxNyIsICJzY3kiOiAiYXV0byIsICJzbmkiOiAiaC5oM2lvLmNvIiwgInRscyI6ICJ0bHMiLCAidHlwZSI6ICIiLCAidiI6ICIyIn0=
vmess://eyJhZGQiOiAic25hcHBmb29kLmlyIiwgInBvcnQiOiAiODAiLCAiaWQiOiAiZTY0MGI3YTgtYzQyZC00MTg4LWQ0MTEtNGZiNzczNmY5MGJjIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDIxIiwgImhvc3QiOiAiZGF5ei1nb25lLndlYnNpdGUiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiIsICJ0eXBlIjogIm5vbmUiLCAic2VydmVyUG9ydCI6IDAsICJuYXRpb24iOiAiIn0=
```

