#include <iostream>
#include<stdio.h>
void Hanoi (int n, char from, char by, char to){
  // from 옮길 원반의 시작 막대
  // by 도착지를 가기 위해 거치는 막대
  // to 옮길 원반의 막대
  if (n==1) // base case
  {
    printf("1번 원반 %c->%c로 이동\n",from, to);
  }
  else{
    Hanoi(n-1,from,to,by);
    printf("%d번 원반 %c->%c로 이동\n",n,from,to);
    Hanoi(n-1,by,from,to); 
  }
}



int main(){

  // 옮길 원반의 갯수
  int n = 3;
  Hanoi(n,'a','b','c');

  return 0;
}