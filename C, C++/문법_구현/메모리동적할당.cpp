#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int *arr2;
    size_t size = 5;

    // 동적으로 메모리 할당
    arr = (int*)malloc(size * sizeof(int));

    arr2 = (int *)malloc(sizeof(int) * 4);

    arr2[0] = 1;

    printf("%d\n",arr2[0]);

    if (arr == NULL) {
        printf("메모리 할당 실패\n");
        return 1; // 실패 상태를 나타냄
    }

    // 할당된 메모리 사용
    for (size_t i = 0; i < size; i++) {
        arr[i] = i * 2;
        printf("%d ", arr[i]);
    }

    // 할당된 메모리 해제
    free(arr);
    free(arr2);
    return 0; // 성공 상태를 나타냄
}