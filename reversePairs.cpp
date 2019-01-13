#include <iostream>
#include <vector>



long long merge(std::vector<int> &arr, int l, int s, int r) {
    int i = l;
    int j = s + 1;
    std::vector<int> aux;
    long long cntInv = 0;
    while (i <= s && j <= r) {
	if (arr[i] <= arr[j]) {
		aux.push_back(arr[i]);
		i++;
	} else {
		cntInv += s - i + 1;
		aux.push_back(arr[j]);
		j++;
	}
    }
    while (i <= s) {
	aux.push_back(arr[i++]);	
    }
    while (j <= r) {
	aux.push_back(arr[j++]);
    }

    for (int k = l; k <= r; k++) {
	arr[k] = aux[k - l];
    }
    return cntInv;
}

long long mergeSort(std::vector<int> &arr, int l, int r) {
    if (l >= r) {
	return 0;
    }
    int m = l + (r - l) / 2;
    long long cntLeft = mergeSort(arr, l, m);
    long long cntRight = mergeSort(arr, m + 1, r);
    long long cntSplit = merge(arr, l, m, r);
    return cntLeft + cntRight + cntSplit;
}



int main() {
    int n;	
    std::cin >> n;
    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
	long long cnt = mergeSort(arr, 0, n - 1);
	std::cout << cnt;
}
