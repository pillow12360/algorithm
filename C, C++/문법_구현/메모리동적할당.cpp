#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int *arr2;
    size_t size = 5;

    // �������� �޸� �Ҵ�
    arr = (int*)malloc(size * sizeof(int));

    arr2 = (int *)malloc(sizeof(int) * 4);

    arr2[0] = 1;

    printf("%d\n",arr2[0]);

    if (arr == NULL) {
        printf("�޸� �Ҵ� ����\n");
        return 1; // ���� ���¸� ��Ÿ��
    }

    // �Ҵ�� �޸� ���
    for (size_t i = 0; i < size; i++) {
        arr[i] = i * 2;
        printf("%d ", arr[i]);
    }

    // �Ҵ�� �޸� ����
    free(arr);
    free(arr2);
    return 0; // ���� ���¸� ��Ÿ��
}