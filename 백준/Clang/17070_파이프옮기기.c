#include <stdio.h>

int arr[20][20];
int n;

void dfs(int x, int y, int direction){
	arr[x][y]++;
	
	if(direction==0 || direction==2){
		if(y<n && arr[x][y+1]!=-1)
			dfs(x,y+1,0);
	}
	if(direction==1 || direction==2){
		if(x<n && arr[x+1][y]!=-1)
			dfs(x+1,y,1);
	}
	if(x<n && y<n && arr[x][y+1]!=-1 && arr[x+1][y]!=-1 && arr[x+1][y+1]!=-1)
		dfs(x+1,y+1,2);
	
	return;
}

int main(){
	scanf("%d",&n);
	
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++){
			scanf("%d",&arr[i][j]);
			if(arr[i][j]==1) arr[i][j] = -1;
		}
	
	//0:가로, 1:세로, 2:대각선
	dfs(1,2,0);
	
	if(arr[n][n]==-1) arr[n][n] = 0;
	
	printf("%d",arr[n][n]);
	
	return 0;
}