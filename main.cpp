#include <iostream>
#include <vector>
#include <map>
#include <random>

template <class T>
void print(std::vector<T> arr) {
    std::cout << '[';
    for (int i = 0; i < arr.size() - 1; i++) {
        std::cout <<  arr[i] << ", ";
    }
    std::cout << arr[arr.size() - 1] << ']';
}


template <class T>
void selectionSort(std::vector<T> &arr) {
    /*
     arr[0, i-1] sorted
     arr[i, n-1] unsorted
     * * * * *
     i
      <----j->
     * * * * *
       i
        <--j->
     * * * * *
         i
          <j->
     * * * * *
           i
            j
     */

    size_t n = arr.size();
    for (int i = 0; i <= n - 2; i++) {
        // find minIndex in arr[i, n-1]
        int minIndex = i;
        for (int j = i + 1; j <= n - 1; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // -----------------------------
        std::swap(arr[i], arr[minIndex]);
    }

}


template <class T>
void insertionSort(std::vector<T> &arr) {
    /*
     arr[0, i-1] sorted
     arr[i, end] unsorted
    */

    size_t n = arr.size();
    for (int i = 0; i < n; i++) {
        int j = i;
        while (j >= 1 && arr[j - 1] > arr[j]) {
            std::swap(arr[j - 1], arr[j]);
            j--;
        }
    }
}


template <class T>
void gnomeSort(std::vector<T> &arr) {
    size_t n = arr.size();
    for (int i = 1; i < n;) {
        if (i < 1 || arr[i - 1] < arr[i]) {
            i++;
        } else {
            std::swap(arr[i - 1], arr[i]);
            i--;
        }
    }
}

template <class T>
void bubbleSort(std::vector<T> &arr) {
    /*

     * * * * *
     <--i--> j
     * * * * *
     <-i-> j
     * * * * *
     <i> j
     * * * * *
     i j

    */

    size_t n = arr.size();
    for (int j = n - 1; j >= 1; j--) {
        for (int i = 0; i <= j - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
            }
        }
    }
}

template <class T>
int partition(std::vector<T> &arr, int l, int r) {
    /*
     ... * * * * * ...
         l       r
         i         j

     arr[l, i] <= pivot
     arr[i+1, j-1] to be scanned
     arr[j, r] > pivot

    */

    T pivot = arr[l];
    int i = l;
    int j = r + 1;
    // stop when i+1 > j-1, i.e. arr[i+1, j-1] is empty.
    while (i + 1 <= j -1) {
        if (arr[i + 1] <= pivot) {
            i++;
        } else {
            std::swap(arr[j - 1], arr[i + 1]);
            j--;
        }
    }
    std::swap(arr[l], arr[i]);
    return i;
}

template <class T>
void __quickSort(std::vector<T> &arr, int l, int r) {
    if (l >= r) {
        return;
    }
    int p = partition(arr, l, r);
    __quickSort(arr, l, p - 1);
    __quickSort(arr, p + 1, r);
}

template <class T>
void quickSort(std::vector<T> &arr) {
    __quickSort(arr, 0, arr.size() - 1);
}

template <class T>
void merge(std::vector<T> &arr, int l, int s, int r) {
    /*
     ... * * * * * ...
         l   s   r

     arr[l, s] sorted
     arr[s+1, r] sorted
     */
    std::vector<T> aux;
    int i = l;
    int j = s + 1;
    while (i <= s && j <= r) {
        if (arr[i] < arr[j]) {
            aux.push_back(arr[i++]);
        } else {
            aux.push_back(arr[j++]);
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
}


template <class T>
void __mergeSort(std::vector<T> &arr, int l, int r) {
    if (l >= r) {
        return;
    }
    int m = l + (r - l) / 2;
    __mergeSort(arr, l, m);
    __mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
}

template <class T>
void mergeSort(std::vector<T> &arr) {
    __mergeSort(arr, 0, arr.size() - 1);
}



int main() {
    std::vector<int> arr = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1000};
    //bubbleSort(arr);
    //gnomeSort(arr);
    //selectionSort(arr);
    //insertionSort(arr);
    //quickSort(arr);

    //std::vector<int> arr = {1,3,5,7,9,2,4,6,8,10};
    //merge(arr, 0, 4, 10);

    //mergeSort(arr);
    print(arr);
    return 0;
}
