
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                              | cn            | cc   | isp                 | ip                    | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------|:--------------|:-----|:--------------------|:----------------------|:-----------------|
|  0 | [2](config/2.json)   | 156.249.18.10                                                     | Netherlands   | NL   | YISP B.V.           | 154.84.1.40           | Yes (Region: NL) |
|  1 | [3](config/3.json)   | 64.32.4.41                                                        | United States | US   | SHARKTECH           | 107.167.13.162        | Yes (Region: US) |
|  2 | [5](config/5.json)   | 156.225.67.158                                                    | Netherlands   | NL   | YISP B.V.           | 154.84.1.197          | Yes (Region: NL) |
|  3 | [6](config/6.json)   | dl6.v001sssv.pw                                                   | Germany       | DE   | Hetzner Online GmbH | 2a01:4f8:1c17:4d19::1 | Yes (Region: DE) |
|  4 | [8](config/8.json)   | 8.cashdawiodxkawjaiocjdawdawdadwrawgfsegsededwadawfgrdrcvsssl.top | Germany       | DE   | AS-GLOBALTELEHOST   | 193.108.118.34        | Yes (Region: DE) |
|  5 | [26](config/26.json) | 104.31.16.58                                                      |               |      |                     | 2a01:4f8:1c17:c667::1 | Yes (Region: DE) |

## Valid
```
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJhZGQiOiAiMTU2LjI0OS4xOC4xMCIsICJwb3J0IjogIjQ2MDAzIiwgImlkIjogIjVhNGQ2OWFkLTIwYTktNDk0MS1iMjIzLTg3YmJkMDlmNWY1MiIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMyIsICJhZGQiOiAiNjQuMzIuNC40MSIsICJwb3J0IjogIjQzMTY2IiwgImlkIjogIjg2NTMwMDRmLWRlNjctNDRjMi05Y2NlLWUwODMwOTMzZmIwMyIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZmFcdWQ4M2NcdWRkZjhVU1x1N2Y4ZVx1NTZmZCh5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwMikiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDUiLCAiYWRkIjogIjE1Ni4yMjUuNjcuMTU4IiwgInBvcnQiOiAiNDg4MTIiLCAiaWQiOiAiOWMwMjZlZmUtNmFmMC00NjVmLWI4YzAtM2Y1OGM4YzJkNGM1IiwgImFpZCI6ICI2NCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAidGNwIiwgInR5cGUiOiAibm9uZSIsICJob3N0IjogIiIsICJwYXRoIjogIiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIifQ==
vmess://eyJhZGQiOiAiZGw2LnYwMDFzc3N2LnB3IiwgImFpZCI6IDAsICJob3N0IjogIiIsICJpZCI6ICI4ZWVjZTJlMS1jZmMxLTRmODQtODAzZS0xYTY2NjUwOTgyZWEiLCAibmV0IjogIndzIiwgInBhdGgiOiAiLyIsICJwb3J0IjogODAsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTgyODJcdTcwYjkgNiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTZmYjNcdTU5MjdcdTUyMjlcdTRlOWFDYW50ZXJidXJ5IEdpcmxzJyBTZWNvbmRhcnkgQ29sbGVnZSA4IiwgImFkZCI6ICI4LmNhc2hkYXdpb2R4a2F3amFpb2NqZGF3ZGF3ZGFkd3Jhd2dmc2Vnc2VkZWR3YWRhd2ZncmRyY3Zzc3NsLnRvcCIsICJwb3J0IjogIjIwOTUiLCAiaWQiOiAiMzFkNDlkZWUtMDkzMS00MjIzLWEwYmItNjAxNDFiYzUxMTQxIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJqcHBwcC5jYXNoZGF3aW9keGthd2phaW9jamRhd2Rhd2RhZHdyYXdnZnNlZ3NlZGVkd2FkYXdmZ3JkcmN2c3NzbC50b3AiLCAicGF0aCI6ICIvIiwgInRscyI6ICIifQ==
vmess://eyJhZGQiOiAiMTA0LjMxLjE2LjU4IiwgInYiOiAiMiIsICJwcyI6ICJnaXRodWIuY29tL2ZyZWVmcSAtIFx1N2Y4ZVx1NTZmZENsb3VkRmxhcmVcdTUxNmNcdTUzZjhDRE5cdTgyODJcdTcwYjkgMjYiLCAicG9ydCI6IDQ0MywgImlkIjogImExMGY5ZDI0LWJiNWQtNDYyMi1lNzViLWYwMmMzNDg1MDZhOSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJNY2ktUmlnaHRlbC10YWxpYS1tb2toYWJlcmF0LmlyYW5jZWxsLWlyYW5jZWxsLndlYnNpdGUiLCAicGF0aCI6ICIvQFNleXllZE1UIEBTZXl5ZWRNVCIsICJ0bHMiOiAidGxzIn0=
```

