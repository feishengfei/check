
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr             | cn            | cc   | isp           | ip                                  | chatgpt          |
|---:|:---------------------|:-----------------|:--------------|:-----|:--------------|:------------------------------------|:-----------------|
|  0 | [1](config/1.json)   | 100.42.70.145    | United States | US   | MULTA-ASN1    | 2607:f130:109:0:d6ae:52ff:febc:e193 | Yes (Region: US) |
|  1 | [2](config/2.json)   | 64.32.24.210     | United States | US   | SHARKTECH     | 170.178.189.58                      | Yes (Region: US) |
|  2 | [4](config/4.json)   | 192.74.228.167   | United States | US   | PEGTECHINC    | 142.0.129.201                       | Yes (Region: US) |
|  3 | [7](config/7.json)   | 156.249.18.38    | Netherlands   | NL   | YISP B.V.     | 2a02:2a38:1:2796:ec4:7aff:fe81:7d76 | Yes (Region: US) |
|  4 | [8](config/8.json)   | dongtaiwang2.com | Netherlands   | NL   | CLOUDFLARENET | 2a09:bac1:5560::20a:2a              | Yes (Region: NL) |
|  5 | [13](config/13.json) | Shopify.com      | France        | FR   | CLOUDFLARENET | 2a09:bac5:3264:be::13:298           | Yes (Region: FR) |
|  6 | [16](config/16.json) | 156.225.67.230   | Netherlands   | NL   | YISP B.V.     | 154.84.1.219                        | Yes (Region: NL) |

## Valid
```
vmess://eyJhZGQiOiAiMTAwLjQyLjcwLjE0NSIsICJhaWQiOiAiNjQiLCAiZW5jcnlwdGlvbiI6ICJhdXRvIiwgImhvc3QiOiAiIiwgImlkIjogIjZhYWEyZjlmLTdjOTEtNGI1MS1hYTc3LTA1YTgzYTVkNmE0ZCIsICJuZXQiOiAidGNwIiwgInBhdGgiOiAiLyIsICJwb3J0IjogIjQxMjQ1IiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkXHU1MmEwXHU1MjI5XHU3OThmXHU1YzNjXHU0ZTlhXHU1ZGRlXHU2ZDFiXHU2NzQ5XHU3N2Y2TVVMVEFDT01cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMSIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiBmYWxzZSwgInRscyI6ICIiLCAidHlwZSI6ICIiLCAidXJsX2dyb3VwIjogInYycmF5IiwgInYiOiAiMiJ9
vmess://eyJhZGQiOiAiNjQuMzIuMjQuMjEwIiwgImFpZCI6IDY0LCAiaG9zdCI6ICIiLCAiaWQiOiAiY2ZmOWQ4NjAtNzMzMC00ZWUxLWIwNzItNzE0MmRkZjE1NzFkIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIiLCAicG9ydCI6IDQ4NjU5LCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTZkMWJcdTY3NDlcdTc3ZjZTaGFya3RlY2hcdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgMiIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTUyYTBcdTUyMjlcdTc5OGZcdTVjM2NcdTRlOWFcdTVkZGVcdTU3MjNcdTRmNTVcdTU4NWVQRUcgVEVDSFx1NjU3MFx1NjM2ZVx1NGUyZFx1NWZjMyA0IiwgImFkZCI6ICIxOTIuNzQuMjI4LjE2NyIsICJwb3J0IjogIjQ0MyIsICJpZCI6ICIwNTFiODQ0Zi1lZmUzLTQ4NDctOTJhYS02NmI1ZGUwYjZkNGUiLCAiYWlkIjogIjY0IiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ3d3cuNTkyNzQ3MDYueHl6IiwgInBhdGgiOiAiL3BhdGgvMTY5MDk3MzQ3ODk4NiIsICJ0bHMiOiAidGxzIiwgInNuaSI6ICJ3d3cuNTkyNzQ3MDYueHl6In0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRcdTRmYzRcdTUyZDJcdTUxODhcdTVkZGVcdTZjZTJcdTcyNzlcdTUxNzBBbWF6b25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNiIsICJhZGQiOiAidXMwMS52aXBub2RlLm9ubGluZSIsICJwb3J0IjogIjgwIiwgImlkIjogIjJhMTlkNDg2LWM2YjktNDE3Zi1hOGExLWE1Zjg0MWU4Nzg3OSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiIiwgInBhdGgiOiAiLyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWVcdThjNmFcdTc2N2JcdTc3MDFcdTdlYTZcdTdmZjBcdTUxODVcdTY1YWZcdTU4MjFDbG91ZGlubm92YXRpb25cdTY1NzBcdTYzNmVcdTRlMmRcdTVmYzMgNyIsICJhZGQiOiAiMTU2LjI0OS4xOC4zOCIsICJwb3J0IjogIjQ4MjIyIiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJ1cy5jYXNoZGF3aW9keGthd2phaW9jamRhd2Rhd2RhZHdyYXdnZnNlZ3NlZGVkd2FkYXdmZ3JkcmN2c3NzbC50b3AiLCAicGF0aCI6ICIvIiwgInRscyI6ICIiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDgiLCAiYWRkIjogImRvbmd0YWl3YW5nMi5jb20iLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMjVhOWYzYjktMWU2ZC00MGJkLTk2OGItZTA4MThjMWIxOTZmIiwgImFpZCI6ICIwIiwgInNjeSI6ICJhdXRvIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIyLmZyZWVrMS54eXoiLCAicGF0aCI6ICIvZG9uZ3RhaXdhbmcuY29tIiwgInRscyI6ICJ0bHMiLCAic25pIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmRDbG91ZEZsYXJlXHU1MTZjXHU1M2Y4Q0ROXHU4MjgyXHU3MGI5KHNob3BpZnkpIDEzIiwgImFkZCI6ICJTaG9waWZ5LmNvbSIsICJwb3J0IjogMjA4NiwgImlkIjogIjI1MGY0MzMxLThjM2UtNGI4Ny1hODZiLTVjNWZiZjlkZGJhOCIsICJhaWQiOiAwLCAic2N5IjogImF1dG8iLCAibmV0IjogIndzIiwgImhvc3QiOiAiRnIuY2xvdWRmbGFyZS5xdWVzdCIsICJwYXRoIjogIi9hcmllcyIsICJ0bHMiOiAiIn0=
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDE2IiwgImFkZCI6ICIxNTYuMjI1LjY3LjIzMCIsICJwb3J0IjogIjU5ODAxIiwgImlkIjogIjUxNWJjYjRkLTBiYTEtNGNhZS04N2NmLWEwNDcwMDdlZWM1NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJcdWQ4M2NcdWRkZWRcdWQ4M2NcdWRkZjBIS1x1OTk5OVx1NmUyZih5b3V0dWJlXHU5NjNmXHU0ZjFmXHU3OWQxXHU2MjgwKSIsICJwYXRoIjogIi8iLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
```

