# 미래 도시

## 느낀점
* 다익스트라 vs 플로이드 와샬

## notes
* 

## input
```
5 7 // vn 5, en 7
1 2 // 1-2
1 3 // ...
1 4
2 4
3 4
3 5
4 5 // 4-5
4 5 // 5를 들려서 4로 가야함.
```
```
4 2
1 3
2 4
3 4 // 4를 거쳐서 3으로 가야함.
```

## output
```
3 // 1 - 3 - 5 - 4 거치면 됨.
```
```
-1 // 방법이 없음.
```

## strategy
* 보통 통밥으로 문제를 훑으면 항상 놓치는 게 있다. 다음 프로세스를 잘 따르자.
  * input output 정리 (문제 통독)
  * 주어진 TC 종이에 써보면서 이해 (DP나 그래프 문제일 경우엔 더더욱)
  * 문제 정독
  * strategy 작성
  * 코드 작성
* 플로이드 와샬값 + 1 해줘야 함.


```
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
```
```
4 2
1 3
2 4
3 4
```