#include <iostream>
#include <vector>
using namespace std;

int CountingTrailingZeros(int n){
	int count=0;
	
	// contagem de quantas vezes e possivel divir o fatorial por 5 e seus multiplos
	for(int i=5; n/i >= 1; i *= 5)
		count += n/i;
	
	return count;
}
int main() {
	int n, aux;
	cin >> n;
	
	std::vector<int> inputs;
	
	for(int i=0; i<=n; i++){
		cin >> aux;
		inputs.push_back(aux);
	}
	
	for(int i=0; i<=n; i++){
		cout << CountingTrailingZeros(inputs[i]) << endl;
	}
	
	return 0;
}
