
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                 | cn             | cc   | isp                              | ip                                 | chatgpt          |
|---:|:---------------------|:---------------------|:---------------|:-----|:---------------------------------|:-----------------------------------|:-----------------|
|  0 | [9](config/9.json)   | 169.197.141.187      | United States  | US   | AS-GLOBALTELEHOST                | 169.197.141.187                    | Yes (Region: US) |
|  1 | [10](config/10.json) | 156.225.67.230       | Netherlands    | NL   | YISP B.V.                        | 154.84.1.219                       | Yes (Region: NL) |
|  2 | [12](config/12.json) | 169.197.141.187      | United States  | US   | AS-GLOBALTELEHOST                | 169.197.141.187                    | Yes (Region: US) |
|  3 | [15](config/15.json) | 169.197.141.187      | United States  | US   | AS-GLOBALTELEHOST                | 169.197.141.187                    | Yes (Region: US) |
|  4 | [16](config/16.json) | 172.99.190.149       | United Kingdom | GB   | AS-GLOBALTELEHOST                | 172.99.190.149                     | Yes (Region: GB) |
|  5 | [17](config/17.json) | 172.99.190.149       | United Kingdom | GB   | AS-GLOBALTELEHOST                | 172.99.190.149                     | Yes (Region: GB) |
|  6 | [20](config/20.json) | new3.hucloud-dns.xyz | United States  | US   | PONYNET                          | 209.141.33.7                       | Yes (Region: US) |
|  7 | [21](config/21.json) | hax1.freeair.eu.org  | Germany        | DE   | Hetzner Online GmbH              | 2a01:4f8:140:229c:107c:6491:7de9:1 | Yes (Region: DE) |
|  8 | [27](config/27.json) | us2.sanfencdn.net    | United States  | US   | Eons Data Communications Limited | 65.75.221.195                      | Yes (Region: US) |

## Valid
```
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@169.197.141.187:8091#github.com/freefq%20-%20%E5%8C%97%E7%BE%8E%E5%9C%B0%E5%8C%BA%20%209
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzNTdcdTk3NWUgIDEwIiwgImFkZCI6ICIxNTYuMjI1LjY3LjIzMCIsICJwb3J0IjogIjQ5MjMxIiwgImlkIjogIjUxNWJjYjRkLTBiYTEtNGNhZS04N2NmLWEwNDcwMDdlZWM1NCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIn0=
ss://YWVzLTI1Ni1nY206ekROVmVkUkZQUWV4Rzl2@169.197.141.187:6379#github.com/freefq%20-%20%E5%8C%97%E7%BE%8E%E5%9C%B0%E5%8C%BA%20%2012
ss://YWVzLTI1Ni1nY206ZzVNZUQ2RnQzQ1dsSklk@169.197.141.187:5003#github.com/freefq%20-%20%E5%8C%97%E7%BE%8E%E5%9C%B0%E5%8C%BA%20%2015
ss://YWVzLTI1Ni1nY206UENubkg2U1FTbmZvUzI3@172.99.190.149:8090#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2016
ss://YWVzLTI1Ni1nY206cEtFVzhKUEJ5VFZUTHRN@172.99.190.149:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%2017
vmess://eyJhZGQiOiAibmV3My5odWNsb3VkLWRucy54eXoiLCAiYWlkIjogMCwgImhvc3QiOiAibmV3My5odWNsb3VkLWRucy54eXoiLCAiaWQiOiAiMWM4YWQzZjItODM1Yy00ZmRhLWI5YjYtODgxZDNjYWRmZDhlIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi8iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAyMCIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAiaGF4MS5mcmVlYWlyLmV1Lm9yZyIsICJhaWQiOiAwLCAiaG9zdCI6ICIiLCAiaWQiOiAiMmNhMTUzMTgtMTAxNS00ODZkLWVmM2UtNDY1MjEwMmEyMzVhIiwgIm5ldCI6ICJ3cyIsICJwYXRoIjogIi9oYXgxIiwgInBvcnQiOiA4MCwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1ODI4Mlx1NzBiOSAyMSIsICJ0bHMiOiAiIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
vmess://eyJhZGQiOiAidXMyLnNhbmZlbmNkbi5uZXQiLCAiYWlkIjogMCwgImhvc3QiOiAiIiwgImlkIjogImRhOWQ1Yzc0LWE1NzItNGNmNC1hMzc1LTE5Yjg4NmY1ZmZjNCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICIvemgtY24iLCAicG9ydCI6IDQ0MywgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAyNyIsICJ0bHMiOiAidGxzIiwgInR5cGUiOiAiYXV0byIsICJzZWN1cml0eSI6ICJhdXRvIiwgInNraXAtY2VydC12ZXJpZnkiOiB0cnVlLCAic25pIjogIiJ9
```

