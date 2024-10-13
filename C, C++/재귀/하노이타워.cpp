#include <iostream>
#include<stdio.h>
void Hanoi (int n, char from, char by, char to){
  // from �ű� ������ ���� ����
  // by �������� ���� ���� ��ġ�� ����
  // to �ű� ������ ����
  if (n==1) // base case
  {
    printf("1�� ���� %c->%c�� �̵�\n",from, to);
  }
  else{
    Hanoi(n-1,from,to,by);
    printf("%d�� ���� %c->%c�� �̵�\n",n,from,to);
    Hanoi(n-1,by,from,to); 
  }
}



int main(){

  // �ű� ������ ����
  int n = 3;
  Hanoi(n,'a','b','c');

  return 0;
}