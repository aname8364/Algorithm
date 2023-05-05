#include <iostream>
#include <vector>

int binary_search(std::vector<int> arr, int min, int max, int num) {
    if (min > max) return -1;
    
    int mid = (min+max)/2;
    
    if (arr[mid] > num) {
        // 찾으려는 값이 왼쪽에 있음
        return binary_search(arr, min, mid-1, num);
    }
    else if (arr[mid] < num) {
        // 찾으려는 값이 오른쪽에 있음
        return binary_search(arr, mid+1, max, num);
    }
    else return mid;
}

int main() {
    std::vector<int> arr = {1, 3, 5, 6, 8, 10, 13, 14, 15};
    
    int target_num;
    scanf("%d", &target_num);

    int target_idx;
    target_idx = binary_search(arr, 0, arr.size(), target_num);
    if (target_idx < 0) {
        printf("Failed to find");
        return 1;
    }
    printf("%d", target_idx);
}