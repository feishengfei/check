
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                                                                                            | cn          | cc   | isp                            | ip              | chatgpt          |
|---:|:---------------------|:------------------------------------------------------------------------------------------------|:------------|:-----|:-------------------------------|:----------------|:-----------------|
|  0 | [1](config/1.json)   | 94.131.12.58                                                                                    | Switzerland | CH   | Stark Industries Solutions Ltd | 94.131.12.58    | Yes (Region: CH) |
|  1 | [3](config/3.json)   | 94.131.115.129                                                                                  | Sweden      | SE   | Stark Industries Solutions Ltd | 94.131.115.129  | Yes (Region: SE) |
|  2 | [5](config/5.json)   | 45.159.249.231                                                                                  | Finland     | FI   | Stark Industries Solutions Ltd | 45.159.249.231  | Yes (Region: FI) |
|  3 | [16](config/16.json) | 54.36.174.181                                                                                   | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  4 | [18](config/18.json) | ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  5 | [24](config/24.json) | 54.36.174.181                                                                                   | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  6 | [27](config/27.json) | www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou | Poland      | PL   | OVH SAS                        | 54.36.174.181   | Yes (Region: FR) |
|  7 | [30](config/30.json) | 183.233.187.214                                                                                 | China       | CN   | CNSERVERS                      | 192.151.223.154 | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpCMHJ5NTZYMkF4ZkZnY2dJN3NIRFdE@94.131.12.58:26669#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%201
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpiTlVlMGpSOXJ6c3ZMRXpmUG1JNE9m@94.131.115.129:38108#github.com/freefq%20-%20%E4%B9%8C%E5%85%8B%E5%85%B0%20%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp6SVBqeW5LTlZWYUJuS0swVVo1enUy@45.159.249.231:38584#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%20%205
ss://YWVzLTI1Ni1nY206Rm9PaUdsa0FBOXlQRUdQ@54.36.174.181:7307#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2016
ss://YWVzLTI1Ni1nY206Y2RCSURWNDJEQ3duZklO@ak1732.www.outline.network.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:8119#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2018
ss://YWVzLTI1Ni1nY206ZmFCQW9ENTRrODdVSkc3@54.36.174.181:2375#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2024
ss://YWVzLTI1Ni1nY206UmV4bkJnVTdFVjVBRHhH@www.outline.network.ak1941.fr8678825324247b8176d59f83c30bd94d23d2e3ac5cd4a743bkwqeikvdyufr.cyou:7001#github.com/freefq%20-%20%E6%B3%95%E5%9B%BD%E6%A0%BC%E6%8B%89%E6%B2%83%E5%88%A9%E8%AE%B7OVH%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2027
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTVlN2ZcdTVkZGVcdTVlMDJcdTc5ZmJcdTUyYTggMzAiLCAiYWRkIjogIjE4My4yMzMuMTg3LjIxNCIsICJwb3J0IjogIjUwOTY1IiwgImlkIjogIjQxODA0OGFmLWEyOTMtNGI5OS05YjBjLTk4Y2EzNTgwZGQyNCIsICJhaWQiOiAiNjQiLCAic2N5IjogImF1dG8iLCAibmV0IjogInRjcCIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICIiLCAicGF0aCI6ICIiLCAidGxzIjogIiIsICJzbmkiOiAiIiwgImFscG4iOiAiIn0=
```

