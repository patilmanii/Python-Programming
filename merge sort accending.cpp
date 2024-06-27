//Mwerge sort algorthim
#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int l, int m, int r) {
    vector<int> L(arr.begin() + l, arr.begin() + m + 1), 
	R(arr.begin() + m + 1, arr.begin() + r + 1);
    
	for (int i = l, j = 0, k = 0; i <= r; ++i)
        
	arr[i] = (j < L.size() && (k >= R.size() || L[j] <= R[k])) ? L[j++] : R[k++];
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    
    vector<int> arr(n);
    
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) 
	cin >> arr[i];
    
	mergeSort(arr, 0, n - 1);
    
    for (int i = 0; i < n; i++) 
	cout << arr[i] << " ";
    cout << endl;
    return 0;
}

