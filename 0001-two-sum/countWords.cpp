#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// void accept(vector<string> words){
// 	int n;
// 	cout<<"Enter the number of words: ";
// 	cin>>n;
	
// 	for(int i=0; i<n; i++){
// 		string temp;
// 		cout<<i<<"th word: ";
// 		cin>>temp;
// 		words.push_back(temp);
// 	}
// }

// void check(vector<string> words){
// 	unordered_map<string, int> umap;	
// 	for(int i=0; i<words.size(); i++){
// 		for(auto x: umap){
// 			if(x.first == words[i]) x.second++;
// 			else umap[words[i]];
// 		}
// 	}
	
// 	cout<<umap.size()<<endl;
	
// 	for(auto x: umap){
// 		cout<<x.second<<endl;
// 	}
	
	// int n=words.size();
	// vector<int> counts(n, 0);
	// int count=0;
	
	// for(int i=0; i<words.size(); i++){
	// 	for(int j=i; j<words.size(); j++){
	// 		if(words[i]==words[j]){
	// 			counts[i]++;
	// 			count++;
	// 		}else{
	// 			count++;
	// 		}
	// 	}
	// }	
	// cout<<count<<endl;
	// for(int i=0; i<words.size(); i++){
	// 	cout<<counts[i]<<endl;
	// }
// }


int main() {
	vector<string> words;
  int num;
	cout<<"Enter the number of words: ";
	cin>>num;
	
	for(int i=0; i<num; i++){
		string temp;
		cout<<i<<"th word: ";
		cin>>temp;
		words.push_back(temp);
	}
	
	// accept(words);
int n=words.size();
	vector<int> counts(n, 1);
  // int counts[n];
	int count=0;
	
	for(int i=0; i<words.size(); i++){
		for(int j=i+1; j<words.size(); j++){
			if(words[i]==words[j]){
				counts[i]++;
			}else{
        //counts.push_back(1);
				// count++;
			}
		}
	}	
	cout<<counts.size()<<endl;
	for(int i=0; i<count; i++){
		cout<<counts[i]<<endl;
	}	
	return 0;
}
